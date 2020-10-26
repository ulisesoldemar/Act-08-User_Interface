from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox
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