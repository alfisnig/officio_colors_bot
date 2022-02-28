# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'control_panel.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
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
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_control_panel(object):
    def setupUi(self, control_panel):
        if not control_panel.objectName():
            control_panel.setObjectName(u"control_panel")
        control_panel.resize(381, 600)
        control_panel.setMinimumSize(QSize(381, 600))
        control_panel.setMaximumSize(QSize(381, 600))
        self.centralwidget = QWidget(control_panel)
        self.centralwidget.setObjectName(u"centralwidget")
        self.start_bot_button = QPushButton(self.centralwidget)
        self.start_bot_button.setObjectName(u"start_bot_button")
        self.start_bot_button.setGeometry(QRect(70, 160, 241, 71))
        font = QFont()
        font.setPointSize(18)
        font.setBold(False)
        self.start_bot_button.setFont(font)
        self.add_catalog_button = QPushButton(self.centralwidget)
        self.add_catalog_button.setObjectName(u"add_catalog_button")
        self.add_catalog_button.setGeometry(QRect(70, 340, 241, 71))
        self.add_catalog_button.setFont(font)
        self.stop_bot_button = QPushButton(self.centralwidget)
        self.stop_bot_button.setObjectName(u"stop_bot_button")
        self.stop_bot_button.setEnabled(False)
        self.stop_bot_button.setGeometry(QRect(70, 250, 241, 71))
        self.stop_bot_button.setFont(font)
        control_panel.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(control_panel)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 381, 21))
        control_panel.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(control_panel)
        self.statusbar.setObjectName(u"statusbar")
        control_panel.setStatusBar(self.statusbar)

        self.retranslateUi(control_panel)

        QMetaObject.connectSlotsByName(control_panel)
    # setupUi

    def retranslateUi(self, control_panel):
        control_panel.setWindowTitle(QCoreApplication.translate("control_panel", u"MainWindow", None))
        self.start_bot_button.setText(QCoreApplication.translate("control_panel", u"Start bot", None))
        self.add_catalog_button.setText(QCoreApplication.translate("control_panel", u"Add catalog", None))
        self.stop_bot_button.setText(QCoreApplication.translate("control_panel", u"Stop bot", None))
    # retranslateUi

