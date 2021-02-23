from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMainWindow
from controllers.parser_ui import Ui_MainWindow
from controllers.core import WildberriesBot
import sys
import os
import threading


class ParserUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.filename = ''
        self.__init_ui_parser()

    def __init_ui_parser(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()

        # Logical
        self.bot = WildberriesBot(self.ui)
        self.ui.browseFile.clicked.connect(self.__upload_file_parsing)
        self.ui.startParsingBtn.clicked.connect(self.__parsing)

        sys.exit(app.exec_())

    def closeEvent(self, event):
        self.bot.close()

    def __upload_file_parsing(self):
        file_path = QFileDialog.getSaveFileName(self,
                                                'Сохранить Excel файл',
                                                os.path.join(os.path.dirname(os.path.dirname(__file__)), 'files'),
                                                'Excel file (*.xlsx)')
        self.filename = file_path[0]

    def __parsing(self):
        keyword = self.ui.keywordParser.text()
        qty_page = self.ui.qtyPageParser.text()

        if keyword != '' and qty_page != '' and self.filename != '':
            try:
                # Initializing the bot
                self.bot.initialization_bot(keyword, int(qty_page), self.filename)
                bot_thread = threading.Thread(target=self.bot.run, daemon=True)
                bot_thread.start()
                # bot_thread.join()
                # self.ui.statusParser.append('Путь к файлу парсинга: ' + self.filename)
            except ValueError as err:
                print(err)
                self.ui.statusParser.append('Укажите кол-во страниц цифрами')
            except KeyboardInterrupt as err:
                print(err)
                self.ui.statusParser.append('Выполнение программы прервано')
        else:
            self.ui.statusParser.append('Все поля обязательны к заполнению')


app = QtWidgets.QApplication(sys.argv)
