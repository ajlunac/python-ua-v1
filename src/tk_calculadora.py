import tkinter as tk
from tkinter import messagebox

class Calculadora(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('400x330+450+150')
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
        boton_limpiar = tk.Button(botones_frame, text='C', width=41, height=3, 
                                  bd=0, bg='#eee', cursor='hand2', command=self._evento_limpiar)
        boton_limpiar.grid(row=0, column=0, columnspan=3, padx=1, pady=1)
        
        # Botón de dividir.
        boton_dividir = tk.Button(botones_frame, text='/', width=13, height=3, 
                                  bd=0, bg='#eee', cursor='hand2', command=lambda: self._evento_click('/'))
        boton_dividir.grid(row=0, column=3, padx=1, pady=1)
        
        # Segundo renglón.
        # Botón de 7.
        boton_siete = tk.Button(botones_frame, text='7', width=13, height=3, 
                                bd=0, bg='#fff', cursor='hand2', command=lambda: self._evento_click('7'))
        boton_siete.grid(row=1, column=0, padx=1, pady=1)
        
        # Botón de 8.
        boton_ocho = tk.Button(botones_frame, text='8', width=13, height=3, 
                                bd=0, bg='#fff', cursor='hand2', command=lambda: self._evento_click('8'))
        boton_ocho.grid(row=1, column=1, padx=1, pady=1)
        
        # Botón de 9.
        boton_nueve = tk.Button(botones_frame, text='9', width=13, height=3, 
                                bd=0, bg='#fff', cursor='hand2', command=lambda: self._evento_click('9'))
        boton_nueve.grid(row=1, column=2, padx=1, pady=1)
        
        # Botón de multiplicar.
        boton_multiplicar = tk.Button(botones_frame, text='*', width=13, height=3,
                                    bd=0, bg='#eee', cursor='hand2', command=lambda: self._evento_click('*'))
        boton_multiplicar.grid(row=1, column=3, padx=1, pady=1)
        
        # Tercer renglón.
        # Botón de 4.
        boton_cuatro = tk.Button(botones_frame, text='4', width=13, height=3, 
                                bd=0, bg='#fff', cursor='hand2', command=lambda: self._evento_click('4'))
        boton_cuatro.grid(row=2, column=0, padx=1, pady=1)
        
        # Botón de 5.
        boton_cinco = tk.Button(botones_frame, text='5', width=13, height=3, 
                                bd=0, bg='#fff', cursor='hand2', command=lambda: self._evento_click('5'))
        boton_cinco.grid(row=2, column=1, padx=1, pady=1)
        
        # Botón de 6.
        boton_seis = tk.Button(botones_frame, text='6', width=13, height=3, 
                                bd=0, bg='#fff', cursor='hand2', command=lambda: self._evento_click('6'))
        boton_seis.grid(row=2, column=2, padx=1, pady=1)
        
        # Botón de resta.
        boton_resta = tk.Button(botones_frame, text='-', width=13, height=3,
                                    bd=0, bg='#eee', cursor='hand2', command=lambda: self._evento_click('-'))
        boton_resta.grid(row=2, column=3, padx=1, pady=1)
        
        # Cuarto renglón.
        # Botón de 1.
        boton_uno = tk.Button(botones_frame, text='1', width=13, height=3, 
                                bd=0, bg='#fff', cursor='hand2', command=lambda: self._evento_click('1'))
        boton_uno.grid(row=3, column=0, padx=1, pady=1)
        
        # Botón de 2.
        boton_dos = tk.Button(botones_frame, text='2', width=13, height=3, 
                                bd=0, bg='#fff', cursor='hand2', command=lambda: self._evento_click('2'))
        boton_dos.grid(row=3, column=1, padx=1, pady=1)
        
        # Botón de 3.
        boton_tres = tk.Button(botones_frame, text='3', width=13, height=3, 
                                bd=0, bg='#fff', cursor='hand2', command=lambda: self._evento_click('3'))
        boton_tres.grid(row=3, column=2, padx=1, pady=1)
        
        # Botón de suma.
        boton_suma = tk.Button(botones_frame, text='+', width=13, height=3,
                                    bd=0, bg='#eee', cursor='hand2', command=lambda: self._evento_click('+'))
        boton_suma.grid(row=3, column=3, padx=1, pady=1)
        
        # Quinto renglón.
        # Botón de 0.
        boton_cero = tk.Button(botones_frame, text='0', width=27, height=3, 
                                bd=0, bg='#fff', cursor='hand2', command=lambda: self._evento_click('0'))
        boton_cero.grid(row=4, column=0, columnspan=2, padx=1, pady=1)
        
        # Botón de punto.
        boton_punto = tk.Button(botones_frame, text='.', width=13, height=3,
                                    bd=0, bg='#eee', cursor='hand2', command=lambda: self._evento_click('.'))
        boton_punto.grid(row=4, column=2, padx=1, pady=1)
        
        # Botón de igual.
        boton_evaluar = tk.Button(botones_frame, text='=', width=13, height=3,
                                    bd=0, bg='#eee', cursor='hand2', command=self._evento_evaluar)
        boton_evaluar.grid(row=4, column=3, padx=1, pady=1)
        
    def _evento_evaluar(self):
        # eval evalua la expresión str como una expresión aritmética y devuelve el resultado.
        try:
            if self.expresion:
                resultado = str(eval(self.expresion))
                self.entrada_texto.set(resultado)
        except Exception as e:
            messagebox.showerror('Error', f'Ocurrió un error al evaluar la expresión.\nError: {e}')
            self.entrada_texto.set('')
        finally:
            self.expresion = ''
        
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
        