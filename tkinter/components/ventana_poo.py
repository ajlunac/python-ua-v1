import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

class App(tk.Tk):
    def __init__(self):
        super().__init__() # Constructor de la clase padre.
        # Configuración de la ventana.
        self.configurar_ventana()
        # Configurar el grid.
        self.configurar_grid()
        # Mostrar tabla.
        self.mostrar_tabla()
        
    def configurar_ventana(self):
        self.geometry('600x400')
        self.configure(bg='#1d2d44')
        self.title('Manejo de ventanas con POO')

    def configurar_grid(self):
        self.columnconfigure(0, weight=1)   
        self.columnconfigure(1, weight=0)
        
    def mostrar_tabla(self):
        # Definir un estilo.
        estilos = ttk.Style()
        estilos.theme_use('clam') # Prepara el manejo del tema oscuro.
        estilos.configure('Treeview', background='black', foreground='white', fieldbackground='black', rowheight=30)
        estilos.map('Treeview', background=[('selected', '#3a86ff')])
        
        # Definir las columnas.
        columnas = ('Id', 'Nombre', 'Edad')
        self.tabla = ttk.Treeview(self, columns=columnas, show='headings')

        # Cabecera de la tabla.
        self.tabla.heading('Id', text='Id', anchor=tk.W)
        self.tabla.heading('Nombre', text='Nombre', anchor=tk.W)
        self.tabla.heading('Edad', text='Edad', anchor=tk.W)
        
        # Formato a las columnas.
        self.tabla.column('Id', width=80)
        self.tabla.column('Nombre', width=120)
        self.tabla.column('Edad', width=120)
        
        # Cargar datos a la tabla.
        datos = ((1, 'Alejandra', 25), (2, 'Matias', 32))    
        for persona in datos:
            self.tabla.insert(parent='', index=tk.END, values=persona)
            
        # Agregamos un scrollbar.
        scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.tabla.yview)
        self.tabla.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky=tk.NS)
        
        # Asociar el evento de select de la tabla.
        self.tabla.bind('<<TreeviewSelect>>', self.mostrar_registro_seleccionado)
        
        # Publicamos la tabla.
        self.tabla.grid(row=0, column=0, sticky=tk.NSEW)
        
    # Mostrar registro seleccionado.
    def mostrar_registro_seleccionado(self, event):
        print('Ejecutando método mostrar_registro_seleccionado')
        elemento_seleccionado = self.tabla.selection()[0] # Solo procesamos el primer registro.
        elemento =self.tabla.item(elemento_seleccionado) # item.
        persona = elemento['values'] # Tupla de personas.
        showinfo(title='Persona seleccionada', message=f'Persona: {persona}')
        


if __name__ == '__main__':
    app = App()
    app.mainloop()