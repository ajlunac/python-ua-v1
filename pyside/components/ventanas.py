from random import randint
from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit

class NuevaVentana(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Ventana Nueva')
        layout = QVBoxLayout()
        self.etiqueta = QLabel(f'Nueva ventana: {randint(1, 100)}')
        layout.addWidget(self.etiqueta)
        self.setLayout(layout)

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.nueva_ventana = NuevaVentana()
        self.setWindowTitle('Ventanas')
        self.boton = QPushButton('Mostrar/Ocultar nueva ventana')
        self.boton.clicked.connect(self.mostrar_nueva_ventana)
        # Definimos una entrada de texto.
        self.entrada_texto = QLineEdit()
        self.entrada_texto.textChanged.connect(self.nueva_ventana.etiqueta.setText)
        #  Layout.
        layout = QVBoxLayout()
        layout.addWidget(self.boton)
        layout.addWidget(self.entrada_texto)
        contenedor = QWidget()
        contenedor.setLayout(layout)
        self.setCentralWidget(contenedor)
        
    def mostrar_nueva_ventana(self, estado):
        if self.nueva_ventana.isVisible():
            self.nueva_ventana.hide()
        else:
            self.nueva_ventana.show()
        
if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()
    
    