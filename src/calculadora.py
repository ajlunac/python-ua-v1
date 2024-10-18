import tkinter as tk
from tkinter import messagebox

class Calculadora(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('400x450+450+150')
        self.resizable(0, 0)
        self.title('Calculadora')
        self.iconbitmap(r'resources\img\calculadora.ico')
        # Atributos de clase
        self.expresion = ''
        # Caja de texto (input)
        self.entrada = None
        # StringVar lo utilizamos para obtener el valor de un widget o input.
        self.entrada_texto = tk.StringVar()
        # Creamos los componentes de la calculadora
        self._creacion_componentes()
    
    # Métodos de clase.
    # Método para crear los componentes.
    def _creacion_componentes(self):
        # Creamos un frame para la caja de texto.
        entrada_frame = tk.Frame(self, width=400, height=50, bg='grey')
        entrada_frame.pack(side=tk.TOP)
        # Caja de texto (input)
        entrada = tk.Entry(entrada_frame, font=('Arial', 18, 'bold'), textvariable=self.entrada_texto, width=30, justify=tk.RIGHT)
        entrada.grid(row=0, column=0, ipady=10)
        
        # Agregamos un segundo frame para la parte inferior.
        botones_frame = tk.Frame(self, width=400, height=450, bg='grey')
        botones_frame.pack()
        
        
        # Primer renglón.
        # Botón de Limpiar.
        boton_limpiar = tk.Button(botones_frame, text='C', width=36, height=3, 
                                  bd=0, bg='#eee', cursor='hand2', command=self._evento_limpiar)
        boton_limpiar.grid(row=0, column=0, columnspan=3, padx=1, pady=1)
        
        # Botón de dividir.
        boton_dividir = tk.Button(botones_frame, text='/', width=18, height=3, 
                                  bd=0, bg='#eee', cursor='hand2', command=lambda: self._evento_click('/'))
        boton_dividir.grid(row=0, column=3, padx=1, pady=1)
        
    
    def _evento_limpiar(self):
        self.expresion = ''
        self.entrada_texto.set(self.expresion)
        
    def _evento_click(self, elemento):
        # Concatenamos el nuevo elemento a la expresión ya existente.
        self.expresion = f'{self.expresion}{elemento}'
        self.entrada_texto.set(self.expresion)
        
        
if __name__ == '__main__':
    calculadora = Calculadora()
    calculadora.mainloop()
        