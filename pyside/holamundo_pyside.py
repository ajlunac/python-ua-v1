import sys
from PySide6.QtWidgets import QApplication, QMainWindow

# Clase base de Qt (PySide).
# Se encarga de procesar los evenytos (event loop).
app = QApplication()
# Crear un objeto ventana.
# Cuañlquier componenete puede ser una ventana en PySide.
# ventana = QPushButton('Botón de PySide')
ventana = QMainWindow()
# Titulo de la ventana.
ventana.setWindowTitle('Hola mundo con PySid')
# Tamaña de la ventana.
ventana.resize(600, 400)
# Mostrar la ventana.
ventana.show()
# Se ejecuta la aplicación.
sys.exit(app.exec())