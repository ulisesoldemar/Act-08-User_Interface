from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import Slot
from ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        # Incializa el constructor con el constructor
        # de la clase padre
        super(MainWindow, self).__init__()
        # Objeto de la "vista"
        ui = Ui_MainWindow()
        # Dónde se incrusta la "vista", self indica
        # que en esta misma clase
        ui.setupUi(self)
        # Push Button se conecta a la función click
        ui.pushButton.clicked.connect(self.click_agregar)
    
    # Definir un "slot", es parecido a un evento
    @Slot() # Decorador
    def click_agregar(self):
        print ("Agregar")
