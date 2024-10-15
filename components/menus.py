import sys
import tkinter as tk
from tkinter import ttk, messagebox, Menu

ventana = tk.Tk()
ventana.title("Manejo de componentes")
ventana.geometry("600x400")
ventana.iconbitmap(r"img\icono.ico")


entrada1 = ttk.Entry(ventana, width=30)
entrada1.grid(row=0, column=0)

etiqueta1 = tk.Label(ventana, text="Aquí se mostrará el contenido de la caja de texto.")
etiqueta1.grid(row=1, column=0, columnspan=2)

def enviar():
    etiqueta1.config(text=entrada1.get())
    mensaje1 = entrada1.get()
    if mensaje1:
        messagebox.showinfo("Mensaje Informativo", mensaje1 + " Informativo")
        
def salir():
    ventana.quit()
    ventana.destroy()
    print("Saliendo...")
    sys.exit()
        
def crear_menu():
    # Configurar el menú principal.
    menu_principal = Menu(ventana)
    
    # tearoff=FALSE para evitar que se pueda separar el menú de la interfaz.
    submenu_archivo = Menu(menu_principal, tearoff=False)
    # Agregamos una nueva opción al menú archivo.
    submenu_archivo.add_command(label="Nuevo")
    # Agregar un separador.
    submenu_archivo.add_separator()
    # Agrgamos la opción de salir.
    submenu_archivo.add_command(label="Salir", command=salir)
    # Agregamos el submenú archivo al menú principal.
    menu_principal.add_cascade(menu=submenu_archivo, label="Archivo")
    
    # Submenu ayuda.
    submenu_ayuda = Menu(menu_principal, tearoff=False)
    submenu_ayuda.add_command(label="Acerca de...", command=lambda: messagebox.showinfo("Acerca de...", "Este es un programa de ejemplo"))
    menu_principal.add_cascade(menu=submenu_ayuda, label="Ayuda")

    # Mostramos el menú en la ventana principal.
    ventana.config(menu=menu_principal)
        
boton1 = ttk.Button(ventana, text="Enviar", command=enviar)
boton1.grid(row=0, column=1)

crear_menu()


ventana.mainloop()