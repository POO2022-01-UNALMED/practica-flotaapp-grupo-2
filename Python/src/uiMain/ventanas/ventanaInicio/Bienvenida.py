from uiMain.ventanas.VentanaUsuario import VentanaUsuario
from tkinter import Label, Entry, Button, PhotoImage, Frame, INSERT, scrolledtext, DISABLED
from PIL import Image, ImageTk
import os
import pathlib

class Bienvenida(Frame):
    def __init__(self, window):
        super().__init__(window)
        self._window = window
        self._p3 = Frame(self)
        self._p4 = Frame(self)
        self._next_el = 0
        saludo = Label(self._p3, width=100, text="Bienvenido al software de Flota-APP")
        self.saludo2 = scrolledtext.ScrolledText(self._p3, height=5)
        self.saludo2.tag_configure("center", justify="center")
        self.saludo2.insert(INSERT, """Estimado usuario, bienvenido a FlotaAPP. 
Somos una APP que gestiona los diferentes servicios de una flota 
de autobuses con diferentes funcionalidades como:  automatizar la 
compra de tiquetes, la ocupación y disponibilidad de viajes, 
guardar registros de sus viajes e implementar recomendaciones 
personalizadas en cada usuario y desarrollar las distintas 
estadísticas por ciudad y por viaje. Todo esto, con el objetivo de 
facilitar y mejorar la calidad del tedioso proceso de organizar un viaje.""")
        self.saludo2.config(state = DISABLED)
        self._pantallazos = []
        for i in range(0, 5):
            path = os.path.join(pathlib.Path(__file__).parent.parent.parent.absolute(),'assets/pantallazo_{0}.png'.format(i))
            pantallazo = ImageTk.PhotoImage(Image.open(path).resize((600, 400)))
            self._pantallazos.append(pantallazo)

        self._label = Label(self._p4, image=self._pantallazos[0], height=500, width=750)
        self._label.bind('<Enter>', self.proximo)
        self._label.pack()

        button = Button(self._p4, text="Ventana Principal del Administrador", command=self.abrir_ventana_principal)
        button.pack()
        saludo.grid()
        self._p3.pack()
        self._p4.pack()

    # Actualiza el proximo pantallazo de la aplicacion
    def proximo(self, _):
        if self._next_el < 4:
            self._next_el = self._next_el + 1
        else:
            self._next_el = 0

        self._label.configure(image=self._pantallazos[self._next_el])
        self._label.image = self._pantallazos[self._next_el]

    # Carga la ventana principal del admin y cierra la ventana actual
    def abrir_ventana_principal(self):
        self._window.destroy()
        VentanaUsuario()