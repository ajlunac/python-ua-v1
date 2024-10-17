import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from time import sleep

class Componentes(tk.Tk):
    def __init__(self):
        super().__init__()

        # Ventana principal.
        self.title("Componentes")
        self.geometry("650x400+450+200")
        self.iconbitmap(r"resources\img\icono.ico")
        self._crear_tabs()

    def _crear_componentes_tabulador1(self, tabulador):
        # Agregar una etiqueta y un componente de entrada.
        lblEtiqueta1 = ttk.Label(tabulador, text="Nombre:")
        lblEtiqueta1.grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)
        txtEntrada1 = ttk.Entry(tabulador, width=30)
        txtEntrada1.grid(row=0, column=1, padx=5, pady=5)
        
        # Agregar un botón.
        def enviar():
            messagebox.showinfo("Mensaje", f"Nombre: {txtEntrada1.get()}")
            
        btnBoton1 = ttk.Button(tabulador, text="Enviar", command=enviar)
        btnBoton1.grid(row=1, column=0, columnspan=2)
    
    def _crear_componentes_tabulador2(self, tabulador):
        contenido = 'Este es el contenido del segundo tabulador.'
        # Creamos el componete de scroll.
        scroll = scrolledtext.ScrolledText(tabulador, width=50, height=10, wrap=tk.WORD)
        scroll.insert(tk.INSERT, contenido)
        # Mostramos el componente de scroll.
        scroll.grid(row=0, column=0)
    
    def _crear_componentes_tabulador3(self, tabulador):
        # Creamos una lista usando data list comprehension.
        datos = [x+1 for x in range(10)]
        cboComboBox = ttk.Combobox(tabulador, width=15, values=datos)
        cboComboBox.grid(row=0, column=0, padx=10, pady=10)
        # Seleccionamos un elemento por defecto a mostrar.
        cboComboBox.current(5)
        # Agregar un botón para saber que opción seleccionó el usuario.
        def mostrar_valor():
            messagebox.showinfo("Valor seleccionado", f"Valor seleccionada: {cboComboBox.get()}")
            
        btnBoton1 = ttk.Button(tabulador, text="Mostrar valor seleccionado", command=mostrar_valor)
        btnBoton1.grid(row=0, column=1, padx=10, pady=10)
        
    def _crear_componentes_tabulador4(self, tabulador):
        imagen = tk.PhotoImage(file=r"resources\img\python-logo.png")
        
        def mostrar_titulo():
            messagebox.showinfo("Más info imagen", f"Nombre imagen: {imagen.cget('file')}")
        
        btnBotonImagen = ttk.Button(tabulador, image=imagen, command=mostrar_titulo)
        btnBotonImagen.grid(row=0, column=0)
        
    def _crear_componentes_tabulador5(self, tabulador):
        # Creamos el componente de barra de progreso.
        barra_progreso = ttk.Progressbar(tabulador, orient=tk.HORIZONTAL, length=550, mode="determinate")
        barra_progreso.grid(row=0, column=0, padx=10, pady=10, columnspan=4)
        # Métodos para controlar los eventos de la barra de progreso.
        def ejecutar_barra_progreso():
            barra_progreso['maximum'] = 100
            for valor in range(101):
                # Mandamos a esperar un poco antes de continuar con la ejecución de la barra de progreso.
                sleep(0.05)
                # Incremenetamos el valor de la barra de progreso.
                barra_progreso['value'] = valor
                # Actualizamos la barra de progreso.
                barra_progreso.update()
            barra_progreso['value'] = 0
        
        def ejecutar_ciclo():
            barra_progreso.start()
            
        def detener():
            barra_progreso.stop()
            
        def detener_despues():
            esperar_ms = 1000
            self.after(esperar_ms, barra_progreso.stop)
            
        # Botones para controlar la barra de progreso.
        btnInicio = ttk.Button(tabulador, text="Ejecutar barra de progreso", command=ejecutar_barra_progreso)
        btnInicio.grid(row=1, column=0)
        btnCiclo = ttk.Button(tabulador, text="Ejecutar ciclo", command=ejecutar_ciclo)
        btnCiclo.grid(row=1, column=1)
        btnDetener = ttk.Button(tabulador, text="Detener ejecución", command=detener)
        btnDetener.grid(row=1, column=2)
        btnDespues = ttk.Button(tabulador, text="Detener ejecución después", command=detener_despues)
        btnDespues.grid(row=1, column=3)
    

    def _crear_tabs(self):
        # creamos un tab control, para ello usamos la clase Notebook.
        control_tabulador = ttk.Notebook(self)
        # Agragamos un marco (frame) para agregar dentro del tab y poder organizar los elementos.
        tabulador1 = ttk.Frame(control_tabulador)
        # Agregamos el tabulador al control de tabuladores.
        control_tabulador.add(tabulador1, text="Tabulador 1")
        # Mostramos el tabulador.
        control_tabulador.pack(fill="both")
        # Creamos los componenetes del tabulador1.
        self._crear_componentes_tabulador1(tabulador1)
        # Creamos un segundo tabulador.
        tabulador2 = ttk.LabelFrame(control_tabulador, text="Contenido")
        control_tabulador.add(tabulador2, text="Tabulador 2")
        # Componenetes del segundo tabulador.
        self._crear_componentes_tabulador2(tabulador2)
        # Creamos un tercer tabulador.
        tabulador3 = ttk.Frame(control_tabulador)
        control_tabulador.add(tabulador3, text="Tabulador 3")
        # Creamos los componenetes del tercer tabulador.
        self._crear_componentes_tabulador3(tabulador3)
        # Creamos un cuarto tabulador.
        tabulador4 = ttk.LabelFrame(control_tabulador, text="Imagen")
        control_tabulador.add(tabulador4, text="Tabulador 4")
        # Creamos los componenetes del cuarto tabulador.
        self._crear_componentes_tabulador4(tabulador4)
        # Creamos un quinto tabulador.
        tabulador5 = ttk.LabelFrame(control_tabulador, text="Progress bar")
        control_tabulador.add(tabulador5, text="Tabulador 5")
        # Creamos los componenetes del quinto tabulador.
        self._crear_componentes_tabulador5(tabulador5)
    

# Ejecutamos la ventana.
if __name__ == "__main__":
    frmVentana = Componentes()
    frmVentana.mainloop()