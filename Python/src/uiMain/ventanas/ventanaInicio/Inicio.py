from tkinter import Tk, Menu
from uiMain.ventanas.ventanaInicio.HojaVida import HojaVida
from uiMain.ventanas.ventanaInicio.Bienvenida import Bienvenida

class VentanaInicio(Tk):
    def __init__(self):
        super().__init__()
        self.title('Flota-APP')
        self.option_add("*tearOff",  False)
        self.menubar = Menu(self)
        inicio = Menu(self.menubar)
        inicio.add_command(label="Descripcion", command=lambda: self.bienvenida.saludo2.grid())
        inicio.add_command(label="Salir", command=lambda : self.destroy())

        self.menubar.add_cascade(label="Inicio", menu=inicio)
        self.config(menu=self.menubar)
        self.hoja_vida = HojaVida(self)
        self.bienvenida = Bienvenida(self)
        self.hoja_vida.grid(row=0, column=1)
        self.bienvenida.grid(row=0, column=0)
