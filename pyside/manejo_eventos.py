# Sinals y slots
import sys
from PySide6.QtWidgets import QMainWindow, QPushButton, QApplication, QLabel, QLineEdit, QVBoxLayout, QWidget

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Sinals y Slots')
        self.setFixedSize(400, 200)
        # Definimos la etiqueta y línea de edición.
        self.etiqueta = QLabel()
        self.entrada_texto = QLineEdit()
        # Conectar el wiget de entrada_texto con la etiqueta.
        self.entrada_texto.textChanged.connect(self.etiqueta.setText)
        # Publicamos los comopnentes usando un layout.
        layout = QVBoxLayout()
        layout.addWidget(self.entrada_texto)
        layout.addWidget(self.etiqueta)
        # Crear un contenedor para el layout.
        contenedor = QWidget()
        contenedor.setLayout(layout)
        # Publicamos el contendor, el cual incluye los demás elementos.
        self.setCentralWidget(contenedor)
        
if __name__ == '__main__':
    # Creamnos el objeto de la aplicación.
    app = QApplication([])
    # Creamos una instancia de nuestra clase.
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())