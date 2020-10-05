import sys
from PySide2.QtWidgets import QPushButton, QApplication
from mainwindow import MainWindow

# Aplicación de Qt
app = QApplication()
window = MainWindow()
window.show()

# Qt loop
sys.exit(app.exec_())
