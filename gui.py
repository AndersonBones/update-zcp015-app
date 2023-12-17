# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QProgressBar, QPushButton, QSizePolicy, QWidget)

class Ui_main_window(object):
    def setupUi(self, main_window):
        if not main_window.objectName():
            main_window.setObjectName(u"main_window")
        main_window.resize(579, 284)
        main_window.setStyleSheet(u"background-color: rgb(254, 254, 254);\n"
"\n"
"button:{\n"
"	border:none;\n"
"	border-radius:5px\n"
"}")
        self.exit_button = QPushButton(main_window)
        self.exit_button.setObjectName(u"exit_button")
        self.exit_button.setGeometry(QRect(20, 230, 71, 31))
        self.exit_button.setStyleSheet(u"background-color:'white';\n"
"\n"
"border:1px solid #0072ff;\n"
"color:#0072ff;\n"
"font-weight:600;\n"
"box-shadow: rgba(0, 0, 0, 0.15) 1.95px 1.95px 2.6px;\n"
"border-radius:5px;\n"
"\n"
"")
        self.run_process_btn = QPushButton(main_window)
        self.run_process_btn.setObjectName(u"run_process_btn")
        self.run_process_btn.setGeometry(QRect(100, 230, 91, 31))
        self.run_process_btn.setMaximumSize(QSize(16777215, 16777215))
        self.run_process_btn.setStyleSheet(u"background-color: rgb(0, 114, 255);\n"
"border:none;\n"
"color:'white';\n"
"font-weight:600;\n"
"box-shadow: rgba(0, 0, 0, 0.15) 1.95px 1.95px 2.6px;\n"
"border-radius:5px;")
        self.search_file_btn = QPushButton(main_window)
        self.search_file_btn.setObjectName(u"search_file_btn")
        self.search_file_btn.setGeometry(QRect(470, 100, 81, 31))
        self.search_file_btn.setStyleSheet(u"background-color: rgb(0, 114, 255);\n"
"border:none;\n"
"color:'white';\n"
"font-weight:600;\n"
"box-shadow: rgba(0, 0, 0, 0.15) 1.95px 1.95px 2.6px;\n"
"border-radius:5px;")
        self.lineEdit = QLineEdit(main_window)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(20, 100, 441, 31))
        self.lineEdit.setStyleSheet(u"border:1px solid #0072ff;\n"
"border-radius:5px;")
        self.title = QLabel(main_window)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(20, 10, 421, 31))
        font = QFont()
        font.setFamilies([u"Calibri"])
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStyleStrategy(QFont.PreferDefault)
        self.title.setFont(font)
        self.title.setStyleSheet(u"color: rgb(84, 84, 84);")
        self.info = QLabel(main_window)
        self.info.setObjectName(u"info")
        self.info.setGeometry(QRect(20, 60, 231, 21))
        font1 = QFont()
        font1.setPointSize(10)
        self.info.setFont(font1)
        self.info.setStyleSheet(u"color: rgb(0, 114, 255);")
        self.label = QLabel(main_window)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(390, 260, 171, 20))
        self.progressBar = QProgressBar(main_window)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(20, 170, 441, 21))
        self.progressBar.setStyleSheet(u"QProgressBar{\n"
"	text-align:center;\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"	border:1px solid  rgba(0, 114, 255, 255);\n"
"	border-radius:5px;\n"
"	font-weight:600;\n"
"	color: rgb(84, 84, 84);\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"	\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #00c6ff, stop:1 rgba(0, 114, 255, 255));\n"
"}")
        self.progressBar.setValue(24)
        self.label_2 = QLabel(main_window)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 150, 61, 16))
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color: rgb(0, 114, 255);")
        self.exit_button.raise_()
        self.run_process_btn.raise_()
        self.search_file_btn.raise_()
        self.lineEdit.raise_()
        self.info.raise_()
        self.label.raise_()
        self.progressBar.raise_()
        self.label_2.raise_()
        self.title.raise_()

        self.retranslateUi(main_window)

        QMetaObject.connectSlotsByName(main_window)
    # setupUi

    def retranslateUi(self, main_window):
        main_window.setWindowTitle(QCoreApplication.translate("main_window", u"UPDATE ZCP015", None))
        self.exit_button.setText(QCoreApplication.translate("main_window", u"Sair", None))
        self.run_process_btn.setText(QCoreApplication.translate("main_window", u"Processar", None))
        self.search_file_btn.setText(QCoreApplication.translate("main_window", u"Procurar", None))
        self.title.setText(QCoreApplication.translate("main_window", u"Atualiza\u00e7\u00e3o de Base de Dados ZCP015", None))
        self.info.setText(QCoreApplication.translate("main_window", u"Selecione a Base com os novos dados", None))
        self.label.setText(QCoreApplication.translate("main_window", u"Desenvolvido com \u2764 por Anderson", None))
        self.label_2.setText(QCoreApplication.translate("main_window", u"Progresso", None))
    # retranslateUi

