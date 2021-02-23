# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'parser-wb.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 400)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(400, 400))
        MainWindow.setMaximumSize(QtCore.QSize(400, 400))
        MainWindow.setStyleSheet("background-color: #481173;\n"
"color: white;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.statusParser = QtWidgets.QTextBrowser(self.centralwidget)
        self.statusParser.setGeometry(QtCore.QRect(10, 200, 381, 180))
        self.statusParser.setStyleSheet("background-color: white;\n"
"color: black;")
        self.statusParser.setObjectName("statusParser")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 381, 165))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.keywordParser = QtWidgets.QLineEdit(self.layoutWidget)
        self.keywordParser.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.keywordParser.setText("")
        self.keywordParser.setAlignment(QtCore.Qt.AlignCenter)
        self.keywordParser.setObjectName("keywordParser")
        self.horizontalLayout.addWidget(self.keywordParser)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.qtyPageParser = QtWidgets.QLineEdit(self.layoutWidget)
        self.qtyPageParser.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.qtyPageParser.setText("")
        self.qtyPageParser.setAlignment(QtCore.Qt.AlignCenter)
        self.qtyPageParser.setObjectName("qtyPageParser")
        self.horizontalLayout_2.addWidget(self.qtyPageParser)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4, 0, QtCore.Qt.AlignHCenter)
        self.browseFile = QtWidgets.QPushButton(self.layoutWidget)
        self.browseFile.setStyleSheet("background-color: white;\n"
"color: black;\n"
"border-radius: 10px;\n"
"height: 30px;")
        self.browseFile.setObjectName("browseFile")
        self.horizontalLayout_4.addWidget(self.browseFile)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.startParsingBtn = QtWidgets.QPushButton(self.layoutWidget)
        self.startParsingBtn.setMinimumSize(QtCore.QSize(150, 0))
        self.startParsingBtn.setMaximumSize(QtCore.QSize(100, 16777215))
        self.startParsingBtn.setStyleSheet("background-color: white;\n"
"color: black;\n"
"border-radius: 5px;\n"
"height: 30px;")
        self.startParsingBtn.setObjectName("startParsingBtn")
        self.verticalLayout.addWidget(self.startParsingBtn, 0, QtCore.Qt.AlignHCenter)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Парсер Wildberries"))
        self.label.setText(_translate("MainWindow", "Ключевое слово для парсинга:"))
        self.label_2.setText(_translate("MainWindow", "Сколько страниц парсить (0 - ВСЕ):"))
        self.label_4.setText(_translate("MainWindow", "Куда сохранить файл парсинга:"))
        self.browseFile.setText(_translate("MainWindow", "Выбрать папку..."))
        self.startParsingBtn.setText(_translate("MainWindow", "Начать парсинг"))
