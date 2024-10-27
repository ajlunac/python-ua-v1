import sys
from PySide6.QtCore import QSize
from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton
from PySide6.QtGui import QAction


class VentanaPySide(QMainWindow):
    def __init__(self):
        # Llamamos el método init de la clase padre.
        super().__init__()
        self.setWindowTitle('POO con PySide')
        # self.resize(600, 400)
        # Valores de ancho y alto fijo
        self.setFixedSize(QSize(600, 400))
        # Algunos componentes de la ventana.
        self._agregar_componentes()
        
    def _agregar_componentes(self):
        # Menú
        menu = self.menuBar()
        menu_archivo = menu.addMenu('Archivo')
        # Opciones del menú
        accion_nuevo = QAction('Nuevo', self)
        menu_archivo.addAction(accion_nuevo)
        # Texto a la barra de estado
        accion_nuevo.setStatusTip('Nuevo archivo')
        # Mensaje en la barra de estado
        self.statusBar().showMessage('Infomración de la barra de estado...')
        # Botón
        boton = QPushButton('Nuevo Botón')
        # Publicamos el botón en la ventana.
        self.setCentralWidget(boton)



if __name__ == '__main__':
    app = QApplication([])
    # Creamos el objeto de tipo ventana.
    ventana = VentanaPySide()
    ventana.show()
    # Ejecutamos la ventana.
    sys.exit(app.exec())
        