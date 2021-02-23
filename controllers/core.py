import requests
import time
import os
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from controllers.main_func import insert_row
from controllers.export_excel import ExportExcel
from controllers.settings import USER_AGENT


class WildberriesBot:
    def __init__(self, bot_ui):
        self.bot_ui = bot_ui
        self.site = 'https://www.wildberries.ru'
        self.product_file = ExportExcel()
        self.num_page = 0
        self.query = ''
        self.quantity_page = 0
        self.filename = ''

        # Данные для Chrome браузера
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        self.browser = webdriver.Chrome(os.path.join(os.path.abspath(''), 'drivers', 'chromedriver'),
                                        options=chrome_options)

        self.session = requests.Session()
        self.session.headers = {
            'User-Agent': USER_AGENT,
            'Accept-Language': 'ru',
        }

    def initialization_bot(self, keyword, qty_page, filename):
        self.query = keyword
        self.quantity_page = qty_page
        self.filename = filename

    def load_page(self, url_page=''):
        # сделать получение запроса от пользователя
        site = self.site
        url_page_start = site + '/catalog/0/search.aspx?search={}&sort=popular&page=1'.format(self.query)
        url_page_pagination = site + url_page
        url = url_page_start if url_page == '' else url_page_pagination
        res = self.session.get(url)
        res.raise_for_status()
        return {
            'res': res.text,
            'query': self.query
        }

    def write_csv(self, info_good, ws):
        photo_size = (200, 200)
        insert_row(ws, info_good, size=photo_size)

    def pagination_page(self, pagination_block):
        # Работа с пагинацией
        if pagination_block.text.strip() != '':
            pagination_page = pagination_block.find(class_='pagination-next')

            if pagination_page is not None:
                self.parse_page(self.load_page(url_page=pagination_page.get('href')))
            else:
                return None

    def parse_page(self, res):
        soup = BeautifulSoup(res['res'], 'lxml')
        table_goods = soup.find('div', class_='catalog_main_table').select('.j-card-item')
        pagination = soup.find('div', class_='pager-bottom').find('div', class_='pageToInsert')
        file = self.filename
        self.num_page += 1
        num_stream = self.num_page
        pattern_no_text = r'[а-яА-Я]|\s'

        if self.num_page <= self.quantity_page or self.quantity_page == 0:
            self.bot_ui.statusParser.append('Начался парсинг товаров на странице №' + str(self.num_page))
            print('Начался парсинг товаров на странице №' + str(self.num_page))

            # Цикл парсинга товаров
            for card_good in table_goods:
                # Получаем данные с мини-карточки товара
                block_good = card_good.find('div', class_='dtList-inner')
                title_brand_price_block = block_good.find('div', class_='dtlist-inner-brand')
                url_photo_block = block_good.find('a', class_='j-open-full-product-card')

                title_good = title_brand_price_block.find('span', class_='goods-name').text
                brand_good = title_brand_price_block.find('strong', class_='brand-name').text
                price_good = title_brand_price_block.find('div', class_='j-cataloger-price').find(class_='lower-price').text
                url_full_good = self.site + url_photo_block.get('href')

                # Получаем данные с полной карточки товара
                self.browser.get(url_full_good)
                info_card_rating_good = self.browser.find_element_by_class_name('card-row').find_element_by_class_name(
                    'product-rating').find_element_by_tag_name('span').text
                info_card_reviews_good = self.browser.find_element_by_class_name('card-row').find_element_by_class_name(
                    'count-review').find_element_by_tag_name('span').text
                info_card_quantity_good = self.browser.find_element_by_class_name('card-row').find_element_by_class_name(
                    'order-quantity').text
                info_card_photo_good = self.browser.find_element_by_class_name('card-left').find_element_by_class_name(
                    'j-zoom-photo').get_attribute('src')

                # Запись товара в файл CSV
                self.write_csv({
                    'title': title_good,
                    'brand': brand_good,
                    'price': price_good,
                    'url': url_full_good,
                    'photo': info_card_photo_good,
                    'rating': info_card_rating_good,
                    'reviews': re.sub(pattern_no_text, '', info_card_reviews_good),
                    'quantity': re.sub(pattern_no_text, '', info_card_quantity_good),
                }, self.product_file.ws)

                self.bot_ui.statusParser.append('парсим товар')
                print('парсим товар')
                time.sleep(1)

            # Пагинация
            if self.pagination_page(pagination) is None:
                self.product_file.wb.save(file)
        else:
            self.product_file.wb.save(file)

        if num_stream == 1:
            self.bot_ui.statusParser.append('Парсинг товаров окончен')
            print('Парсинг товаров окончен')
            self.browser.quit()

    def run(self):
        html = self.load_page()
        try:
            self.parse_page(html)
        except AttributeError:
            self.bot_ui.statusParser.append('Такого товара нет на Wildberries. Введите другой запрос')
            print('Такого товара нет на Wildberries. Введите другой запрос')

    def close(self):
        print('Выход из программы')
        self.browser.quit()
