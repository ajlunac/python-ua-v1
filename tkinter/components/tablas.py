import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo, showerror, showwarning

# Ventana principal.
ventana = tk.Tk()
ventana.title('Manejo de tablas')
ventana.geometry('600x400')
ventana.configure(bg='#1d2d44')

# Configurar el grid.
ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=0)

# Definir un estilo.
estilos = ttk.Style()
estilos.theme_use('clam') # Prepara el manejo del tema oscuro.
estilos.configure('Treeview', background='black', foreground='white', fieldbackground='black', rowheight=30)
estilos.map('Treeview', background=[('selected', '#3a86ff')])

# Definir las columnas.
columnas = ('Id', 'Nombre', 'Edad')
tabla = ttk.Treeview(ventana, columns=columnas, show='headings')

# Cabecera de la tabla.
tabla.heading('Id', text='Id', anchor=tk.W)
tabla.heading('Nombre', text='Nombre', anchor=tk.W)
tabla.heading('Edad', text='Edad', anchor=tk.W)

# Formato a las columnas.
tabla.column('Id', width=80)
tabla.column('Nombre', width=120)
tabla.column('Edad', width=120)

# Cargar datos a la tabla.
datos = ((1, 'Alejandra', 25), (2, 'Matias', 32))    
for persona in datos:
    tabla.insert(parent='', index=tk.END, values=persona)

# Agregamos un scrollbar.
scrollbar = ttk.Scrollbar(ventana, orient=tk.VERTICAL, command=tabla.yview)
tabla.configure(yscroll=scrollbar.set)
scrollbar.grid(row=0, column=1, sticky=tk.NS)

# Mostrar registro seleccionado.
def mostrar_registro_seleccionado(event):
    print('Ejecutando método mostrar_registro_seleccionado')
    elemento_seleccionado = tabla.selection()[0] # Solo procesamos el primer registro.
    elemento = tabla.item(elemento_seleccionado) # item.
    persona = elemento['values'] # Tupla de personas.
    showinfo(title='Persona seleccionada', message=f'Persona: {persona}')
    
# Asociar el evento de select de la tabla.
tabla.bind('<<TreeviewSelect>>', mostrar_registro_seleccionado)
    
# Publicamos la tabla.
tabla.grid(row=0, column=0, sticky=tk.NSEW)


ventana.mainloop()
