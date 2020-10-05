# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(305, 463)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_4 = QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.formLayout_4 = QFormLayout(self.groupBox)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.label)

        self.spinBox = QSpinBox(self.groupBox)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMaximum(999999999)

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.spinBox)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.spinBox_2 = QSpinBox(self.groupBox)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setMaximum(500)

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.spinBox_2)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.formLayout_4.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.spinBox_3 = QSpinBox(self.groupBox)
        self.spinBox_3.setObjectName(u"spinBox_3")
        self.spinBox_3.setMaximum(500)

        self.formLayout_4.setWidget(2, QFormLayout.FieldRole, self.spinBox_3)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.formLayout_4.setWidget(3, QFormLayout.LabelRole, self.label_4)

        self.spinBox_4 = QSpinBox(self.groupBox)
        self.spinBox_4.setObjectName(u"spinBox_4")
        self.spinBox_4.setMaximum(500)

        self.formLayout_4.setWidget(3, QFormLayout.FieldRole, self.spinBox_4)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.formLayout_4.setWidget(4, QFormLayout.LabelRole, self.label_5)

        self.spinBox_5 = QSpinBox(self.groupBox)
        self.spinBox_5.setObjectName(u"spinBox_5")
        self.spinBox_5.setMaximum(500)

        self.formLayout_4.setWidget(4, QFormLayout.FieldRole, self.spinBox_5)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.formLayout_4.setWidget(5, QFormLayout.LabelRole, self.label_6)

        self.spinBox_6 = QSpinBox(self.groupBox)
        self.spinBox_6.setObjectName(u"spinBox_6")
        self.spinBox_6.setMaximum(999999999)

        self.formLayout_4.setWidget(5, QFormLayout.FieldRole, self.spinBox_6)

        self.groupBox_2 = QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.formLayout_3 = QFormLayout(self.groupBox_2)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_7)

        self.spinBox_13 = QSpinBox(self.groupBox_2)
        self.spinBox_13.setObjectName(u"spinBox_13")
        self.spinBox_13.setMaximum(500)

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.spinBox_13)

        self.label_15 = QLabel(self.groupBox_2)
        self.label_15.setObjectName(u"label_15")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_15)

        self.spinBox_14 = QSpinBox(self.groupBox_2)
        self.spinBox_14.setObjectName(u"spinBox_14")
        self.spinBox_14.setMaximum(500)

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.spinBox_14)

        self.label_16 = QLabel(self.groupBox_2)
        self.label_16.setObjectName(u"label_16")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.label_16)

        self.spinBox_15 = QSpinBox(self.groupBox_2)
        self.spinBox_15.setObjectName(u"spinBox_15")
        self.spinBox_15.setMaximum(500)

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.spinBox_15)


        self.formLayout_4.setWidget(6, QFormLayout.SpanningRole, self.groupBox_2)

        self.pushButton = QPushButton(self.groupBox)
        self.pushButton.setObjectName(u"pushButton")

        self.formLayout_4.setWidget(7, QFormLayout.SpanningRole, self.pushButton)


        self.gridLayout_4.addWidget(self.groupBox, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 305, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Part\u00edcula", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"ID:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Origen en X:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Origen en Y:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Destino X:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Destino Y:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Velocidad", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Color:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Red:", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Green:", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Blue:", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar", None))
    # retranslateUi

