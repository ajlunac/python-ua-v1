from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton, QDialog, QDialogButtonBox, QVBoxLayout, QLabel, QMessageBox

class VentanaDialogo(QDialog):
    def __init__(self, padre=None):
        super().__init__(padre)
        self.setWindowTitle('Ventana de Dialogo')   
        # Agregamos un botón de aceptar y otro de cancelar.
        botones = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        self.botones_dialogo = QDialogButtonBox(botones)
        self.botones_dialogo.accepted.connect(self.accept)
        self.botones_dialogo.rejected.connect(self.reject)
        
        # Creamos un layaout para publicar los botones.
        self.layout = QVBoxLayout()
        mensaje = QLabel('Presiona alguno de los botones')
        self.layout.addWidget(mensaje)
        self.layout.addWidget(self.botones_dialogo)
        self.setLayout(self.layout)
 
class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Dialogos')
        # Agragamos un botón
        boton = QPushButton('Mostrar Dialogo')
        boton.clicked.connect(self.click_boton)
        
        # Publicamos el botón
        self.setCentralWidget(boton)
        
    # def click_boton(self, s):
    #     print(f'Click sobre botón {s}')
    #     # Creamos un dialogo
    #     dialogo = QMessageBox(self)
    #     dialogo.setWindowTitle('Dialogo Simple')
    #     dialogo.setText('Ventana de dialogo simple')
    #     valor_retornado = dialogo.exec()
    #     # Imprimimos el valor de retorno
    #     print(f'Valor de retorno: {valor_retornado}')
    #     if valor_retornado == QMessageBox.Ok:
    #         print('Regreso el valor Ok')
    #     else:
    #         print('Regreso el valor distinto de Ok')
    
    # def click_boton(self, s):
    #     print(f'Click sobre botón {s}')
    #     # Creamos un dialogo
    #     dialogo = QMessageBox(self)
    #     dialogo.setWindowTitle('Dialogo con pregunta')
    #     dialogo.setText('Ventana de dialogo con pregunta')
    #     # Agregamos los botones de las respuestas a la pregunta.
    #     dialogo.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    #     # Agregamos un icono a la ventana de dialogo.
    #     dialogo.setIcon(QMessageBox.Question)
    #     valor_retornado = dialogo.exec()
    #     # Imprimimos el valor de retorno
    #     print(f'Valor de retorno: {valor_retornado}')
    #     if valor_retornado == QMessageBox.Yes:
    #         print('Regreso el valor Yes (si)')
    #     else:
    #         print('Regreso el valor de No')
    
    # def click_boton(self, s):
    #     print(f'Click sobre botón {s}')
    #     # Creamos un dialogo
    #     dialogo = QMessageBox.question(self, 'Dialogo con pregunta', '¿Estás seguro de que quieres salir?')
    #     if dialogo == QMessageBox.Yes:
    #         print('Regreso el valor Yes (si)')
    #     else:
    #         print('Regreso el valor de No')
    
    def click_boton(self, s):
        print(f'Click sobre botón {s}')
        # Creamos un dialogo personalizada
        dialogo = QMessageBox.critical(self, 'Probrma Crítico', 'Ventana con problema crítico.', 
                                       buttons=QMessageBox.Discard | QMessageBox.NoToAll | QMessageBox.Ignore, defaultButton=QMessageBox.Discard)
        
        # Revisamos cual botón se presionó        
        if dialogo == QMessageBox.Discard:
            print('Regreso el valor Discard (Descartar)')
        elif dialogo == QMessageBox.NoToAll:
            print('Regreso el valor de NoToAll (No para todos)')
        else:
            print('Regreso el valor Ignore (Ignorar)')
        
if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()
    
    