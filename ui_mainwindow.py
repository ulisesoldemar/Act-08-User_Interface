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
        MainWindow.resize(800, 825)
        self.actionAbrir = QAction(MainWindow)
        self.actionAbrir.setObjectName(u"actionAbrir")
        self.actionGuardar = QAction(MainWindow)
        self.actionGuardar.setObjectName(u"actionGuardar")
        self.actionSalir = QAction(MainWindow)
        self.actionSalir.setObjectName(u"actionSalir")
        self.actionLista = QAction(MainWindow)
        self.actionLista.setObjectName(u"actionLista")
        self.actionGrafo = QAction(MainWindow)
        self.actionGrafo.setObjectName(u"actionGrafo")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.agregar_inicio_pushButton = QPushButton(self.groupBox)
        self.agregar_inicio_pushButton.setObjectName(u"agregar_inicio_pushButton")

        self.gridLayout.addWidget(self.agregar_inicio_pushButton, 6, 2, 1, 2)

        self.velocidad_spinBox = QSpinBox(self.groupBox)
        self.velocidad_spinBox.setObjectName(u"velocidad_spinBox")
        self.velocidad_spinBox.setMaximum(500)

        self.gridLayout.addWidget(self.velocidad_spinBox, 4, 2, 1, 2)

        self.id_spinBox = QSpinBox(self.groupBox)
        self.id_spinBox.setObjectName(u"id_spinBox")
        self.id_spinBox.setMaximum(999999999)

        self.gridLayout.addWidget(self.id_spinBox, 0, 1, 1, 3)

        self.groupBox_3 = QGroupBox(self.groupBox)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.horizontalLayout = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.groupBox_3)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.origen_x_spinBox = QSpinBox(self.groupBox_3)
        self.origen_x_spinBox.setObjectName(u"origen_x_spinBox")
        self.origen_x_spinBox.setMaximum(500)

        self.horizontalLayout.addWidget(self.origen_x_spinBox)

        self.label_3 = QLabel(self.groupBox_3)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.origen_y_spinBox = QSpinBox(self.groupBox_3)
        self.origen_y_spinBox.setObjectName(u"origen_y_spinBox")
        self.origen_y_spinBox.setMaximum(500)

        self.horizontalLayout.addWidget(self.origen_y_spinBox)


        self.gridLayout.addWidget(self.groupBox_3, 1, 0, 1, 4)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_13 = QLabel(self.groupBox)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout.addWidget(self.label_13, 5, 0, 1, 2)

        self.label_12 = QLabel(self.groupBox)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout.addWidget(self.label_12, 4, 0, 1, 2)

        self.groupBox_5 = QGroupBox(self.groupBox)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_6 = QLabel(self.groupBox_5)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_3.addWidget(self.label_6)

        self.red_spinBox = QSpinBox(self.groupBox_5)
        self.red_spinBox.setObjectName(u"red_spinBox")
        self.red_spinBox.setMaximum(255)

        self.horizontalLayout_3.addWidget(self.red_spinBox)

        self.label_7 = QLabel(self.groupBox_5)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_3.addWidget(self.label_7)

        self.green_spinBox = QSpinBox(self.groupBox_5)
        self.green_spinBox.setObjectName(u"green_spinBox")
        self.green_spinBox.setMaximum(255)

        self.horizontalLayout_3.addWidget(self.green_spinBox)

        self.label_8 = QLabel(self.groupBox_5)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_3.addWidget(self.label_8)

        self.blue_spinBox = QSpinBox(self.groupBox_5)
        self.blue_spinBox.setObjectName(u"blue_spinBox")
        self.blue_spinBox.setMaximum(255)

        self.horizontalLayout_3.addWidget(self.blue_spinBox)


        self.gridLayout.addWidget(self.groupBox_5, 3, 0, 1, 4)

        self.groupBox_4 = QGroupBox(self.groupBox)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_4 = QLabel(self.groupBox_4)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_2.addWidget(self.label_4)

        self.destino_x_spinBox = QSpinBox(self.groupBox_4)
        self.destino_x_spinBox.setObjectName(u"destino_x_spinBox")
        self.destino_x_spinBox.setMaximum(500)

        self.horizontalLayout_2.addWidget(self.destino_x_spinBox)

        self.label_5 = QLabel(self.groupBox_4)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_2.addWidget(self.label_5)

        self.destino_y_spinBox = QSpinBox(self.groupBox_4)
        self.destino_y_spinBox.setObjectName(u"destino_y_spinBox")
        self.destino_y_spinBox.setMaximum(500)

        self.horizontalLayout_2.addWidget(self.destino_y_spinBox)


        self.gridLayout.addWidget(self.groupBox_4, 2, 0, 1, 4)

        self.agregar_final_pushButton = QPushButton(self.groupBox)
        self.agregar_final_pushButton.setObjectName(u"agregar_final_pushButton")

        self.gridLayout.addWidget(self.agregar_final_pushButton, 6, 0, 1, 2)

        self.distancia_lineEdit = QLineEdit(self.groupBox)
        self.distancia_lineEdit.setObjectName(u"distancia_lineEdit")
        self.distancia_lineEdit.setReadOnly(True)

        self.gridLayout.addWidget(self.distancia_lineEdit, 5, 2, 1, 2)


        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 1, 1)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_tabla = QWidget()
        self.tab_tabla.setObjectName(u"tab_tabla")
        self.gridLayout_4 = QGridLayout(self.tab_tabla)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.buscar_lineEdit = QLineEdit(self.tab_tabla)
        self.buscar_lineEdit.setObjectName(u"buscar_lineEdit")

        self.gridLayout_4.addWidget(self.buscar_lineEdit, 1, 0, 1, 1)

        self.tabla = QTableWidget(self.tab_tabla)
        self.tabla.setObjectName(u"tabla")

        self.gridLayout_4.addWidget(self.tabla, 0, 0, 1, 2)

        self.mostrar_tabla_pushButton = QPushButton(self.tab_tabla)
        self.mostrar_tabla_pushButton.setObjectName(u"mostrar_tabla_pushButton")

        self.gridLayout_4.addWidget(self.mostrar_tabla_pushButton, 2, 0, 1, 2)

        self.buscar_pushButton = QPushButton(self.tab_tabla)
        self.buscar_pushButton.setObjectName(u"buscar_pushButton")

        self.gridLayout_4.addWidget(self.buscar_pushButton, 1, 1, 1, 1)

        self.tabWidget.addTab(self.tab_tabla, "")
        self.tab_visualizador = QWidget()
        self.tab_visualizador.setObjectName(u"tab_visualizador")
        self.gridLayout_5 = QGridLayout(self.tab_visualizador)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.graphicsView = QGraphicsView(self.tab_visualizador)
        self.graphicsView.setObjectName(u"graphicsView")

        self.gridLayout_5.addWidget(self.graphicsView, 0, 0, 1, 2)

        self.dibujar_pushButton = QPushButton(self.tab_visualizador)
        self.dibujar_pushButton.setObjectName(u"dibujar_pushButton")

        self.gridLayout_5.addWidget(self.dibujar_pushButton, 1, 0, 1, 1)

        self.limpiar_pushButton = QPushButton(self.tab_visualizador)
        self.limpiar_pushButton.setObjectName(u"limpiar_pushButton")

        self.gridLayout_5.addWidget(self.limpiar_pushButton, 1, 1, 1, 1)

        self.tabWidget.addTab(self.tab_visualizador, "")

        self.gridLayout_3.addWidget(self.tabWidget, 0, 1, 2, 1)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.salida_comboBox = QComboBox(self.groupBox_2)
        self.salida_comboBox.addItem("")
        self.salida_comboBox.addItem("")
        self.salida_comboBox.setObjectName(u"salida_comboBox")

        self.gridLayout_2.addWidget(self.salida_comboBox, 0, 0, 1, 2)

        self.salida_plainTextEdit = QPlainTextEdit(self.groupBox_2)
        self.salida_plainTextEdit.setObjectName(u"salida_plainTextEdit")
        self.salida_plainTextEdit.setReadOnly(True)

        self.gridLayout_2.addWidget(self.salida_plainTextEdit, 1, 0, 1, 2)

        self.ordenar_pushButton = QPushButton(self.groupBox_2)
        self.ordenar_pushButton.setObjectName(u"ordenar_pushButton")

        self.gridLayout_2.addWidget(self.ordenar_pushButton, 2, 0, 1, 1)

        self.ordenar_comboBox = QComboBox(self.groupBox_2)
        self.ordenar_comboBox.addItem("")
        self.ordenar_comboBox.addItem("")
        self.ordenar_comboBox.addItem("")
        self.ordenar_comboBox.setObjectName(u"ordenar_comboBox")

        self.gridLayout_2.addWidget(self.ordenar_comboBox, 2, 1, 1, 1)

        self.mostrar_pushButton = QPushButton(self.groupBox_2)
        self.mostrar_pushButton.setObjectName(u"mostrar_pushButton")

        self.gridLayout_2.addWidget(self.mostrar_pushButton, 3, 0, 1, 2)


        self.gridLayout_3.addWidget(self.groupBox_2, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 25))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menuArchivo.addAction(self.actionAbrir)
        self.menuArchivo.addAction(self.actionGuardar)
        self.menuArchivo.addSeparator()
        self.menuArchivo.addAction(self.actionLista)
        self.menuArchivo.addAction(self.actionGrafo)
        self.menuArchivo.addSeparator()
        self.menuArchivo.addAction(self.actionSalir)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAbrir.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
#if QT_CONFIG(shortcut)
        self.actionAbrir.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionGuardar.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
#if QT_CONFIG(shortcut)
        self.actionGuardar.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionSalir.setText(QCoreApplication.translate("MainWindow", u"Salir", None))
#if QT_CONFIG(shortcut)
        self.actionSalir.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.actionLista.setText(QCoreApplication.translate("MainWindow", u"Lista", None))
#if QT_CONFIG(shortcut)
        self.actionLista.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+L", None))
#endif // QT_CONFIG(shortcut)
        self.actionGrafo.setText(QCoreApplication.translate("MainWindow", u"Grafo", None))
#if QT_CONFIG(shortcut)
        self.actionGrafo.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+G", None))
#endif // QT_CONFIG(shortcut)
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Part\u00edcula", None))
        self.agregar_inicio_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar al inicio", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Origen", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"x:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"y:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"ID:", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Distancia:", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Velocidad:", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Color", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"R:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"G:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"B:", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Destino", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"x:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"y:", None))
        self.agregar_final_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar al final", None))
        self.distancia_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Aqu\u00ed saldr\u00e1 la distancia", None))
        self.buscar_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ingresa el ID de la part\u00edcula", None))
        self.mostrar_tabla_pushButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.buscar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_tabla), QCoreApplication.translate("MainWindow", u"Tabla", None))
        self.dibujar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Dibujar", None))
        self.limpiar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_visualizador), QCoreApplication.translate("MainWindow", u"Visualizador", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Salida", None))
        self.salida_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Lista", None))
        self.salida_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Grafo", None))

        self.ordenar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Ordenar", None))
        self.ordenar_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Por ID", None))
        self.ordenar_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Por distancia", None))
        self.ordenar_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Por velocidad", None))

        self.mostrar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
    # retranslateUi

