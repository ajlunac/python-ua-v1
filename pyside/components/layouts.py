import sys
from PySide6.QtGui import QColor, QPalette
from PySide6.QtWidgets import QWidget, QMainWindow, QApplication, QVBoxLayout, QHBoxLayout, QGridLayout, QStackedLayout, QPushButton, QTabWidget

class Color(QWidget):
    def __init__(self, nuevo_color):
        super().__init__()
        # Indicamos que se puede agregar un color de fondo.
        self.setAutoFillBackground(True)
        paletaColores = self.palette()
        # Creamos el componente de color de fondo aplicando el nuevo color.
        paletaColores.setColor(QPalette.Window, QColor(nuevo_color))
        # Aplicamos el nuevo color al componente.
        self.setPalette(paletaColores)
        
class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        # self.setWindowTitle('Layouts en PySide6')
        
        # # Layout vertical.
        # layout = QVBoxLayout()
        # # Agregamos un nuevo componente de color.
        # layout.addWidget(Color('red'))
        # layout.addWidget(Color('green'))
        # layout.addWidget(Color('blue'))
        
        # ----------------------------------------------------------------------------------------------------------------
        
        # Layout horizontal.
        # layout = QHBoxLayout()
        # # Agregamos un nuevo componente de color.
        # layout.addWidget(Color('red'))
        # layout.addWidget(Color('green'))
        # layout.addWidget(Color('blue'))
                
        # ----------------------------------------------------------------------------------------------------------------
        
        # # Anidar Layouts (Layout dentro de otro Layout).
        # # Creamos en primer lugar el layout horizontal y después el vertical.
        # layout_horizontal = QHBoxLayout()
        # # Agregamos espacio al margen del layout_horizontal.
        # layout_horizontal.setContentsMargins(10, 10, 10, 10)
        # # Agregams un espacio entre cada elemento del layout_horizontal.
        # layout_horizontal.setSpacing(30)
        # # Agregamos algunos widgets al layout_horizontal.
        # layout_vertical = QVBoxLayout()
        # # Agregamos espacio en el layout_vertical.
        # layout_vertical.setContentsMargins(5, 10, 5, 10)
        # # Agregamos un espacio dentro de cada elemento del laytout_vertical.
        # layout_vertical.setSpacing(20)
        # # Agregamos algunos widgets al layout_vertical.
        # layout_vertical.addWidget(Color('red'))
        # layout_vertical.addWidget(Color('green'))
        # layout_vertical.addWidget(Color('blue'))
        # # Agregamnos el layput_vertical dentro del layout_horizontal.
        # # Es decir, se agraga de manera anidada, un layout dentro de otro layout.
        # layout_horizontal.addLayout(layout_vertical)
        # # Agregamos más elementos al layout_horizontal.
        # layout_horizontal.addWidget(Color('yellow'))
        # layout_horizontal.addWidget(Color('purple'))        
        
        # ----------------------------------------------------------------------------------------------------------------
        
        # # Layout con Grid.
        # layout = QGridLayout()
        # layout.addWidget(Color('red'), 0, 0)
        # layout.addWidget(Color('blue'), 0, 2)
        # layout.addWidget(Color('green'), 1, 1)
        # layout.addWidget(Color('yellow'), 1, 0)
        # layout.addWidget(Color('purple'), 1, 2)
        
        # ----------------------------------------------------------------------------------------------------------------
        
        # # Layout QStackedLayout.
        # layout = QStackedLayout()
        # # Por default solo se visualiza el primer widget agregado.
        # layout.addWidget(Color('red'))
        # layout.addWidget(Color('green'))
        # layout.addWidget(Color('yellow'))
        # layout.setCurrentIndex(2) # Cambiamos el widget actual al segundo.
        
        # ----------------------------------------------------------------------------------------------------------------
        
    #     # Creamos los layouts.
    #     layout_principal = QVBoxLayout()
    #     layout_botones = QHBoxLayout()
    #     self.layout_tipo_stack = QStackedLayout()
    #     # Agregamos los layouts hijos al layout principal.
    #     layout_principal.addLayout(layout_botones)
    #     layout_principal.addLayout(self.layout_tipo_stack)
        
    #     # Creamos los botones.
    #     boton_rojo = QPushButton('Rojo')
    #     # Publicamos este botón en el layout de botones.
    #     layout_botones.addWidget(boton_rojo)
    #     # publicamos el color rojo al layout de tipo stack.
    #     self.layout_tipo_stack.addWidget(Color('red')) # Indice 0.
    #     # Conectamos el evento pressed del botón respectivo.
    #     boton_rojo.pressed.connect(lambda: self.activar_tabulador(0))
        
    #     # Creamos el botón azul.
    #     boton_azul = QPushButton('Azul')
    #     layout_botones.addWidget(boton_azul)
    #     self.layout_tipo_stack.addWidget(Color('blue')) # Indice 1.
    #     boton_azul.pressed.connect(lambda: self.activar_tabulador(1))
        
    #     # Creamos el botón amarillo.
    #     boton_amarillo = QPushButton('Amarillo')
    #     layout_botones.addWidget(boton_amarillo)
    #     self.layout_tipo_stack.addWidget(Color('yellow')) # Indice 2.
    #     boton_amarillo.pressed.connect(lambda: self.activar_tabulador(2))
               
    #     # Creamos un componente generico para poder publicar el layout.
    #     componente = QWidget()
    #     componente.setLayout(layout_principal)
    #     self.setCentralWidget(componente)
        
    # def activar_tabulador(self, indice):
    #     self.layout_tipo_stack.setCurrentIndex(indice)
    #     print(f'Indice seleccionado: {indice}')
        
    # ----------------------------------------------------------------------------------------------------------------
    
        self.setWindowTitle('Tabulador en PySide6')
        
        # Creamos el componente de tab.
        tabuladro = QTabWidget()
        # Posición de las etiquetas del tabulador.
        tabuladro.setTabPosition(QTabWidget.North)
        # Indicamos si queremos que se muevan las etiquetas del tabulador.
        tabuladro.setMovable(True)
        # Para que se vea similar en MacOs.
        tabuladro.setDocumentMode(True)
        
        # Agragamos los colores a cada tabulador.
        tabuladro.addTab(Color('red'), 'Rojo')
        tabuladro.addTab(Color('yellow'), 'Amarillo')
        tabuladro.addTab(Color('green'), 'Verde')
        
        
        self.setCentralWidget(tabuladro)
        
        
if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()
    
    