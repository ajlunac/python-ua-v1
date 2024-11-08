from PySide6.QtGui import QAction, QIcon, QKeySequence
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
        
        # Menú de la ventana.
        menu = self.menuBar()
        menu_archivo = menu.addMenu('&Archivo')
        menu_archivo.addAction(boton_nuevo)
        
        # Agregamos una segunda opción.
        menu_archivo.addAction(boton_guardar)
        
        # Agregamos un separador.
        menu_archivo.addSeparator()
        
        # Agregamos una tercera opción.
        boton_salir = QAction('Salir', self)
        menu_archivo.addAction(boton_salir)
        
        # Submenu ayuda.
        menu_ayuda = menu.addMenu('&Ayuda')
        menu_ayuda.addAction(boton_acercade)
        
        # Agregamos un submenu.
        menu_archivo.addMenu(menu_ayuda)
        
        # Creación de atajos para nuestro menú.
        # Ej. Combinación de teclas.
        # boton_nuevo.setShortcut(QKeySequence('Ctrl+N'))
        boton_nuevo.setShortcut(Qt.CTRL | Qt.Key_N)
        # Atajo acerca de - Ctrl | 1
        boton_acercade.setShortcut(Qt.CTRL | Qt.Key_1)
        # Atajo guardar - Ctrl | G
        boton_guardar.setShortcut(Qt.CTRL | Qt.Key_G)

        
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
    
    