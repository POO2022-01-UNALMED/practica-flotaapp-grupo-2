from cProfile import label
from tkinter import *
from tkinter import messagebox, ttk, simpledialog

from matplotlib.pyplot import text 

from gestorAplicacion.viajes.Ciudad import Ciudad
from gestorAplicacion.viajes.Viaje import Viaje
from gestorAplicacion.personas.Comprador import Comprador
from gestorAplicacion.viajes.Tiquete import Tiquete
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
        Bpromocion = Button(self._frame, text="Evaluar", cursor="hand2", bg="white", command= self.EvaluarViaje)
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
    
    def EvaluarViaje(self):
        try:
            promocionar = Viaje.getViajes()[int(self.comboViaje.get())]
        except:
            ExceptionPopUp("Ingrese un ID valido para un viaje")

        
        porcentaje = ((len(promocionar.getVehiculo().getSillas()) - len(promocionar.tiquetesDisponibles()))*100)/len(promocionar.getVehiculo().getSillas())
        message = f"Porcentaje Ocupacion = {porcentaje}\nNo se a podido promocionar el Viaje"
        if (porcentaje >= 85):
            promocionar.aumentarFrecuencia(1)
            message = f"Porcentaje Ocupacion = {porcentaje}\nLa frecuencia del viaje se a aumentado en una hora"
            messagebox.showinfo(title = "Promocion de Viaje", message = message)
        
        elif porcentaje <85 and porcentaje >= 45:
            message = f"Porcentaje Ocupacion = {porcentaje}\n¿Desea promocionar este viaje?"
            des = messagebox.askyesno(title = "Promocion de Viaje", message = message)
            if des == True:
                res = simpledialog.askstring('Promocion', 'Dime la promocion')
                promocionar.getDestino().setPromocion(int(res))
                messagebox.showinfo(title = "Promocion de Viaje", message = "El viaje a sido promocionado")

        elif (porcentaje >= 20 and porcentaje < 45):
            promocionar.disminuirFrecuencia(2)
            message = f"Porcentaje Ocupacion = {porcentaje}\nLa frecuencia del viaje se a disminuido en dos hora"
            messagebox.showinfo(title = "Promocion de Viaje", message = message)
        
        elif(porcentaje < 20):
            message = f"Porcentaje Ocupacion = {porcentaje}\n¿Desea Eliminar el viaje?"
            des = messagebox.askyesno(title = "Promocion de Viaje", message = message)
            if des == True:
                self.ElimarViaje()

        


    def MatarTodo(self, frameUsado):
        for frame in self.winfo_children():
            frame.pack_forget()
        frameUsado.pack(fill=BOTH,expand=True)


class GestionarViajes(Frame):

    def __init__(self, window):
        super().__init__(window)
        self._vTop = Frame(self)
        self.entrada = StringVar(value=1)

        title = Label(self, text="G E S T I O N A R   V I A J E S").place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.08) 
        viaje = Label(self, text="Gestionar viaje con la cédula: ").place(relx=0.05, rely=0.15, relwidth=0.3, relheight=0.08) 
        info = Entry(self, borderwidth=2, textvariable = self.entrada).place(relx=0.32, rely=0.15, relwidth=0.45, relheight=0.08) 
        buscar = Button(self, text="Buscar", command= self.FrameComprador ).place(relx=0.75, rely=0.15, relwidth=0.15, relheight=0.08) 


    def FrameComprador(self):
        valor = int(self.entrada.get())
        self._vTop.destroy()
        self._vTop = Frame(self)

        listaTiquete = []
        compradorTiquete = Comprador()
        for comprador in Comprador.getCompradores():
            if comprador.getCc() == valor:
                compradorTiquete = comprador
                listaTiquete = [f"{t.getId()} - {t.getViaje()} - {t.getSillaTiquete()}" for t in comprador.getHistorioViaje()]

        Label(self._vTop, text= f"CC: {comprador.getCc()} - Nombre : {compradorTiquete.getuNombre()}").place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.08)
        self.valorDefectoTiquete = StringVar(value="Seleccione Viaje")
        self.comboTiquete = ttk.Combobox(self._vTop, state="readonly",  values= listaTiquete, textvariable=self.valorDefectoTiquete, width=15)
        self.comboTiquete.place(relx=0.05, rely=0.15, relwidth=0.7, relheight=0.08)
        buscarTiquetes = Button(self._vTop, text="Gestionar", command= self.FrameTiquete)
        buscarTiquetes.place(relx=0.75, rely=0.15, relwidth=0.2, relheight=0.08)    

        self._vTop.place(relx=0.05, rely=0.25, relwidth=0.9, relheight=0.7) 

        self._frameInfoTiquete = Frame(self._vTop)


    def FrameTiquete(self):
        
        def cancelarTiquete():
            Label(self._vTop, text="Tu tiquete ha sido cancelado").place(relx=0.05, rely=0.55, relwidth=0.9, relheight=0.08)    

        self._frameInfoTiquete.destroy()
        self._frameInfoTiquete = Frame(self._vTop)
        tiquete = Tiquete.buscarTiquete(int(self.comboTiquete.get()[:3]))
        print(tiquete)
        Label(self._frameInfoTiquete,  text= f"Silla = {tiquete.getSillaTiquete()}").pack()
        Label(self._frameInfoTiquete,  text= f"Viaje = {tiquete.getViaje()}").pack()
        Label(self._frameInfoTiquete,  text= f"Valor = {tiquete.getValor()} Fecha = {tiquete.getFechaCompra()}").pack()

        self._frameInfoTiquete.place(relx=0.05, rely=0.25, relwidth=0.9, relheight=0.20) 
         

        BCambiar = Button(self._vTop, text="Cambiar Tiquete", command= self.CambiarTiquete) 
        BCancelar = Button(self._vTop, text="Cancelar Tiquete", command= cancelarTiquete)
        
        BCambiar.bind("<Enter>", lambda event: color(event, "pale green"))
        BCambiar.bind("<Leave>", lambda event: color(event, "white"))   

        BCancelar.bind("<Enter>", lambda event: color(event, "red"))
        BCancelar.bind("<Leave>", lambda event: color(event, "white"))   

        BCambiar.place(relx=0.05, rely=0.45, relwidth=0.45, relheight=0.08)   
        BCancelar.place(relx=0.5, rely=0.45, relwidth=0.45, relheight=0.08)    

        self._vTop.place(relx=0.05, rely=0.25, relwidth=0.9, relheight=0.7) 


    def CambiarTiquete(self):

        self.CambioTiquete = Toplevel(self)
        self.CambioTiquete.geometry("450x500")
        title3 = Label(self.CambioTiquete, text="C A M B I A R   T I Q U E T E").place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.08)   
        viaje3 = Label(self.CambioTiquete, text="Escoge un tiquete por el cual cambiarlo ").place(relx=0.05, rely=0.15, relwidth=0.9, relheight=0.08)   
        buscar3 = Button(self.CambioTiquete, text="Volver a pantalla gestionar viajes").place(relx=0.05, rely=0.25, relwidth=0.9, relheight=0.08)   
