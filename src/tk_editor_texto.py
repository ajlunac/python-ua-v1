import tkinter as tk
from tkinter.filedialog import askopenfile, asksaveasfilename

class Editor(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Editor de Texto')
        # Configuración tamaño mínimo de la ventana.
        self.rowconfigure(0, minsize=600, weight=1)
        # Configuración mínima de la segunda columna
        self.columnconfigure(1, minsize=600, weight=1)
        # Atributo de campo de texto.
        self.campo_texto = tk.Text(self, wrap=tk.WORD)
        # Atributo de archivo.
        self.archivo = None
        # Atributo para saber si ya se abrío un archivo anteriormente.
        self.archivo_abierto = False
        # Creación de componentes.
        self._crear_componenets()
        # Crear menú.
        self._crear_menu()
        
    
    def _crear_componenets(self):
        frame_botones = tk.Frame(self, relief=tk.RAISED, bd=2)
        boton_abrir = tk.Button(frame_botones, text='Abrir', command=self._abrir_archivo)
        boton_guardar = tk.Button(frame_botones, text='Guardar', command=self._guardar)
        boton_guardar_como = tk.Button(frame_botones, text='Guardar Como...', command=self._guardar_como)
        # Los botones los expandimos de manera horizontal (sticky='we').
        boton_abrir.grid(row=0, column=0, sticky='we', padx=5, pady=5)
        boton_guardar.grid(row=1, column=0, sticky='we', padx=5, pady=5)
        boton_guardar_como.grid(row=2, column=0, sticky='we', padx=5, pady=5)
        # Se coloca el frame de manera vertical (sticky='ns').
        frame_botones.grid(row=0, column=0, sticky='ns')
        # Agregamos el campo de texto, se expandirá por completo en el espacio que le reste sticky='nsew').
        self.campo_texto.grid(row=0, column=1, sticky='nsew')
    
    
    def _crear_menu(self):
        # Creamos el menú de la app.
        menu_app = tk.Menu(self)
        self.config(menu=menu_app)
        # Agregamos las opciones al menú.
        # Agregamos menu archivo.
        menu_archivo = tk.Menu(menu_app, tearoff=False)
        menu_app.add_cascade(label='Archivo', menu=menu_archivo)
        # Agregamos las opciones del menú archivo.
        menu_archivo.add_command(label='Abrir', command=self._abrir_archivo)
        menu_archivo.add_command(label='Guardar', command=self._guardar)
        menu_archivo.add_command(label='Guardar Como...', command=self._guardar_como)
        menu_archivo.add_separator()
        menu_archivo.add_command(label='Salir', command=self.quit)
        
    
    def _abrir_archivo(self):
        # Abrir archivo para editar (lectura y escritura).
        self.archivo_abierto = askopenfile(mode='r+')
        # Eliminar el texto anterior.
        self.campo_texto.delete('1.0', tk.END)
        # Revisamos si hay un archivo.
        if not self.archivo_abierto:
            return
        # Abrimos el archvio en modo de lectura y escritura como un recurso.
        with open(self.archivo_abierto.name, 'r+') as self.archivo:
            # Leemos el contenido del archvio.
            texto = self.archivo.read()
            # Insertamos el contenido en el campo de texto.
            self.campo_texto.insert('1.0', texto)
            # Modificamos el título de la aplicación.
            self.title(f'*Editor de Texto - {self.archivo.name}')
            
    def _guardar(self):
        # Si ya se abrió previamente un archivo, lo sobreescribimos.
        if self.archivo_abierto:
            # Salvamos el archivo (lo abrimos en modo escritura)
            with open(self.archivo_abierto.name, 'w') as self.archivo:
                # Leemos el contenido de la caja de texto.
                texto = self.campo_texto.get('1.0', tk.END)
                # Escribimos el contenido al mismo archivo.
                self.archivo.write(texto)
                # cambiamos el título de la aplicación.
                self.title(f'Editor de Texto - {self.archivo.name}')
        else:
            self._guardar_como()
                
    def _guardar_como(self):
        # Salvamos el archivo actual como un nuevo archivo.
        self.archivo = asksaveasfilename(
            defaultextension='.txt',
            filetypes=[('Archivos de Texto', '*.txt'), ('Todos los Archivos', '*.*')]
        )
        if not self.archivo:
            return
        # Abrimos el archivo en modo de escritura.
        with open(self.archivo, 'w') as archivo:
            # Leemos el contenido de la caja de texto.
            texto = self.campo_texto.get('1.0', tk.END)
            # Escribimos el contenido al nuevo archivo.
            archivo.write(texto)
            # Cambiamos el título de la aplicación.
            self.title(f'Editor de Texto - {archivo.name}')
            # Indicamos que hemos abierto un archivo.
            self.archivo_abierto = archivo
        
        
if __name__ == "__main__":
    editor = Editor()
    editor.mainloop()