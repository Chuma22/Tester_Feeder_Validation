# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QLCDNumber, QLabel,
    QLayout, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTextBrowser, QWidget)
import resources.resources

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1568, 785)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.startPushButton = QPushButton(self.centralwidget)
        self.startPushButton.setObjectName(u"startPushButton")
        self.startPushButton.setGeometry(QRect(70, 510, 121, 51))
        self.stopPushButton = QPushButton(self.centralwidget)
        self.stopPushButton.setObjectName(u"stopPushButton")
        self.stopPushButton.setGeometry(QRect(70, 590, 121, 51))
        self.inputLcdNumber = QLCDNumber(self.centralwidget)
        self.inputLcdNumber.setObjectName(u"inputLcdNumber")
        self.inputLcdNumber.setGeometry(QRect(1180, 170, 151, 81))
        self.messagesTextBrowser = QTextBrowser(self.centralwidget)
        self.messagesTextBrowser.setObjectName(u"messagesTextBrowser")
        self.messagesTextBrowser.setGeometry(QRect(10, 10, 1511, 81))
        self.messagesTextBrowser.setAutoFillBackground(False)
        self.messagesTextBrowser.setStyleSheet(u"background-color: rgb(255, 255, 0);")
        self.imagesLabel = QLabel(self.centralwidget)
        self.imagesLabel.setObjectName(u"imagesLabel")
        self.imagesLabel.setGeometry(QRect(280, 110, 849, 665))
        self.imagesLabel.setContextMenuPolicy(Qt.PreventContextMenu)
        self.imagesLabel.setPixmap(QPixmap(u":/Images/Tester.png"))
        self.RestartPushButton = QPushButton(self.centralwidget)
        self.RestartPushButton.setObjectName(u"RestartPushButton")
        self.RestartPushButton.setGeometry(QRect(70, 670, 121, 51))
        self.outputLcdNumber = QLCDNumber(self.centralwidget)
        self.outputLcdNumber.setObjectName(u"outputLcdNumber")
        self.outputLcdNumber.setGeometry(QRect(1180, 300, 151, 81))
        self.railLcdNumber = QLCDNumber(self.centralwidget)
        self.railLcdNumber.setObjectName(u"railLcdNumber")
        self.railLcdNumber.setGeometry(QRect(1180, 440, 151, 81))
        self.unitsIntLabel = QLabel(self.centralwidget)
        self.unitsIntLabel.setObjectName(u"unitsIntLabel")
        self.unitsIntLabel.setGeometry(QRect(1180, 130, 141, 20))
        self.unitsOutLabel = QLabel(self.centralwidget)
        self.unitsOutLabel.setObjectName(u"unitsOutLabel")
        self.unitsOutLabel.setGeometry(QRect(1190, 270, 111, 20))
        self.priorityRailLabel = QLabel(self.centralwidget)
        self.priorityRailLabel.setObjectName(u"priorityRailLabel")
        self.priorityRailLabel.setGeometry(QRect(1190, 400, 101, 20))
        self.timeProductionLabel = QLabel(self.centralwidget)
        self.timeProductionLabel.setObjectName(u"timeProductionLabel")
        self.timeProductionLabel.setGeometry(QRect(1180, 560, 141, 20))
        self.lastResultLabel = QLabel(self.centralwidget)
        self.lastResultLabel.setObjectName(u"lastResultLabel")
        self.lastResultLabel.setGeometry(QRect(80, 120, 131, 21))
        self.timeProductionTextBrowser = QTextBrowser(self.centralwidget)
        self.timeProductionTextBrowser.setObjectName(u"timeProductionTextBrowser")
        self.timeProductionTextBrowser.setGeometry(QRect(1170, 600, 181, 31))
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(30, 140, 211, 361))
        self.lastResultQFrom = QFormLayout(self.layoutWidget)
        self.lastResultQFrom.setObjectName(u"lastResultQFrom")
        self.lastResultQFrom.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.lastResultQFrom.setFieldGrowthPolicy(QFormLayout.ExpandingFieldsGrow)
        self.lastResultQFrom.setRowWrapPolicy(QFormLayout.WrapLongRows)
        self.lastResultQFrom.setLabelAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.lastResultQFrom.setFormAlignment(Qt.AlignJustify|Qt.AlignTop)
        self.lastResultQFrom.setHorizontalSpacing(15)
        self.lastResultQFrom.setVerticalSpacing(18)
        self.lastResultQFrom.setContentsMargins(22, 12, 18, 14)
        self.testN1Label = QLabel(self.layoutWidget)
        self.testN1Label.setObjectName(u"testN1Label")

        self.lastResultQFrom.setWidget(0, QFormLayout.LabelRole, self.testN1Label)

        self.testN2Label = QLabel(self.layoutWidget)
        self.testN2Label.setObjectName(u"testN2Label")

        self.lastResultQFrom.setWidget(0, QFormLayout.FieldRole, self.testN2Label)

        self.resultN1Label = QLabel(self.layoutWidget)
        self.resultN1Label.setObjectName(u"resultN1Label")
        self.resultN1Label.setEnabled(True)
        font = QFont()
        font.setKerning(True)
        self.resultN1Label.setFont(font)
        self.resultN1Label.setAutoFillBackground(False)
        self.resultN1Label.setStyleSheet(u"background-color:rgb(170, 170, 127)")

        self.lastResultQFrom.setWidget(1, QFormLayout.LabelRole, self.resultN1Label)

        self.resultN2Label = QLabel(self.layoutWidget)
        self.resultN2Label.setObjectName(u"resultN2Label")
        self.resultN2Label.setStyleSheet(u"background-color:rgb(170, 170, 127)")

        self.lastResultQFrom.setWidget(1, QFormLayout.FieldRole, self.resultN2Label)

        self.testN3Label = QLabel(self.layoutWidget)
        self.testN3Label.setObjectName(u"testN3Label")

        self.lastResultQFrom.setWidget(2, QFormLayout.LabelRole, self.testN3Label)

        self.testN4Label = QLabel(self.layoutWidget)
        self.testN4Label.setObjectName(u"testN4Label")

        self.lastResultQFrom.setWidget(2, QFormLayout.FieldRole, self.testN4Label)

        self.resultN3Label = QLabel(self.layoutWidget)
        self.resultN3Label.setObjectName(u"resultN3Label")
        self.resultN3Label.setStyleSheet(u"background-color:rgb(170, 170, 127)")

        self.lastResultQFrom.setWidget(3, QFormLayout.LabelRole, self.resultN3Label)

        self.resultN4Label = QLabel(self.layoutWidget)
        self.resultN4Label.setObjectName(u"resultN4Label")
        self.resultN4Label.setStyleSheet(u"background-color:rgb(170, 170, 127)")

        self.lastResultQFrom.setWidget(3, QFormLayout.FieldRole, self.resultN4Label)

        self.testN5Label = QLabel(self.layoutWidget)
        self.testN5Label.setObjectName(u"testN5Label")

        self.lastResultQFrom.setWidget(4, QFormLayout.LabelRole, self.testN5Label)

        self.testN6Label = QLabel(self.layoutWidget)
        self.testN6Label.setObjectName(u"testN6Label")

        self.lastResultQFrom.setWidget(4, QFormLayout.FieldRole, self.testN6Label)

        self.resultN5Label = QLabel(self.layoutWidget)
        self.resultN5Label.setObjectName(u"resultN5Label")
        self.resultN5Label.setStyleSheet(u"background-color:rgb(170, 170, 127)")

        self.lastResultQFrom.setWidget(5, QFormLayout.LabelRole, self.resultN5Label)

        self.resultN6Label = QLabel(self.layoutWidget)
        self.resultN6Label.setObjectName(u"resultN6Label")
        self.resultN6Label.setStyleSheet(u"background-color:rgb(170, 170, 127)")

        self.lastResultQFrom.setWidget(5, QFormLayout.FieldRole, self.resultN6Label)

        self.testN7Label = QLabel(self.layoutWidget)
        self.testN7Label.setObjectName(u"testN7Label")

        self.lastResultQFrom.setWidget(6, QFormLayout.LabelRole, self.testN7Label)

        self.testN8Label = QLabel(self.layoutWidget)
        self.testN8Label.setObjectName(u"testN8Label")

        self.lastResultQFrom.setWidget(6, QFormLayout.FieldRole, self.testN8Label)

        self.resultN7Label = QLabel(self.layoutWidget)
        self.resultN7Label.setObjectName(u"resultN7Label")
        self.resultN7Label.setStyleSheet(u"background-color:rgb(170, 170, 127)")

        self.lastResultQFrom.setWidget(7, QFormLayout.LabelRole, self.resultN7Label)

        self.resultN8Label = QLabel(self.layoutWidget)
        self.resultN8Label.setObjectName(u"resultN8Label")
        self.resultN8Label.setStyleSheet(u"background-color:rgb(170, 170, 127)")

        self.lastResultQFrom.setWidget(7, QFormLayout.FieldRole, self.resultN8Label)

        self.validationN1Label = QLabel(self.layoutWidget)
        self.validationN1Label.setObjectName(u"validationN1Label")

        self.lastResultQFrom.setWidget(8, QFormLayout.LabelRole, self.validationN1Label)

        self.validationN2Label = QLabel(self.layoutWidget)
        self.validationN2Label.setObjectName(u"validationN2Label")

        self.lastResultQFrom.setWidget(8, QFormLayout.FieldRole, self.validationN2Label)

        self.resultValidationN1Label = QLabel(self.layoutWidget)
        self.resultValidationN1Label.setObjectName(u"resultValidationN1Label")
        self.resultValidationN1Label.setStyleSheet(u"background-color:rgb(170, 170, 127)")

        self.lastResultQFrom.setWidget(9, QFormLayout.LabelRole, self.resultValidationN1Label)

        self.resultValidationN2Label = QLabel(self.layoutWidget)
        self.resultValidationN2Label.setObjectName(u"resultValidationN2Label")
        self.resultValidationN2Label.setStyleSheet(u"background-color:rgb(170, 170, 127)")

        self.lastResultQFrom.setWidget(9, QFormLayout.FieldRole, self.resultValidationN2Label)

        MainWindow.setCentralWidget(self.centralwidget)
        self.imagesLabel.raise_()
        self.startPushButton.raise_()
        self.stopPushButton.raise_()
        self.inputLcdNumber.raise_()
        self.messagesTextBrowser.raise_()
        self.RestartPushButton.raise_()
        self.outputLcdNumber.raise_()
        self.railLcdNumber.raise_()
        self.unitsIntLabel.raise_()
        self.unitsOutLabel.raise_()
        self.priorityRailLabel.raise_()
        self.timeProductionLabel.raise_()
        self.lastResultLabel.raise_()
        self.timeProductionTextBrowser.raise_()
        self.layoutWidget.raise_()
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1568, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.startPushButton.setText(QCoreApplication.translate("MainWindow", u"Inicio", None))
        self.stopPushButton.setText(QCoreApplication.translate("MainWindow", u"Detener", None))
        self.messagesTextBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:36pt; font-weight:700;\">STOP!!</span></p></body></html>", None))
        self.imagesLabel.setText("")
        self.RestartPushButton.setText(QCoreApplication.translate("MainWindow", u"Restablecer ", None))
        self.unitsIntLabel.setText(QCoreApplication.translate("MainWindow", u"Piezas Entrada", None))
        self.unitsOutLabel.setText(QCoreApplication.translate("MainWindow", u"Piezas Salida", None))
        self.priorityRailLabel.setText(QCoreApplication.translate("MainWindow", u"Prioridad del riel", None))
        self.timeProductionLabel.setText(QCoreApplication.translate("MainWindow", u"Tiempo de produccion ", None))
        self.lastResultLabel.setText(QCoreApplication.translate("MainWindow", u"Resultados previos ", None))
        self.timeProductionTextBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">0 S</span></p></body></html>", None))
        self.testN1Label.setText(QCoreApplication.translate("MainWindow", u"Tester Nido1", None))
        self.testN2Label.setText(QCoreApplication.translate("MainWindow", u"Tester Nido 2", None))
        self.resultN1Label.setText(QCoreApplication.translate("MainWindow", u"Null", None))
        self.resultN2Label.setText(QCoreApplication.translate("MainWindow", u"Null", None))
        self.testN3Label.setText(QCoreApplication.translate("MainWindow", u"Tester Nido 3", None))
        self.testN4Label.setText(QCoreApplication.translate("MainWindow", u"Tester Nido 4", None))
        self.resultN3Label.setText(QCoreApplication.translate("MainWindow", u"Null", None))
        self.resultN4Label.setText(QCoreApplication.translate("MainWindow", u"Null", None))
        self.testN5Label.setText(QCoreApplication.translate("MainWindow", u"Tester Nido 5", None))
        self.testN6Label.setText(QCoreApplication.translate("MainWindow", u"Tester Nido 6", None))
        self.resultN5Label.setText(QCoreApplication.translate("MainWindow", u"Null", None))
        self.resultN6Label.setText(QCoreApplication.translate("MainWindow", u"Null", None))
        self.testN7Label.setText(QCoreApplication.translate("MainWindow", u"Tester Nido 7", None))
        self.testN8Label.setText(QCoreApplication.translate("MainWindow", u"Tester Nido 8", None))
        self.resultN7Label.setText(QCoreApplication.translate("MainWindow", u"Null", None))
        self.resultN8Label.setText(QCoreApplication.translate("MainWindow", u"Null", None))
        self.validationN1Label.setText(QCoreApplication.translate("MainWindow", u"Validacion Nido 1", None))
        self.validationN2Label.setText(QCoreApplication.translate("MainWindow", u"Validacion Nido2", None))
        self.resultValidationN1Label.setText(QCoreApplication.translate("MainWindow", u"Null", None))
        self.resultValidationN2Label.setText(QCoreApplication.translate("MainWindow", u"Null", None))
    # retranslateUi

