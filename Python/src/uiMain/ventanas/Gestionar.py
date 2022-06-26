from tkinter import *

from numpy import expand_dims
from pyparsing import col
from gestorAplicacion.viajes.Ciudad import Ciudad

def verde(evento):
    evento.widget.config(bg="pale green")

def blanco(evento):
    evento.widget.config(bg="white")

class GestionarCiudades(Frame):
    def __init__(self, window):
        super().__init__(window)
        for i in range(5):
            f = Frame(self)
            Label(f, text=f"{Ciudad.getCiudades()[i].getNombre()} - Numero Visitantes : {Ciudad.getCiudades()[i].getNumVisitantes()}").grid(row=0, column=0)
            boton1 = Button(f, text="Gestionar", cursor="hand2", bg="white")
            boton1.bind("<Enter>", verde)
            boton1.bind("<Leave>", blanco)
            boton1.grid(row=1, column=0, sticky="w")
            f.place(relx=0.05, rely=0.05+0.20*i, relwidth=0.5, relheight=0.15)

            f2 = Frame(self)
            Label(f2, text=f"{Ciudad.getCiudades()[i].getNombre()} - Numero Visitantes : {Ciudad.getCiudades()[i].getNumVisitantes()}").grid(row=0, column=0)
            boton2 = Button(f2, text="Gestionar", cursor="hand2", bg="white")
            boton2.bind("<Enter>", verde)
            boton2.bind("<Leave>", blanco)
            boton2.grid(row=1, column=0, sticky="w")
            f2.place(relx=0.5, rely=0.05+0.20*i, relwidth=0.5, relheight=0.15)


        self.place(relx=0, rely=0, relwidth=1, relheight=1)
    

