from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem
from PySide2.QtCore import Slot
from ui_mainwindow import Ui_MainWindow
from particulas.admin import Admin
from particulas.particula import Particula
from particulas.algoritmos import distancia_euclidiana

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.admin = Admin()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.agregar_final_pushButton.clicked.connect(self.click_agregar_final)
        self.ui.agregar_inicio_pushButton.clicked.connect(self.click_agregar_inicio)
        self.ui.mostrar_pushButton.clicked.connect(self.click_mostrar)

        self.ui.actionAbrir.triggered.connect(self.action_abrir_archivo)
        self.ui.actionGuardar.triggered.connect(self.action_guardar_archivo)
        self.ui.actionSalir.triggered.connect(self.action_salir)

        self.ui.mostrar_pushButton_tabla.clicked.connect(self.mostrar_tabla)
        self.ui.buscar_pushButton.clicked.connect(self.buscar_id)
    
    @Slot()
    def buscar_id(self):
        self.format_tabla()
        id = self.ui.buscar_lineEdit.text()
        encontrado = False
        for particula in self.admin:
            if id == str(particula.id):
                self.ui.tabla.clear()
                self.ui.tabla.setRowCount(1)
                self.llenar_tabla(particula, 0)
                encontrado = True
                return

        if not encontrado:
            QMessageBox.warning(
                self, 
                "Atención",
                f"La partícula con el ID \"{id}\" no fue encontrada."
            )

    @Slot()
    def mostrar_tabla(self):
        self.format_tabla()
        self.ui.tabla.setRowCount(len(self.admin))
        row = 0
        for particula in self.admin:
            self.llenar_tabla(particula, row)
            row += 1

    def format_tabla(self):
        self.ui.tabla.setColumnCount(10)
        headers = ["ID", "Origen X", "Origen Y", "Destino X", "Destino Y", "Velocidad", "Distancia", "Red", "Green", "Blue"]
        self.ui.tabla.setHorizontalHeaderLabels(headers)

    def llenar_tabla(self, particula, row):
        id_widget = QTableWidgetItem(str(particula.id))
        origen_x_widget = QTableWidgetItem(str(particula.origen_x))
        origen_y_widget = QTableWidgetItem(str(particula.origen_y))
        destino_x_widget = QTableWidgetItem(str(particula.destino_x))
        destino_y_widget = QTableWidgetItem(str(particula.destino_y))
        velocidad_widget = QTableWidgetItem(str(particula.velocidad))
        distancia_widget = QTableWidgetItem(str(particula.distancia))
        red_widget = QTableWidgetItem(str(particula.red))
        green_widget = QTableWidgetItem(str(particula.green))
        blue_widget = QTableWidgetItem(str(particula.blue))

        self.ui.tabla.setItem(row, 0, id_widget)
        self.ui.tabla.setItem(row, 1, origen_x_widget)
        self.ui.tabla.setItem(row, 2, origen_y_widget)
        self.ui.tabla.setItem(row, 3, destino_x_widget)
        self.ui.tabla.setItem(row, 4, destino_y_widget)
        self.ui.tabla.setItem(row, 5, velocidad_widget)
        self.ui.tabla.setItem(row, 6, distancia_widget)
        self.ui.tabla.setItem(row, 7, red_widget)
        self.ui.tabla.setItem(row, 8, green_widget)
        self.ui.tabla.setItem(row, 9, blue_widget)

    
    @Slot()
    def action_abrir_archivo(self):
        # print("abrir_archivo")
        ubicacion = QFileDialog.getOpenFileName(
            self,
            "Abrir archivo",
            '.',
            "JSON (*.json)"
        )[0]
        print(ubicacion)
        if self.admin.abrir(ubicacion):
            QMessageBox.information(
                self,
                "Éxito",
                "Se abrió el archivo " + ubicacion
            )
        else:
            QMessageBox.critical(
                self,
                "Error",
                "Error al abrir el archivo " + ubicacion
            )

    @Slot()
    def action_guardar_archivo(self):
        # print("guardar_archivo")
        ubicacion = QFileDialog.getSaveFileName(
            self,
            "Guardar archivo",
            '.',
            "JSON (*.json)"
        )[0]
        print(ubicacion)
        if self.admin.guardar(ubicacion):
            QMessageBox.information(
                self,
                "Éxito",
                "Se puedo crear el archivo " + ubicacion
            )
        else:
            QMessageBox.critical(
                self,
                "Error",
                "No se pudo crear el archivo " + ubicacion
            )
    
    @Slot()
    def action_salir(self):
        self.close()

    def obtener_datos(self):
        id = self.ui.id_spinBox.value()
        origen_x = self.ui.origen_x_spinBox.value()
        origen_y = self.ui.origen_y_spinBox.value()
        destino_x = self.ui.destino_x_spinBox.value()
        destino_y = self.ui.destino_y_spinBox.value()
        velocidad = self.ui.velocidad_spinBox.value()
        red = self.ui.red_spinBox.value()
        green = self.ui.green_spinBox.value()
        blue = self.ui.blue_spinBox.value()
        
        self.ui.distancia_lineEdit.clear()
        self.ui.distancia_lineEdit.insert(str(distancia_euclidiana(
            origen_x, origen_y, destino_x, destino_y
        )))

        return Particula(
            id, 
            origen_x, origen_y,
            destino_x, destino_y, 
            velocidad,
            red, green, blue
        )


    @Slot()
    def click_agregar_final(self):
        self.admin.agregar_final(self.obtener_datos())
    
    @Slot()
    def click_agregar_inicio(self):
        self.admin.agregar_inicio(self.obtener_datos())

    @Slot()
    def click_mostrar(self):
        self.ui.salida_plainTextEdit.clear()
        self.ui.salida_plainTextEdit.insertPlainText(str(self.admin) + '\n')