# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainMGkSaq.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(802, 600)
        self.fileopen = QAction(MainWindow)
        self.fileopen.setObjectName(u"fileopen")
        self.action_2 = QAction(MainWindow)
        self.action_2.setObjectName(u"action_2")
        self.help = QAction(MainWindow)
        self.help.setObjectName(u"help")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.background = QLabel(self.centralwidget)
        self.background.setObjectName(u"background")
        self.background.setEnabled(False)
        self.background.setGeometry(QRect(-200, -60, 1271, 1001))
        self.background.setStyleSheet(u"background:black;\n"
"")
        self.orgdata = QLabel(self.centralwidget)
        self.orgdata.setObjectName(u"orgdata")
        self.orgdata.setGeometry(QRect(30, 20, 81, 21))
        font = QFont()
        font.setPointSize(12)
        self.orgdata.setFont(font)
        self.orgdata.setStyleSheet(u"color:white;")
        self.labeldata = QLabel(self.centralwidget)
        self.labeldata.setObjectName(u"labeldata")
        self.labeldata.setGeometry(QRect(30, 260, 81, 21))
        self.labeldata.setFont(font)
        self.labeldata.setStyleSheet(u"color:white;")
        self.next = QPushButton(self.centralwidget)
        self.next.setObjectName(u"next")
        self.next.setGeometry(QRect(700, 490, 81, 41))
        self.prev = QPushButton(self.centralwidget)
        self.prev.setObjectName(u"prev")
        self.prev.setGeometry(QRect(580, 490, 81, 41))
        self.label_value = QTextEdit(self.centralwidget)
        self.label_value.setObjectName(u"label_value")
        self.label_value.setGeometry(QRect(30, 300, 711, 141))
        self.label_value.setStyleSheet(u"QTextEdit {\n"
"                color: white;\n"
"                font-size: 14px;\n"
"                background-color: black;\n"
"            }\n"
"")
        self.org_value = QTextEdit(self.centralwidget)
        self.org_value.setObjectName(u"org_value")
        self.org_value.setGeometry(QRect(30, 50, 711, 141))
        self.org_value.setStyleSheet(u"QTextEdit {\n"
"                color: white;\n"
"                font-size: 14px;\n"
"                background-color: black;\n"
"            }\n"
"")
        self.labeldata_2 = QLabel(self.centralwidget)
        self.labeldata_2.setObjectName(u"labeldata_2")
        self.labeldata_2.setGeometry(QRect(180, 480, 131, 21))
        self.labeldata_2.setFont(font)
        self.labeldata_2.setStyleSheet(u"color:white;")
        self.labeldata_3 = QLabel(self.centralwidget)
        self.labeldata_3.setObjectName(u"labeldata_3")
        self.labeldata_3.setGeometry(QRect(30, 480, 131, 21))
        self.labeldata_3.setFont(font)
        self.labeldata_3.setStyleSheet(u"color:white;")
        self.allsentence_value = QLabel(self.centralwidget)
        self.allsentence_value.setObjectName(u"allsentence_value")
        self.allsentence_value.setGeometry(QRect(30, 510, 111, 21))
        self.allsentence_value.setFont(font)
        self.allsentence_value.setStyleSheet(u"color:white;")
        self.nowsentence_value = QLineEdit(self.centralwidget)
        self.nowsentence_value.setObjectName(u"nowsentence_value")
        self.nowsentence_value.setGeometry(QRect(180, 510, 121, 21))
        self.nowsentence_value.setStyleSheet(u"background:black;\n"
"color:white;")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 802, 22))
        self.menugd = QMenu(self.menubar)
        self.menugd.setObjectName(u"menugd")
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menugd.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.menugd.addAction(self.fileopen)
        self.menu.addAction(self.help)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.fileopen.setText(QCoreApplication.translate("MainWindow", u"\ud30c\uc77c\uc5f4\uae30", None))
        self.action_2.setText(QCoreApplication.translate("MainWindow", u"\uc790\ub3d9\uc800\uc7a5", None))
        self.help.setText(QCoreApplication.translate("MainWindow", u"\ub2e8\ucd95\ud0a4 \ub3c4\uc6c0\ub9d0", None))
        self.background.setText("")
        self.orgdata.setText(QCoreApplication.translate("MainWindow", u"\uc6d0\ubb38\ub370\uc774\ud130", None))
        self.labeldata.setText(QCoreApplication.translate("MainWindow", u"\ub77c\ubca8\ub370\uc774\ud130", None))
        self.next.setText(QCoreApplication.translate("MainWindow", u"\ub2e4\uc74c", None))
        self.prev.setText(QCoreApplication.translate("MainWindow", u"\ub4a4\ub85c", None))
        self.label_value.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'\ub9d1\uc740 \uace0\ub515'; font-size:14px; font-weight:400; font-style:normal;\" bgcolor=\"#000000\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\"> </span></p></body></html>", None))
        self.org_value.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'\ub9d1\uc740 \uace0\ub515'; font-size:14px; font-weight:400; font-style:normal;\" bgcolor=\"#000000\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\"> </span></p></body></html>", None))
        self.labeldata_2.setText(QCoreApplication.translate("MainWindow", u"\ud604\uc7ac \ub77c\ubca8\ub9c1 \uc704\uce58", None))
        self.labeldata_3.setText(QCoreApplication.translate("MainWindow", u"\uc804\uccb4 \ubb38\uc7a5 \uac1c\uc218", None))
        self.allsentence_value.setText("")
        self.menugd.setTitle(QCoreApplication.translate("MainWindow", u"\ud30c\uc77c", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\uc124\uc815", None))
    # retranslateUi

