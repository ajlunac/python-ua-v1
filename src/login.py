import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo, showerror, showwarning

ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Login')
ventana.config(bg='#1d2d44')

# Grid de la ventana.
ventana.columnconfigure(0, weight=1)
ventana.rowconfigure(0, weight=1)

# Estilos de la ventana.
estilo = ttk.Style()
estilo.theme_use('clam')
estilo.configure(ventana, background='#1d2d44', foreground='white', fieldbackground='black')
estilo.configure('TButton', background='#005f73')
estilo.map('TButton', background=[('active', '#0a9396')])

# Frame de la ventana.
frame = ttk.Frame(ventana)
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=3)

# Título
etiqueta = ttk.Label(frame, text='Login', font=('Arial', 20))
etiqueta.grid(row=0, column=0, columnspan=2)

# Usuario
usuario_etiqueta = ttk.Label(frame, text='Usuario: ')
usuario_etiqueta.grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)

usuario_caja_texto = ttk.Entry(frame)
usuario_caja_texto.grid(row=1, column=1, sticky=tk.E, padx=5, pady=5)

# Password
password_etiqueta = ttk.Label(frame, text='Password: ')
password_etiqueta.grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)

password_caja_texto = ttk.Entry(frame, show='*')
password_caja_texto.grid(row=2, column=1, sticky=tk.E, padx=5, pady=5)

# Botón
login_boton = ttk.Button(frame, text='Enviar')
login_boton.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

def validar(event):
    usuario = usuario_caja_texto.get()
    password = password_caja_texto.get()
    if usuario == 'root' and password == 'admin':
        showinfo(title='Login exitoso', message='Datos correctos')
    else:
        showerror(title='Login fallido', message='Datos incorrectos')

# Asociar eventos al botón de login.
login_boton.bind('<Return>', validar) # Presionar Enter para validar.
login_boton.bind('<Button-1>', validar) # Click izquierdo para validar.


frame.grid(row=0, column=0)

ventana.mainloop()