import tkinter as tk
from tkinter import ttk, messagebox

class Login(tk.Tk):
    def __init__(self):
        super().__init__()

        # Ventana principal.
        self.title("Login")
        self.geometry("300x130")
        self.iconbitmap(r"img\icono.ico")
        self.resizable(0,0)

        # Configuración de la grid.
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)
        # Creamos los componentes.
        self._crear_componenetes()
        
    # Definir el método crear_componenetes.
    def _crear_componenetes(self):
        
        # Elementos del usuario.
        lblUsuario = ttk.Label(self, text="Usuario:")
        lblUsuario.grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)
        self.txtUsuario = ttk.Entry(self, width=30)
        self.txtUsuario.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)

        # Elementos de la Password.
        lblPassword = ttk.Label(self, text="Password:")
        lblPassword.grid(row=1, column=0, padx=5, pady=5, sticky=tk.E)
        self.txtPassword = ttk.Entry(self, width=30, show="*")
        self.txtPassword.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)

        # Botón de login.
        btnLogin = ttk.Button(self, text="Login", width=15, command=self._login)
        btnLogin.grid(row=3, column=1, columnspan=2, padx=5, pady=5, sticky=tk.W)

    def _login(self):
        messagebox.showinfo("Datos Login", f"Usuario: {self.txtUsuario.get()}, Password: {self.txtPassword.get()}")


# Ejecutar la ventana.
if __name__ == "__main__":
    frmLogin = Login()
    frmLogin.mainloop()