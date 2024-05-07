# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QStatusBar, QTextEdit,
    QWidget)
import os

basedir = os.path.dirname(__file__)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(727, 475)
        MainWindow.setWindowTitle(u"Image Hider")
        MainWindow.setStyleSheet(u"background-color: #ccc;\n"
"\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.appTitle_container = QWidget(self.centralwidget)
        self.appTitle_container.setObjectName(u"appTitle_container")
        self.appTitle_container.setGeometry(QRect(-21, 0, 751, 80))
        self.appTitle_container.setStyleSheet(u"background-color: black\n"
"")
        self.appTitle = QLabel(self.appTitle_container)
        self.appTitle.setObjectName(u"appTitle")
        self.appTitle.setGeometry(QRect(300, 30, 162, 27))
        self.appTitle.setStyleSheet(u"color: teal;\n"
"letter-spacing: 5px;\n"
"font-size: 20px;\n"
"")
        self.display_image = QWidget(self.centralwidget)
        self.display_image.setObjectName(u"display_image")
        self.display_image.setGeometry(QRect(40, 90, 231, 181))
        self.secret_text = QTextEdit(self.centralwidget)
        self.secret_text.setObjectName(u"secret_text")
        self.secret_text.setGeometry(QRect(440, 90, 231, 181))
        self.import_image = QPushButton(self.centralwidget)
        self.import_image.setObjectName(u"import_image")
        self.import_image.setGeometry(QRect(50, 313, 101, 31))
        self.import_image.setStyleSheet(u"\n"
"background-color: royalblue;\n"
"color: yellow;\n"
"border-radius: 15px;\n"
"")
        self.save_image = QPushButton(self.centralwidget)
        self.save_image.setObjectName(u"save_image")
        self.save_image.setGeometry(QRect(190, 313, 101, 31))
        self.save_image.setStyleSheet(u"\n"
"background-color: royalblue;\n"
"color: yellow;\n"
"border-radius: 15px;\n"
"")
        self.reveal_secret = QPushButton(self.centralwidget)
        self.reveal_secret.setObjectName(u"reveal_secret")
        self.reveal_secret.setGeometry(QRect(276, 383, 151, 41))
        self.reveal_secret.setStyleSheet(u"\n"
"background-color: royalblue;\n"
"color: yellow;\n"
"border-radius: 15px;\n"
"")
        self.is_want_enc = QCheckBox(self.centralwidget)
        self.is_want_enc.setObjectName(u"is_want_enc")
        self.is_want_enc.setGeometry(QRect(440, 320, 118, 20))
        self.is_want_enc.setStyleSheet(u"color: royalblue;")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        self.appTitle.setText(QCoreApplication.translate("MainWindow", u"Image Hider", None))
        self.import_image.setText(QCoreApplication.translate("MainWindow", u"Import Image", None))
        self.save_image.setText(QCoreApplication.translate("MainWindow", u"Save Image", None))
        self.reveal_secret.setText(QCoreApplication.translate("MainWindow", u"Reveal Secret", None))
        self.is_want_enc.setText(QCoreApplication.translate("MainWindow", u"Enable Encryption", None))
        pass
    # retranslateUi

