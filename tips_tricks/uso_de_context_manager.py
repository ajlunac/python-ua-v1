from contextlib import contextmanager

with open(r'tips_tricks\prueba.txt', 'w') as archivo:
    archivo.write('Hola desde Python')
    
# Esto es equivalente a:
archivo = open(r'tips_tricks\prueba.txt', 'w')
try:
    archivo.write('Hola desde Python con TryCatch')
finally:
    archivo.close()
    
# Esto NO es equivalente:
archivo = open(r'tips_tricks\prueba.txt', 'w')
archivo.write('Hola desde Python sin TryCatch')
# Esto no asegura el cierre del recurso en caso de error.
archivo.close()

# Manejo de context manager en clases:
# 1. Implementado el protocolo con las funciones __enter__ y __exit__
# 2. utilizando la libreria de contextlib

# Veamos la opcion 1:
class ManejoArchivos:
    def __init__(self, nombre):
        self.nombre = nombre
        
    def __enter__(self):
        self.archivo = open(self.nombre, 'w')
        return self.archivo
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.archivo:
            self.archivo.close()
    
# Este método es un generador, en primer lugar adquiere el recurso
# posteriormente suspende temporalmente la ejecución al utilizar la palabra yield
# cuando de ser utilizado este método, regresa a la ejecución y cierra el recurso.
@contextmanager
def manejador_archivos(nombre):
    try:
        archivo = open(nombre, 'w')
        yield archivo
    finally:
        archivo.close()
    
# Ejercicio de Identador.
class Identador():
    def __init__(self):
        self.nivel = 0
        
    def __enter__(self):
        self.nivel += 1
        return self
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.nivel -= 1
        
    def imprimir(self, texto):
        print('    ' * self.nivel + texto)

    
if __name__ == '__main__':
    # Prueba implementando el protocolo de context manager
    with ManejoArchivos(r'tips_tricks\prueba.txt') as archivo:
        archivo.write('Hola desde la clase ManejoArchivos')
        
    # Prueba utilizando la libreria contextlib
    with manejador_archivos(r'tips_tricks\prueba.txt') as archivo:
        archivo.write('Hola desde el decorador contextmanager')
        archivo.write('\nadios')
        
    # Prueba de identador
    with Identador() as identador:
        identador.imprimir('primer nivel')
        with identador:
            identador.imprimir('segundo nivel')
            identador.imprimir('continua segundo nivel...')
            with identador:
                identador.imprimir('tercer nivel')
                identador.imprimir('continua tercer nivel...')
            identador.imprimir('fin segundo nivel')
        identador.imprimir('fin primer nivel')