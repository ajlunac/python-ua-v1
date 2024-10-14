# Importando el módulo tkinter.
import tkinter as tk
# Importamos el módulo del tema tkinter.
from tkinter import ttk

# Instanciamos la ventana con la librería tkinter.
ventana = tk.Tk()
# Damos título a la ventana.
ventana.title("Hola Mundo")
# Asignamos un tamaño a la ventana de 600x400 pixeles (ancho x alto).
ventana.geometry("600x400")
# Configuramos el icono de la ventana.
ventana.iconbitmap(r"img\icono.ico")
# Configurar el grid layout manager para la ventana.
ventana.rowconfigure(0, weight=2)
ventana.rowconfigure(1, weight=10)
ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=5)

"""
# Creamos el método evento_click que se ejecutará cuando se pulse el botón.
def evento_click():
    # Se cambia el texto del botón al presionarlo.
    boton1.config(text="Botón presionado")
    print("Ejecución del evento_click")
    # Creams un nuevo botón y lo mostramos en la ventana.
    boton2 = ttk.Button(ventana, text="Nuevo Botón")
    boton2.pack()

# Creamos botón o widget con la librería tkinter, el objeto padre es la ventana.
boton1 = ttk.Button(ventana, text="Dar Click", command=evento_click)
# Usamos el pack layout manager para ubicar el botón en la ventana.
boton1.pack()

"""

# Métodos de los eventos.
def evento1():
    boton1.config(text="Botón 1 presionado")
    
def evento2():
    boton2.config(text="Botón 2 presionado")

# Defenimos dos botones.
boton1 = ttk.Button(ventana, text="Botón 1", command=evento1)
boton1.grid(row=0, column=0, sticky="NSWE")

# N(arriba), E(derecha), S(abajo), W(izquierda)
boton2 = ttk.Button(ventana, text="Botón 2", command=evento2)
boton2.grid(row=1, column=0, sticky="NSWE")

boton3 = ttk.Button(ventana, text="Botón 3")
boton3.grid(row=0, column=1, sticky="NSWE")

boton4 = ttk.Button(ventana, text="Botón 4")
boton4.grid(row=1, column=1, sticky="NSWE")



# Inicializamos la ventana, esto va siempre al final del código.
ventana.mainloop()