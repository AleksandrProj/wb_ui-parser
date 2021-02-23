from openpyxl import Workbook


class ExportExcel:
    def __init__(self):
        header = [
            'Фото товара',
            'Название',
            'Бренд',
            'Цена',
            'Рейтинг',
            'Кол-во отзывов',
            'Кол-во покупок',
            'URL',
        ]
        self.wb = Workbook()
        self.ws = self.wb.active

        self.wb.active.append(header)