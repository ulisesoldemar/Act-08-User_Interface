from PySide2.QtCore import Slot
from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem, QGraphicsScene
from PySide2.QtGui import QPen, QColor, QTransform
from ui_mainwindow import Ui_MainWindow
from pprint import pprint, pformat
from particulas.admin import Admin
from particulas.particula import Particula
from particulas.algoritmos import distancia_euclidiana

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.admin = Admin()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.agregar_final_pushButton.clicked.connect(lambda: self.admin.agregar_final(self.obtener_datos()))
        self.ui.agregar_inicio_pushButton.clicked.connect(lambda: self.admin.agregar_inicio(self.obtener_datos()))
        self.ui.mostrar_pushButton.clicked.connect(self.click_mostrar)

        self.ui.actionAbrir.triggered.connect(self.action_abrir_archivo)
        self.ui.actionGuardar.triggered.connect(self.action_guardar_archivo)
        self.ui.actionSalir.triggered.connect(lambda: self.close())

        self.ui.actionLista.triggered.connect(lambda: self.ui.salida_comboBox.setCurrentIndex(0))
        self.ui.actionGrafo.triggered.connect(lambda: self.ui.salida_comboBox.setCurrentIndex(1))

        self.ui.actionRecorrido.triggered.connect(self.recorrido)

        self.ui.mostrar_tabla_pushButton.clicked.connect(self.mostrar_tabla)
        self.ui.buscar_pushButton.clicked.connect(self.buscar_id)
        
        self.ui.dibujar_pushButton.clicked.connect(self.dibujar)
        self.ui.limpiar_pushButton.clicked.connect(self.limpiar)

        self.scene = QGraphicsScene()
        self.ui.graphicsView.setScene(self.scene)

        self.ui.ordenar_pushButton.clicked.connect(self.ordenar)
    

    @Slot()
    def recorrido(self):
        origen = (self.ui.origen_x_spinBox.value(), self.ui.origen_y_spinBox.value())
        self.admin.grafo()
        self.ui.salida_comboBox.setCurrentIndex(1)
        dfs, bfs = self.admin.dfs(origen), self.admin.bfs(origen)
        if dfs and bfs:
            self.ui.salida_plainTextEdit.setPlainText("Profundidad:" + '\n' + dfs + '\n' + "Amplitud:" + '\n' + bfs)
        else:
            QMessageBox.critical (
                self,
                "Error",
                "No es posible establecer esa ruta."
            )

    @Slot()
    def ordenar(self):
        print("Ordenar")
        # Por ID (ascendente)
        if self.ui.ordenar_comboBox.currentIndex() == 0:
            self.admin.ordenar(lambda Particula: Particula.id)
        # Por distancia (descendente)
        elif self.ui.ordenar_comboBox.currentIndex() == 1:
            self.admin.ordenar(lambda Particula: Particula.distancia, True)
        # Por velocidad (ascendente)
        elif self.ui.ordenar_comboBox.currentIndex() == 2:
            self.admin.ordenar(lambda Particula: Particula.velocidad)
        
        QMessageBox.information (
            self,
            "Éxito",
            "Se ordenaron las partículas " + self.ui.ordenar_comboBox.currentText().lower()
        )
        
        
    def wheelEvent(self, event):
        if event.delta() > 0:
            self.ui.graphicsView.scale(1.2, 1.2)
        else:
            self.ui.graphicsView.scale(0.8, 0.8)

    @Slot()
    def dibujar(self):
        print("Dibujar")
        
        pen = QPen()
        pen.setWidth(2)

        for particula in self.admin:
            
            color = QColor(particula.red, particula.green, particula.blue)
            pen.setColor(color)

            origen_x = particula.origen_x
            origen_y = particula.origen_y
            destino_x = particula.destino_x
            destino_y = particula.destino_y

            self.scene.addEllipse(origen_x, origen_y, 6, 6, pen)
            self.scene.addEllipse(destino_x, destino_y, 6, 6, pen)
            self.scene.addLine(origen_x + 3, origen_y + 3, destino_x + 3, destino_y + 3, pen)

            origen = self.scene.addText('(' + str(origen_x) + ', ' + str(origen_y) + ')')
            origen.setPos(origen_x, origen_y)
            destino = self.scene.addText('(' + str(destino_x) + ', ' + str(destino_y) + ')')
            destino.setPos(destino_x, destino_y)

    @Slot()
    def limpiar(self):
        print("Limpiar")
        self.scene.clear()
        self.ui.graphicsView.setTransform(QTransform())

    @Slot()
    def buscar_id(self):
        id = self.ui.buscar_lineEdit.text()
        encontrado = False
        for particula in self.admin:
            if id == str(particula.id):
                self.ui.tabla.clear()
                self.format_tabla()
                self.ui.tabla.setRowCount(1)
                self.llenar_tabla(particula, 0)
                encontrado = True
                return

        if not encontrado:
            self.format_tabla()
            QMessageBox.warning (
                self, 
                "Atención",
                f"La partícula con el ID \"{id}\" no fue encontrada."
            )

    @Slot()
    def mostrar_tabla(self):
        self.format_tabla()
        total = len(self.admin)
        self.ui.tabla.setRowCount(total)
        for row in range(total):
            self.llenar_tabla(self.admin[row], row)

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
        ubicacion = QFileDialog.getOpenFileName (
            self,
            "Abrir archivo",
            '.',
            "JSON (*.json)"
        )[0]
        print(ubicacion)
        if self.admin.abrir(ubicacion):
            QMessageBox.information (
                self,
                "Éxito",
                "Se abrió el archivo " + ubicacion
            )
        else:
            QMessageBox.critical (
                self,
                "Error",
                "Error al abrir el archivo " + ubicacion
            )

    @Slot()
    def action_guardar_archivo(self):
        # print("guardar_archivo")
        ubicacion = QFileDialog.getSaveFileName (
            self,
            "Guardar archivo",
            '.',
            "JSON (*.json)"
        )[0]
        print(ubicacion)
        if self.admin.guardar(ubicacion):
            QMessageBox.information (
                self,
                "Éxito",
                "Se puedo crear el archivo " + ubicacion
            )
        else:
            QMessageBox.critical (
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

        return Particula (
            id, 
            origen_x, origen_y,
            destino_x, destino_y, 
            velocidad,
            red, green, blue
        )

    @Slot()
    def click_mostrar(self):
        self.ui.salida_plainTextEdit.clear()
        if self.ui.salida_comboBox.currentIndex() == 0:
            self.ui.salida_plainTextEdit.insertPlainText(str(self.admin) + '\n')
        elif self.ui.salida_comboBox.currentIndex() == 1:
            salida = pformat(self.admin.grafo(), width=40, indent=1)
            self.ui.salida_plainTextEdit.insertPlainText(str(salida))
            pprint(salida)