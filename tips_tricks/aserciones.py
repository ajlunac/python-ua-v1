# Tip. Las aserciones nos pueden ayudar a depurar nustros programas de errores.
# que no podamos recuperar.

# Ejemplo 1. Revisamos si la división es entre 0:
def dividir(a, b):
    # Nos aseguramos que el valor de b no es cero para poder continuar.
    assert b!= 0, 'División entre cero'
    print(f'Resultado de la división: {a/b}')

# Ejemplo 2. Realizamos el calculo del promedio de una lista de calificaciones:
def obtener_promedio(calificaciones):
    # Si la lista de calificaciones está vacía, no debería continuar el programa.
    assert len(calificaciones) != 0, 'Lista de calificaciones vacía'
    print(f'El promedio de calificaciones es: {sum(calificaciones)/len(calificaciones)}')
    
# Ejemplo 3. Realizamos un descuento al producto proporcionado:
def aplicar_descuento(productos, descuento):
    precio_con_descuento = productos['precio'] * (1.0-descuento)
    print(f'Nuevo precio con descuento: {precio_con_descuento:0.2f}')
    assert 0 <= precio_con_descuento <= productos['precio'], 'Descuento invalido {precio_con_descuento:0.2f}'
    print(f'Descuento valido...')

if __name__ == '__main__':
    # Prueba Ejemlo 1. División entre 0:
    dividir(10, 5)
    
    # Prueba Ejemlo 2. Calculo promedio de calificaciones:
    calificaciones = [10,8,7,9]
    # calificaciones = []
    obtener_promedio(calificaciones)
    
    # Prueba Ejemlo 3. Aplicar descuento al producto:
    productos = {'nombre': 'Laptop', 'precio': 1000}
    aplicar_descuento(productos, 0.10)
    