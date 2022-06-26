from tkinter import *

from gestorAplicacion.viajes.Ciudad import Ciudad
from gestorAplicacion.viajes.Viaje import Viaje
from uiMain.ventanas.ManejoErrores import ExceptionPopUp

def verde(evento):
    evento.widget.config(bg="pale green")

def blanco(evento):
    evento.widget.config(bg="white")

class GestionarCiudades(Frame):
    def __init__(self, window):
        super().__init__(window)
        self._window = window
        self._frame = Frame(self)
        self.MatarTodo(self._frame)
        self.option_add("*tearOff",  FALSE)


        rowInt= 0
        colInt= -1
        for i in range(len(Ciudad.getCiudades())):  
            if 1 == colInt :
                rowInt +=1
                colInt = 0
            else:
                colInt += 1
            f = Frame(self._frame)
            Label(f, text=f"[{i+1}]  -  {Ciudad.getCiudades()[i].getNombre()} - Numero Visitantes : {Ciudad.getCiudades()[i].getNumVisitantes()}").grid(row=0, column=0)
            f.place(relx=0.05+colInt*0.45, rely=0.2+0.11*rowInt, relwidth=0.5, relheight=0.1)

        ciudadGestionar = Entry(self._frame, textvariable= StringVar(self._frame, "ID"))
        boton1 = Button(self._frame, text="Gestionar", cursor="hand2", bg="white", command= lambda : self.ventanaGestionar(ciudadGestionar.get()))
        boton1.bind("<Enter>", verde)
        boton1.bind("<Leave>", blanco)   
        ciudadGestionar.place(relx=0.05, rely=0.05, relwidth=0.1, relheight=0.1)
        boton1.place(relx=0.15, rely=0.05, relwidth=0.1, relheight=0.1)

        self._frame.place(relx=0, rely=0, relwidth=1, relheight=1)
    
    def ventanaGestionar(self, IdCiudad):
        try: 
            ciudad = Ciudad.getCiudades()[int(IdCiudad)-1]                
        except ValueError:
            raise ExceptionPopUp("Ingrese un valor Numerico")
        except IndexError:
            raise ExceptionPopUp(f"Ingrese un numero entre 1 - {len(Ciudad.getCiudades())}")
        
        top = Toplevel(self._frame)
        top.geometry("580x320")
        top.resizable(False,False)
        top.title("Aplicación") 
        Label(top, text= f"{ciudad.getNombre()}" , font=('Times 12')).place(relx=0, rely=0.05, relwidth=1, relheight=0.1)
        Label(top, text= f"Promocion Actual : {ciudad.getPromocion()}        Direccion : {ciudad.getDireccion()}" , font=('Times 12')).pack()
        Label(top, text= f"Puntaje   Actual : {ciudad.getPuntaje()}          Numero Visitantes : {ciudad.getNumVisitantes()}" , font=('Times 12')).pack()

        for i in range(len(Viaje.getViajes())):
            viaje = Viaje.getViajes()[i]
            if viaje.getDestino().getId() == ciudad.getId():
                Label(top, text=f"[{i+1}]  -  Viaje : {viaje}").pack()
    
    def MatarTodo(self, frameUsado):
        for frame in self.winfo_children():
            frame.pack_forget()
        frameUsado.pack(fill=BOTH,expand=True)

