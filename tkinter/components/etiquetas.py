# Importando el módulo tkinter.
import tkinter as tk
# Importamos el módulo del tema tkinter.
from tkinter import ttk

# Instanciamos la ventana con la librería tkinter.
ventana = tk.Tk()
# Damos título a la ventana.
ventana.title("Manejo de componentes")
# Asignamos un tamaño a la ventana de 600x400 pixeles (ancho x alto).
ventana.geometry("600x400")
# Configuramos el icono de la ventana.
ventana.iconbitmap(r"resources\img\icono.ico")

# variable y caja de texto.
entrada_var1 = tk.StringVar(value="Valor por defecto")
entrada1 = ttk.Entry(ventana, width=30, textvariable=entrada_var1)
entrada1.grid(row=0, column=0)

# Etiqueta Label.
etiqueta1 = tk.Label(ventana, text="Aquí se mostrará el contenido de la caja de texto.")
etiqueta1.grid(row=1, column=0, columnspan=2)

def enviar():
    # Modificamos el texto de la etiqueta.
    etiqueta1.config(text=entrada_var1.get())
    
boton1 = ttk.Button(ventana, text="Enviar", command=enviar)
boton1.grid(row=0, column=1)

# Inicializamos la ventana, esto va siempre al final del código.
ventana.mainloop()