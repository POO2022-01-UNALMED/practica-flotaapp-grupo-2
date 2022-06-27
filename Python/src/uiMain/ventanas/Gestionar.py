from tkinter import *
from tkinter import messagebox, ttk

from gestorAplicacion.viajes.Ciudad import Ciudad
from gestorAplicacion.viajes.Viaje import Viaje
from uiMain.ventanas.ManejoErrores import ExceptionPopUp

def color(evento, color):
    evento.widget.config(bg= color)

class GestionarCiudades(Frame):
    def __init__(self, window):
        super().__init__(window)
        self._window = window
        self._frame = Frame(self)
        self.MatarTodo(self._frame)
        self.option_add("*tearOff",  FALSE)

        self.valorDefecto = StringVar(value="Seleccione Ciudad")
        self.combo = ttk.Combobox(self, state="readonly",  values=[ ciudad.getNombre() for ciudad in Ciudad.getCiudades()], textvariable=self.valorDefecto)
        boton1 = Button(self._frame, text="Gestionar", cursor="hand2", bg="white", command= self.ventanaGestionar)
        boton1.bind("<Enter>", lambda event: color(event, "pale green"))
        boton1.bind("<Leave>", lambda event: color(event, "white"))   

        self.combo.place(relx=0.05, rely=0.05, relwidth=0.5, relheight=0.08)
        boton1.place(relx=0.6, rely=0.05, relwidth=0.1, relheight=0.08)

        self._frame.place(relx=0, rely=0, relwidth=1, relheight=1)
    
    def ventanaGestionar(self):     
        for i in Ciudad.getCiudades():
            if i.getNombre() == self.combo.get():
                ciudad = i
        
        self._frameViaje = Frame(self._frame)
        
        idsViajes = []
        for i in range(len(Viaje.getViajes())):
            viaje = Viaje.getViajes()[i]    
            if viaje.getDestino().getNombre() == self.combo.get() or viaje.getOrigen().getNombre() == self.combo.get():
                Label(self._frameViaje, text=f"[{i}]  -  Viaje : {viaje}").pack()
                idsViajes.append(i)
            
        self._frameViaje.place(relx=0.05, rely=0.45, relwidth=0.9, relheight=0.5)


        Label(self._frame, text= f"Promocion Actual : {ciudad.getPromocion()}        Direccion : {ciudad.getDireccion()}" , font=('Times 12')).place(relx=0.05, rely=0.25, relwidth=0.9, relheight=0.1)
        Label(self._frame, text= f"Puntaje   Actual : {ciudad.getPuntaje()}          Numero Visitantes : {ciudad.getNumVisitantes()}" , font=('Times 12')).place(relx=0.05, rely=0.35, relwidth=0.9, relheight=0.1)
        
        self.valorDefectoViaje = StringVar(value="Seleccione Viaje")
        self.comboViaje = ttk.Combobox(self, state="readonly",  values= idsViajes, textvariable=self.valorDefectoViaje)
        Bpromocion = Button(self._frame, text="Promocionar", cursor="hand2", bg="white")
        BEliminar = Button(self._frame, text="Eliminar", cursor="hand2", bg="white", command= self.ElimarViaje)
        
        Bpromocion.bind("<Enter>", lambda event: color(event, "pale green"))
        Bpromocion.bind("<Leave>", lambda event: color(event, "white"))   

        BEliminar.bind("<Enter>", lambda event: color(event, "red"))
        BEliminar.bind("<Leave>", lambda event: color(event, "white"))   

        self.comboViaje.place(relx=0.05, rely=0.15, relwidth=0.1, relheight=0.05)
        Bpromocion.place(relx=0.15, rely=0.15, relwidth=0.15, relheight=0.05)
        BEliminar.place(relx=0.3, rely=0.15, relwidth=0.1, relheight=0.05)


    def ElimarViaje(self):
        viaje = Viaje.getViajes()[int(self.comboViaje.get())]
        viaje.eliminarViaje()
        self._frameViaje.destroy()
        self.ventanaGestionar()


    def MatarTodo(self, frameUsado):
        for frame in self.winfo_children():
            frame.pack_forget()
        frameUsado.pack(fill=BOTH,expand=True)

