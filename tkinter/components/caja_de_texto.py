# Importando el módulo tkinter.
import tkinter as tk
# Importamos el módulo del tema tkinter.
from tkinter import ttk

# Instanciamos la ventana con la librería tkinter.
ventana = tk.Tk()
# Damos título a la ventana.
ventana.title("Manejo de componentes.")
# Asignamos un tamaño a la ventana de 600x400 pixeles (ancho x alto).
ventana.geometry("600x400")
# Configuramos el icono de la ventana.
ventana.iconbitmap(r"resources\img\icono.ico")

# Definimos una variable que podremos modificar posteriormente (set), leer(get).
entrada_var1 = tk.StringVar(value="Valor por defecto")

# Instanciando una caja de texto con el tamaño de 30 caracteres.
entrada1 = ttk.Entry(ventana, width=30, textvariable=entrada_var1)
entrada1.grid(row=0, column=0)
# Insert agrega un texto a la caja de texto.
# entrada1.insert(0, "Introduce una cadena de texto")
# # Se inserta texto al final de la caja de texto.
# entrada1.insert(tk.END, ".")


# Caja de texto de 30 caracteres con show="*" para mostrar el asterisco.
entrada2 = ttk.Entry(ventana, width=30, justify=tk.CENTER, show="*")
entrada2.grid(row=1, column=0)
# Insert agrega un texto a la caja de texto.
entrada2.insert(0, "Introduce una cadena de texto")
# Se inserta texto al final de la caja de texto.
entrada2.insert(tk.END, ".")

# Caja de texto de 30 caracteres deshabilitada.
entrada3 = ttk.Entry(ventana, width=30, justify=tk.CENTER, state=tk.DISABLED)
entrada3.grid(row=2, column=0)
# Insert agrega un texto a la caja de texto.
entrada3.insert(0, "Introduce una cadena de texto")
# Se inserta texto al final de la caja de texto.
entrada3.insert(tk.END, ".")

# Caja de texto de 30 caracteres con solo lectura.
entrada4 = ttk.Entry(ventana, width=30, justify=tk.CENTER, state=tk.NORMAL)
entrada4.grid(row=3, column=0)
# Insert agrega un texto a la caja de texto.
entrada4.insert(0, "Introduce una cadena de texto")
# Se inserta texto al final de la caja de texto.
entrada4.insert(tk.END, ".")
entrada4.config(state="readonly")

def enviar():
    # print(entrada1.get())
    # boton1.config(text=entrada1.get())
    # entrada1.delete(0, tk.END)
    # Recuperamos la información a partir de la variable asociada a la caja de texto.
    boton1.config(text=entrada_var1.get())
    # Modificación utilizamos la variable de text y el método set.
    entrada_var1.set("Cambio de valor")
    # Recuperar la información.
    print(entrada_var1.get())
    print(entrada1.get())

# Botón para el manejo de eventos.
boton1 = ttk.Button(ventana, text="Enviar", command=enviar)
boton1.grid(row=4, column=0)


# Inicializamos la ventana, esto va siempre al final del código.
ventana.mainloop()