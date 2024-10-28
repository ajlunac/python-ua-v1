# Sinals y slots
import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QMainWindow, QLabel, QApplication, QCheckBox

class Componentes(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Componentes')
        self.setFixedSize(300, 150)
        
        # # Componenente de tipo Label.
        # etiqueta = QLabel('Hola')
        # # Modificar el valor incial.
        # etiqueta.setText('Saludos')
        # # Modificar la fuente.
        # fuente = etiqueta.font()
        # fuente.setPointSize(25)
        # etiqueta.setFont(fuente)
        # # Mofidicar la alineación de la etiqueta.
        # # etiqueta.setAlignment(Qt.AlignCenter)
        # # Deferentes valores de setAlignment: Qt.AlignLeft, Qt.AlignRight, Qt.AlignHCenter, Qt.AlignJustify, Qt.AlignTop, Qt.AlignBottom, Qt.AlignVCenter
        # etiqueta.setAlignment(Qt.AlignHCenter | Qt.AlignLeft)
        
        # Componenente de tipo Label con imagen.
        etiqueta = QLabel('Hola')
        etiqueta.setPixmap(QPixmap(r'resources/img/python-logo.png'))
        etiqueta.setScaledContents(True)
        
        # Publicamos el componente.
        self.setCentralWidget(etiqueta)

        
if __name__ == '__main__':
    app = QApplication([])
    ventana = Componentes()
    ventana.show()
    sys.exit(app.exec())