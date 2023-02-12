# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'guessAhmrwa.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(561, 548)
        MainWindow.setStyleSheet(u"background-color: rgb(170, 170, 255);")
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.guessbtn = QPushButton(self.centralwidget)
        self.guessbtn.setObjectName(u"guessbtn")
        self.guessbtn.setGeometry(QRect(80, 390, 401, 51))
        font = QFont()
        font.setPointSize(18)
        self.guessbtn.setFont(font)
        self.guessbtn.setStyleSheet(u"border-radius: 25px;\n"
"background-color: rgb(170, 255, 255);")
        self.textbtn = QPlainTextEdit(self.centralwidget)
        self.textbtn.setObjectName(u"textbtn")
        self.textbtn.setGeometry(QRect(230, 230, 101, 111))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textbtn.sizePolicy().hasHeightForWidth())
        self.textbtn.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(24)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setUnderline(False)
        font1.setStrikeOut(False)
        font1.setKerning(True)
        self.textbtn.setFont(font1)
        self.textbtn.setMouseTracking(False)
        self.textbtn.setFocusPolicy(Qt.ClickFocus)
        self.textbtn.setToolTipDuration(4)
        self.textbtn.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(10, 10, 10);\n"
"border-radius: 1px;")
        self.textbtn.setFrameShape(QFrame.Box)
        self.textbtn.setLineWidth(5)
        self.textbtn.setMidLineWidth(5)
        self.textbtn.setBackgroundVisible(False)
        self.textbtn.setCenterOnScroll(False)
        self.resultbtn = QPushButton(self.centralwidget)
        self.resultbtn.setObjectName(u"resultbtn")
        self.resultbtn.setGeometry(QRect(180, 290, 201, 91))
        font2 = QFont()
        font2.setPointSize(19)
        font2.setBold(True)
        self.resultbtn.setFont(font2)
        self.resultbtn.setStyleSheet(u"color: rgb(0, 0, 127);\n"
"border-radius: 15px;\n"
"background-color: rgb(170, 170, 255);")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(110, 20, 361, 71))
        font3 = QFont()
        font3.setFamily(u"Comic Sans MS")
        font3.setPointSize(22)
        font3.setBold(True)
        self.pushButton.setFont(font3)
        self.pushButton.setStyleSheet(u"border-radius: 10px;\n"
"color: rgb(132, 0, 198);")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(90, 140, 381, 71))
        font4 = QFont()
        font4.setPointSize(10)
        self.pushButton_2.setFont(font4)
        self.pushButton_2.setStyleSheet(u"border-radius: 10px;")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 561, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.guessbtn.setText(QCoreApplication.translate("MainWindow", u"Guess", None))
#if QT_CONFIG(tooltip)
        self.textbtn.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.textbtn.setPlainText("")
        self.resultbtn.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"GUESS NUMBER ", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"For each guess , Enter your number in the box \n"
"(between 1 to 50)\n"
"&& press Guess button  ", None))
    # retranslateUi

