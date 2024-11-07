from PySide6.QtGui import QAction, QIcon
from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import QMainWindow, QApplication, QLabel, QToolBar, QStatusBar, QCheckBox
 
class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Barra de Herramientas')
        # Publicamos una etiqueta.
        etiqueta = QLabel('Hola Mundo!')
        etiqueta.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(etiqueta)
        
        # Creamos la barra de herramientas.
        barra = QToolBar('Mi barra de herramientas')
        barra.setIconSize(QSize(16, 16))
        # Configuración para mostrar en la barra de herramientas.
        # barra.setToolButtonStyle(Qt.ToolButtonFollowStyle)
        # barra.setToolButtonStyle(Qt.ToolButtonTextOnly)
        # barra.setToolButtonStyle(Qt.ToolButtonIconOnly)
        # barra.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        # barra.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.addToolBar(barra)
        
        # Agregamos los elementos a nuestra barra de herramientas.
        boton_nuevo = QAction(QIcon(r'resources\img\nuevo.png'), 'Nuevo', self)
        boton_guardar = QAction(QIcon(r'resources\img\guardar.png'), 'Guardar', self)
        boton_acercade = QAction(QIcon(r'resources\img\acerca.png'), 'Acerca de...', self)
        
        # Agregamos el botón a la barra.
        barra.addAction(boton_nuevo)
        barra.addAction(boton_guardar)
        barra.addAction(boton_acercade)
        
        # Barra de estado.
        self.setStatusBar(QStatusBar(self))
        
        # Mostrar mensaje del botón de acción.
        boton_nuevo.setStatusTip('Nuevo archivo')
        boton_guardar.setStatusTip('Guardar archivo')
        boton_acercade.setStatusTip('Acerca de este programa')
        
        # Asociamos el evento click.
        boton_nuevo.triggered.connect(self.click_boton_nuevo)
        boton_guardar.triggered.connect(self.click_boton_guardar)
        boton_acercade.triggered.connect(self.click_boton_acercade)
        
        # Hacemos checable el botón.
        # boton_nuevo.setCheckable(True)
        
        barra.addSeparator()
        
        barra.addWidget(QCheckBox('Checkbox'))
        barra.addWidget(QLabel('Salir'))

        
    def click_boton_nuevo(self, s):
        print(f'Nuevo archivo {s}.')
        
    def click_boton_guardar(self, s):
        print(f'Guardar archivo {s}.')
        
    def click_boton_acercade(self, s):
        print(f'Acerca de {s}.')
        
if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()
    
    