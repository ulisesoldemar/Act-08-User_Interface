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
        MainWindow.resize(572, 534)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_5 = QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_3 = QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_3.addWidget(self.label_3, 2, 0, 1, 1)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_3.addWidget(self.label_5, 4, 0, 1, 1)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_3.addWidget(self.label_7, 6, 0, 1, 1)

        self.velocidad_spinBox = QSpinBox(self.groupBox)
        self.velocidad_spinBox.setObjectName(u"velocidad_spinBox")
        self.velocidad_spinBox.setMaximum(500)

        self.gridLayout_3.addWidget(self.velocidad_spinBox, 5, 1, 1, 1)

        self.id_spinBox = QSpinBox(self.groupBox)
        self.id_spinBox.setObjectName(u"id_spinBox")
        self.id_spinBox.setMaximum(999999999)

        self.gridLayout_3.addWidget(self.id_spinBox, 0, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_3.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_3.addWidget(self.label_6, 5, 0, 1, 1)

        self.destino_y_spinBox = QSpinBox(self.groupBox)
        self.destino_y_spinBox.setObjectName(u"destino_y_spinBox")
        self.destino_y_spinBox.setMaximum(500)

        self.gridLayout_3.addWidget(self.destino_y_spinBox, 4, 1, 1, 1)

        self.origen_y_spinBox = QSpinBox(self.groupBox)
        self.origen_y_spinBox.setObjectName(u"origen_y_spinBox")
        self.origen_y_spinBox.setMaximum(500)

        self.gridLayout_3.addWidget(self.origen_y_spinBox, 2, 1, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_3.addWidget(self.label_4, 3, 0, 1, 1)

        self.origen_x_spinBox = QSpinBox(self.groupBox)
        self.origen_x_spinBox.setObjectName(u"origen_x_spinBox")
        self.origen_x_spinBox.setMaximum(500)

        self.gridLayout_3.addWidget(self.origen_x_spinBox, 1, 1, 1, 1)

        self.destino_x_spinBox = QSpinBox(self.groupBox)
        self.destino_x_spinBox.setObjectName(u"destino_x_spinBox")
        self.destino_x_spinBox.setMaximum(500)

        self.gridLayout_3.addWidget(self.destino_x_spinBox, 3, 1, 1, 1)

        self.distancia_lineEdit = QLineEdit(self.groupBox)
        self.distancia_lineEdit.setObjectName(u"distancia_lineEdit")
        self.distancia_lineEdit.setReadOnly(True)

        self.gridLayout_3.addWidget(self.distancia_lineEdit, 6, 1, 1, 1)

        self.color_groupBox = QGroupBox(self.groupBox)
        self.color_groupBox.setObjectName(u"color_groupBox")
        self.gridLayout_4 = QGridLayout(self.color_groupBox)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_8 = QLabel(self.color_groupBox)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_4.addWidget(self.label_8, 0, 0, 1, 1)

        self.label_10 = QLabel(self.color_groupBox)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_4.addWidget(self.label_10, 2, 0, 1, 1)

        self.label_9 = QLabel(self.color_groupBox)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_4.addWidget(self.label_9, 1, 0, 1, 1)

        self.red_spinBox = QSpinBox(self.color_groupBox)
        self.red_spinBox.setObjectName(u"red_spinBox")
        self.red_spinBox.setMaximum(255)

        self.gridLayout_4.addWidget(self.red_spinBox, 0, 1, 1, 1)

        self.green_spinBox = QSpinBox(self.color_groupBox)
        self.green_spinBox.setObjectName(u"green_spinBox")
        self.green_spinBox.setMaximum(255)

        self.gridLayout_4.addWidget(self.green_spinBox, 1, 1, 1, 1)

        self.blue_spinBox = QSpinBox(self.color_groupBox)
        self.blue_spinBox.setObjectName(u"blue_spinBox")
        self.blue_spinBox.setMaximum(255)

        self.gridLayout_4.addWidget(self.blue_spinBox, 2, 1, 1, 1)


        self.gridLayout_3.addWidget(self.color_groupBox, 7, 0, 1, 2)


        self.gridLayout_5.addWidget(self.groupBox, 0, 0, 1, 1)

        self.salida_plainTextEdit = QPlainTextEdit(self.centralwidget)
        self.salida_plainTextEdit.setObjectName(u"salida_plainTextEdit")
        self.salida_plainTextEdit.setReadOnly(True)

        self.gridLayout_5.addWidget(self.salida_plainTextEdit, 0, 1, 1, 1)

        self.agregar_final_pushButton = QPushButton(self.centralwidget)
        self.agregar_final_pushButton.setObjectName(u"agregar_final_pushButton")

        self.gridLayout_5.addWidget(self.agregar_final_pushButton, 1, 0, 1, 2)

        self.agregar_inicio_pushButton = QPushButton(self.centralwidget)
        self.agregar_inicio_pushButton.setObjectName(u"agregar_inicio_pushButton")

        self.gridLayout_5.addWidget(self.agregar_inicio_pushButton, 2, 0, 1, 2)

        self.mostrar_pushButton = QPushButton(self.centralwidget)
        self.mostrar_pushButton.setObjectName(u"mostrar_pushButton")

        self.gridLayout_5.addWidget(self.mostrar_pushButton, 3, 0, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Part\u00edculas", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Part\u00edcula", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"ID:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Origen Y:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Destino Y:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Distancia:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Origen X:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Velocidad:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Destino X:", None))
        self.color_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Color", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Red:", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Blue:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Green:", None))
        self.agregar_final_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar al final", None))
        self.agregar_inicio_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar al inicio", None))
        self.mostrar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
    # retranslateUi

