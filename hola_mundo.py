# Importando el módulo tkinter.
import tkinter as tk
# Importamos el módulo del tema tkinter.
from tkinter import ttk
# Importamos el módulo messagebox para mostrar diferentes mensajes.
from tkinter import messagebox

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


boton1 = ttk.Button(ventana, text="Hola Mundo", command=lambda: messagebox.showinfo("Hola Mundo", "¡Hola Mundo!"))
boton1.grid(row=0, column=0, sticky="NSWE", padx=40, pady=30, ipadx=20, ipady=50, columnspan=2, rowspan=2)

# Inicializamos la ventana, esto va siempre al final del código.
ventana.mainloop()