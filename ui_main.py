# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_organizador.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(828, 693)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color:rgb(255, 255, 255)")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.text_path = QLineEdit(self.frame)
        self.text_path.setObjectName(u"text_path")
        self.text_path.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.text_path)

        self.btn_open = QPushButton(self.frame)
        self.btn_open.setObjectName(u"btn_open")
        self.btn_open.setStyleSheet(u"QPushButton{border-top-radius:15px; background-color:rgb(234, 234, 234)}\n"
"QPushButton:hover{color:#fff, background-color: rgb(0, 157, 235)}")

        self.horizontalLayout_2.addWidget(self.btn_open)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget = QWidget(self.frame)
        self.widget.setObjectName(u"widget")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(160, 10, 151, 111))

        self.horizontalLayout.addWidget(self.widget)

        self.btn_exec = QPushButton(self.frame)
        self.btn_exec.setObjectName(u"btn_exec")
        self.btn_exec.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_exec.setStyleSheet(u"QPushButton{border-top-radius:15px; background-color:rgb(234, 234, 234)}")

        self.horizontalLayout.addWidget(self.btn_exec)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html>\n"
"<head/>\n"
"<body>\n"
"<p align=\"center\">\n"
"<img src=\"C:\\Auto\\robotpy\\_imgs\\icone.png\">\n"
"</p>\n"
"<p align=\"center\">\n"
"<span style=\" font-size:14pt; font-weight:600;\">\n"
"Organizador de arquivos nas pastas</span>\n"
"</p>\n"
"</body>\n"
"</html>", None))
        self.text_path.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Selecione a pasta", None))
        self.btn_open.setText(QCoreApplication.translate("MainWindow", u"Abrir Dir", None))
        self.label_3.setText("")
        self.btn_exec.setText(QCoreApplication.translate("MainWindow", u"Organizar", None))
        self.label_2.setText("")
    # retranslateUi

