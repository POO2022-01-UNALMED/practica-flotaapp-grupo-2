from cProfile import label
from pickle import FRAME
from tkinter import *
from tkinter import messagebox, ttk, simpledialog

from matplotlib.pyplot import text 

from gestorAplicacion.viajes.Ciudad import Ciudad
from gestorAplicacion.viajes.Viaje import Viaje
from gestorAplicacion.personas.Comprador import Comprador
from gestorAplicacion.personas.Conductor import Conductor
from gestorAplicacion.personas.Especialista import Especialista, Especialidad
from gestorAplicacion.viajes.Tiquete import Tiquete
from gestorAplicacion.viajes.Viaje import Viaje
from gestorAplicacion.viajes.Vehiculo import Vehiculo
from uiMain.ventanas.ManejoErrores import ExceptionPopUp, ElecionException, NumericException, IndexException
from uiMain.Funcionalidades.Asignar import Asignar

def color(evento, color):
    evento.widget.config(bg= color)



class GestionarCiudades(Frame):
    """"
    GestionarCiudades: 

    Contiene informacion de:
    - Ciudades

    Su funcionalidad consiste en mostrar las ciudades y sus viajes 
    asignados, los cuales podemos evaluar segun  el  porcentaje de 
    ocupacion o eliminarlos directamente

    """
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
        ciudad = None
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

        try:
            if ciudad == None:
                raise ElecionException("No estas eligiendo una ciudad para Gestionar")
            else:
                Label(self._frame, text= f"Promocion Actual : {ciudad.getPromocion()}        Direccion : {ciudad.getDireccion()}" , font=('Times 12')).place(relx=0.05, rely=0.25, relwidth=0.9, relheight=0.1)
                Label(self._frame, text= f"Puntaje   Actual : {ciudad.getPuntaje()}          Numero Visitantes : {ciudad.getNumVisitantes()}" , font=('Times 12')).place(relx=0.05, rely=0.35, relwidth=0.9, relheight=0.1)
        
        except ElecionException as p:
            ExceptionPopUp("Seleccione una Ciudad para Gestionar")
            p.mostrarMensaje()

            

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
        try:
            if self.comboViaje.get() == "Seleccione Viaje":
                raise ElecionException("No estas eligiendo un Viaje para Eliminar")
            else:
                viaje = Viaje.getViajes()[int(self.comboViaje.get())]
                viaje.eliminarViaje()
                self._frameViaje.destroy()
                self.ventanaGestionar()
        except ElecionException as p:
            ExceptionPopUp("Seleccione una Ciudad para Eliminar")
            p.mostrarMensaje()
    
    def EvaluarViaje(self):
        promocionar = None
        porcentaje = -1
        try:
            if self.comboViaje.get() == "Seleccione Viaje":
                raise ElecionException("No estas eligiendo un Viaje para Evaluar")
            else:
                promocionar = Viaje.getViajes()[int(self.comboViaje.get())]
                porcentaje = ((len(promocionar.getVehiculo().getSillas()) - len(promocionar.tiquetesDisponibles()))*100)/len(promocionar.getVehiculo().getSillas())

        except ElecionException as p:
            ExceptionPopUp("Seleccione un Viaje para Evaluar")
            p.mostrarMensaje()

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
                try:
                    if res.isdigit():
                        promocionar.getDestino().setPromocion(int(res))
                        promocionar.getOrigen().setPromocion(int(res))
                        messagebox.showinfo(title = "Promocion de Viaje", message = "El viaje a sido promocionado")
                    else:
                        raise NumericException()
                except NumericException as p:
                    ExceptionPopUp("Ingrese valores Numericos")
                    p.mostrarMensaje()

        elif (porcentaje >= 20 and porcentaje < 45):
            promocionar.disminuirFrecuencia(2)
            message = f"Porcentaje Ocupacion = {porcentaje}\nLa frecuencia del viaje se a disminuido en dos hora"
            messagebox.showinfo(title = "Promocion de Viaje", message = message)
        
        elif(porcentaje < 20 and porcentaje >= 0):
            message = f"Porcentaje Ocupacion = {porcentaje}\n¿Desea Eliminar el viaje?"
            des = messagebox.askyesno(title = "Promocion de Viaje", message = message)
            if des == True:
                self.ElimarViaje()

        


    def MatarTodo(self, frameUsado):
        for frame in self.winfo_children():
            frame.pack_forget()
        frameUsado.pack(fill=BOTH,expand=True)

class GestionarViajes(Frame):
    """"
    GestionarViajes: 

    Contiene informacion de:
    - Viajes
    - Tiquetes
    - Compradores

    Su funcionalidad consiste en mostrar los viajes que el 
    comprador tiene asignados y observar si quiere cambiarlo o cancelarlo

    """

    def __init__(self, window):
        super().__init__(window)
        self._vTop = Frame(self)
        self.entrada = StringVar(value= Comprador.getCompradores()[0].getCc())

        title = Label(self, text="G E S T I O N A R   V I A J E S").place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.08) 
        viaje = Label(self, text="Gestionar viaje con la cédula: ").place(relx=0.05, rely=0.15, relwidth=0.3, relheight=0.08) 
        info = Entry(self, borderwidth=2, textvariable = self.entrada).place(relx=0.32, rely=0.15, relwidth=0.45, relheight=0.08) 
        buscar = Button(self, text="Buscar", command= self.FrameComprador ).place(relx=0.75, rely=0.15, relwidth=0.15, relheight=0.08) 


    def FrameComprador(self):
        valor = Comprador.getCompradores()[0].getCc()
        try:
            if self.entrada.get().isdigit() and self.entrada.get() != "0":
                valor = int(self.entrada.get())

                self._vTop.destroy()
                self._vTop = Frame(self)

                listaTiquete = []
                compradorTiquete = Comprador()
                for comprador in Comprador.getCompradores():
                    if comprador.getCc() == valor:
                        if comprador.getHistorioViaje() != []:
                            listaTiquete = Tiquete.buscarTiquete(comprador.getHistorioViaje()[0].getId()).getComprador().getHistorioViaje()
                            listaTiquete = [f"{t.getId()} - {t.getViaje()} - {t.getSillaTiquete()}" for t in listaTiquete]
                        compradorTiquete = comprador
                        

                Label(self._vTop, text= f"CC: {compradorTiquete.getCc()} - Nombre : {compradorTiquete.getuNombre()}").place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.08)
                self.valorDefectoTiquete = StringVar(value="Seleccione Viaje")
                self.comboTiquete = ttk.Combobox(self._vTop, state="readonly",  values= listaTiquete, textvariable=self.valorDefectoTiquete, width=15)
                self.comboTiquete.place(relx=0.05, rely=0.15, relwidth=0.7, relheight=0.08)
                buscarTiquetes = Button(self._vTop, text="Gestionar", command= self.FrameTiquete)
                buscarTiquetes.place(relx=0.75, rely=0.15, relwidth=0.2, relheight=0.08)    

                self._vTop.place(relx=0.05, rely=0.25, relwidth=0.9, relheight=0.7) 

                self._frameInfoTiquete = Frame(self._vTop)
            else:
                raise NumericException()
        except NumericException as p:
            ExceptionPopUp("Ingrese un valor Numerico Valido")
            p.mostrarMensaje()



    def FrameTiquete(self):
        
        self._frameInfoTiquete.destroy()
        self._frameInfoTiquete = Frame(self._vTop)
        try:
            if self.comboTiquete.get()[:2].isdigit():
                self.tiquete = Tiquete.buscarTiquete(int(self.comboTiquete.get()[:2]))
            else:
                raise ElecionException("No esta eligiendo un viabe a gestionar")
        except ElecionException as p:
            ExceptionPopUp("Seleccione un Viaje del Comprador para Gestionar")
            p.mostrarMensaje()

        Label(self._frameInfoTiquete,  text= f"Silla = {self.tiquete.getSillaTiquete()}").pack()
        Label(self._frameInfoTiquete,  text= f"Viaje = {self.tiquete.getViaje()}").pack()
        Label(self._frameInfoTiquete,  text= f"Valor = {self.tiquete.getValor()} Fecha = {self.tiquete.getFechaCompra()}").pack()

        self._frameInfoTiquete.place(relx=0.05, rely=0.25, relwidth=0.9, relheight=0.20) 
        
        def cancelarTiquete():
            self.tiquete.getComprador().eliminarTiqueteHistoria(self.tiquete)
            self.tiquete.setEstado(False)
            aux = messagebox.showinfo(title = "Gestionar Viaje", message = "Viaje Cancelado")   
            if aux:
                self.FrameComprador()


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
        
        def cambiarTiquete():
            try:
                if self.tiqueteCambiado.get().isdigit():
                    tiqueteCambio = self.listaDisponibles[int(self.tiqueteCambiado.get())]
                else:
                    tiqueteCambio = None
                    ElecionException("No esta eligiendo un Tiquete para el Cambio")
            except ElecionException as p:
                ExceptionPopUp("Seleccione el una opcion para Cambiar su Tiquete")
                p.mostrarMensaje()


            self.tiquete.getComprador().anadirTiqueteHistoria(tiqueteCambio)
            self.tiquete.getComprador().eliminarTiqueteHistoria(self.tiquete)
            self.tiquete.setEstado(False)
            self.CambioTiquete.destroy()
            self.FrameComprador()

        self.CambioTiquete = Toplevel(self)
        self.CambioTiquete.geometry("550x600")
        self.tiqueteCambiado = StringVar()
        Label(self.CambioTiquete, text="C A M B I A R   T I Q U E T E").place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.08)   
        Label(self.CambioTiquete, text="Escoge un tiquete por el cual cambiarlo ").place(relx=0.05, rely=0.15, relwidth=0.9, relheight=0.08)   
        cambiar = Button(self.CambioTiquete, text="Cambiar Tiquete", command= cambiarTiquete).place(relx=0.05, rely=0.25, relwidth=0.9, relheight=0.08)   

        self.listaDisponibles = [t for t in Tiquete.getTiquetes() if t.getViaje().getDestino() == self.tiquete.getViaje().getDestino() and t.getViaje().getOrigen() == self.tiquete.getViaje().getOrigen() and t.getViaje().getFechaViaje() >= self.tiquete.getViaje().getFechaViaje()]
        contador2 = 0
        frameCambio = Frame(self.CambioTiquete)
        for x in range(len(self.listaDisponibles)):
            mostar = Radiobutton(frameCambio, text= self.listaDisponibles[x], variable=self.tiqueteCambiado, value=contador2).pack()  
            contador2 +=1 
        
        frameCambio.place(relx=0.05, rely=0.35, relwidth=0.9, relheight=0.6)   

class GestionarConductor(Frame):
    """
    GestionarConductor: 
    
    Contiene informacion de:
    - Conductores

    Su funcionalidad consiste en poder mostrar los viajes asignados, 
    despedir  un  conductor o  asignar un viaje  a  los  conductores 
    disponibles

    """
    def __init__(self, window):
        super().__init__(window)
        self._window = window
        self._vCond = Frame(self)
        
        title = Label(self, text="G E S T I O N A R   C O N D U C T O R E S").place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.1)  
        self.ccConductor = [ conduc.getCc() for conduc in Conductor.getConductores()]
            
        self.valorDefecto = StringVar(value= Conductor.getConductores()[0].getCc())
        self.comboC = ttk.Combobox(self,  state="readonly", values=self.ccConductor, textvariable=self.valorDefecto).place(relx=0.05, rely=0.15, relwidth=0.1, relheight=0.08)  
        self.nombreConductor = Label(self, text = Conductor.buscarConductor(int(self.valorDefecto.get())).getuNombre() ).place(relx=0.15, rely=0.15, relwidth=0.5, relheight=0.1)  
        Button(self, text="Gestionar Conductor", command= self.botonesGestion).place(relx=0.65, rely=0.15, relwidth=0.3, relheight=0.08)  
        
    def infoConductor(self):
        self._vCond.destroy()
        self._vCond = Frame(self)
        for viaje in Conductor.buscarConductor(int(self.valorDefecto.get())).getHistoricoViajesRealizados():
            Label(self._vCond, text= f" Viaje = {viaje}").pack()
        
        self._vCond.place(relx=0.05, rely=0.4, relwidth=0.9, relheight=0.65) 

    def botonesGestion(self):
        self.nombreConductor = Label(self, text = Conductor.buscarConductor(int(self.valorDefecto.get())).getuNombre() ).place(relx=0.15, rely=0.15, relwidth=0.5, relheight=0.1)    
        historicoR = Button(self, text="Viajes Asignados", command= self.infoConductor ).place(relx=0.05, rely=0.3, relwidth=0.3, relheight=0.08)
        despedirE = Button(self, text="Despedir", command= self.despedir).place(relx=0.35, rely=0.3, relwidth=0.3, relheight=0.08)
        asignarV = Button(self, text="Asignar Viaje", command= self.asignarViaje).place(relx=0.65, rely=0.3, relwidth=0.3, relheight=0.08)

    def despedir(self):
        for espC in Conductor.getConductores():
            if int(self.valorDefecto.get()) == int(espC.getCc()):
                Conductor.getConductores().remove(espC)
                self.valorDefecto = StringVar(value= Conductor.getConductores()[0].getCc())
                self.ccConductor = [ conduc.getCc() for conduc in Conductor.getConductores()]
                self.comboC = ttk.Combobox(self,  state="readonly", values=self.ccConductor, textvariable=self.valorDefecto).place(relx=0.05, rely=0.15, relwidth=0.1, relheight=0.08)  
                messagebox.showinfo("Despedir", f"Conductor {espC.getuNombre()} despedido")  

        for frame in self.winfo_children():
            frame.pack_forget()
        
            
    def asignarViaje(self):
        self.newViaje = Toplevel(self)
        self.newViaje.geometry("300x150")
        try:
            if self.valorDefecto.get().isdigit():
                for espC in Conductor.getConductores():
                    if int(self.valorDefecto.get()) == int(espC.getCc()):
                        indice = 0
                        for vehi in Viaje.viajeSinConductor():
                            cadaV = Label(self.newViaje, text=f"id: {indice} - Viaje: {vehi}").pack()
                            indice+=1
                        
                        self.vAsignar = Entry(self.newViaje)  
                        aVasignarBot = Button(self.newViaje, text="Asignar Viaje", command=lambda: self.asignarVE(espC))#command=lambda: self.asignarVE(espC, int(vAsignar.get()))).pack(side="top")
                        
                        self.vAsignar .pack()
                        aVasignarBot.pack()
            else:
                raise ElecionException
        except ElecionException as p:
            p.mostrarMensaje()

    
    def asignarVE(self, espcialista):
        indxVehiculo = 0
        try:
            if self.vAsignar.get().isdigit():
                if int(self.vAsignar.get()) < len(Viaje.viajeSinConductor()):
                    messagebox.showinfo("Confirmacion", f"Se ha asignado  {Viaje.viajeSinConductor()[indxVehiculo]} con exito")
                    Asignar.asignarVehiculoConductor(espcialista, Viaje.viajeSinConductor()[indxVehiculo])
                    self.newViaje.destroy()
                else:
                    raise IndexException()
            else:
                raise NumericException()
        except NumericException as p:
            ExceptionPopUp("Ingrese valores Numericos")
            p.mostrarMensaje()
        except IndexException as p:
            ExceptionPopUp("Ingrese un ID correcto")
            p.mostrarMensaje()

        
    

    def MatarTodo(self, frameUsado):
        for frame in self.winfo_children():
            frame.pack_forget()
        frameUsado.pack(fill=BOTH,expand=True)  
             
class GestionarEspecialistas(Frame):
    """"
    GestionarEspecialista: 

    Contiene informacion de:
    - Especialistas

    Su funcionalidad consiste en poder mostrar los vehiculos
    asignados,  despedir  un  especialista   o   asignar  un 
    vehiculo para revisión del especialista 

    """
    def __init__(self, window):
        super().__init__(window)
        self._window = window
        self._vTop = Frame(self)
        self.MatarTodo(self._vTop)
        
        self._frameE = Frame(self._vTop)
        
        self._vEspecialista = Frame(self._window)
        
        self.valorDefecto = StringVar(value="Seleccione Especialidad")
        self.combo = ttk.Combobox(self, state="readonly", values=["ELECTRICO", "MECANICO", "SILLETERIA"], textvariable=self.valorDefecto)
        bGestionar = Button(self, text="Fijar", command= self.gestionarE)
        

        self.combo.place(relx=0.2, rely=0.2, relwidth=0.5, relheight=0.08)
        bGestionar.place(relx=0.725, rely=0.2, relwidth=0.1, relheight=0.08)
        
        self._vTop.place(relx=0, rely=0, relwidth=1, relheight=1)
        
        title = Label(self, text="G E S T I O N A R     E S P E C I A L I S T A S").place(relx=0.25, rely=0.05, relwidth=0.5, relheight=0.1)
        
        
    def gestionarE(self):
        self._frameE.destroy()
        self._frameE = Frame(self._vTop)
        especialistasSelect = []
        selection = str(self.combo.get())
        try:
            if selection == "Seleccione Especialidad":
                    raise ElecionException("No esta eligiendo una Especialidad") 
            else: 
                for espc in Especialista().getEspecialistas():
                    if espc.getEspecialidad().value == selection:
                        especialistasSelect.append(f"{espc.getCc()} - {espc.getuNombre()}") 
        except   ElecionException as p:
            p.mostrarMensaje()   



        
        self.valordefectoEmp = StringVar(value="CC")
        self.comboEmp = ttk.Combobox(self, state="readonly", values=especialistasSelect, textvariable=self.valordefectoEmp)
        self.gestCC = Button(self, text="Gestionar",command=self.ventanaGestionar)
          
        self.comboEmp.place(relx=0.2, rely=0.3, relwidth=0.5, relheight=0.08)
        self.gestCC.place(relx=0.725, rely=0.3, relwidth=0.1, relheight=0.08)

        self._frameE.place(relx=0.07, rely=0.35, relwidth=0.9, relheight=0.4)
        
     
            
    def ventanaGestionar(self):
        try:
            if self.comboEmp.get().isdigit():
                ccAgestionar = self.comboEmp.get()
            else:
                raise ElecionException("No esta escogiendo un Especialista a gestionar")
        except ElecionException as p:
            p.mostrarMensaje() 
        
        self._vTop = Frame(self._window)

        historicoR = Button(self, text="Revisados", command= self.visualizarHistorialViajesAsignados).place(relx=0.05, rely=0.4, relwidth=0.3, relheight=0.08)
        despedirE = Button(self, text="Despedir", command=  self.despedir).place(relx=0.35, rely=0.4, relwidth=0.3, relheight=0.08)
        asignarV = Button(self, text="Asignar Viaje", command=lambda: self.asignarViaje).place(relx=0.65, rely=0.4, relwidth=0.3, relheight=0.08)
                
    
    def visualizarHistorialViajesAsignados(self):
        gHistoricoRevisados = [] 
        cc = 0
        try:
            if self.comboEmp.get().isdigit():
                cc = self.comboEmp.get()
            else:
                raise ElecionException("No esta escogiendo un Especialista para ver sus viajes")
        except ElecionException as p:
            p.mostrarMensaje() 

        for espC in Especialista.getEspecialistas(): # Se busca el especialista seleccionado en el combobox, y se itera la lista de vehiculos revisados para traer sus placas
            if int(cc) == int(espC.getCc()):
                if  espC.getHistoricoVehiculosRevisados() != []:
                    for vehi in espC.getHistoricoVehiculosRevisados():
                        gHistoricoRevisados.append(vehi.getPlaca())
                
        Label(self, text=f"Vehiculos revisados: {gHistoricoRevisados}").place(relx=0.05, rely=0.5, relwidth=0.9, relheight=0.2)
     
            
    def despedir(self):
        cc = 0
        try:
            if self.comboEmp.get().isdigit():
                cc = self.comboEmp.get()
            else:
                raise ElecionException("No esta escogiendo un Especialista para Despedir")
        except ElecionException as p:
            p.mostrarMensaje() 

        for espC in Especialista.getEspecialistas():
            if int(cc) == int(espC.getCc()):
                Especialista.getEspecialistas().remove(espC)
                messagebox.showinfo("Despedir", f"Especialista {espC.getuNombre()} despedido")
        self.gestionarE()
                
            
    def asignarViaje(self, cc):
        self.newViaje = Toplevel(self)
        self.newViaje.geometry("300x150")
        for espC in Especialista.getEspecialistas():
            if int(cc) == int(espC.getCc()):
                indice = 0
                for vehi in Vehiculo.getVehiculos():
                    cadaV = Label(self.newViaje, text=f"id: {indice} - Placa: {vehi.getPlaca()}").pack(side="top")
                    indice+=1
                
                vAsignar = Entry(self.newViaje)
                
                aVasignarBot = Button(self.newViaje, text="Asignar Vehiculo", command=lambda: self.asignarVE(espC, int(vAsignar.get())))#command=lambda: self.asignarVE(espC, int(vAsignar.get()))).pack(side="top")
                
                vAsignar.pack(side="top")
                aVasignarBot.pack(side="top")
                # por que el vAsignar.get() no me trae la entrada


    def asignarVE(self, espcialista, indxVehiculo):
        
        Asignar.asignarVehiculoEspecialista(espcialista, Vehiculo.getVehiculos()[indxVehiculo])
        espcialista.revisionVehiculo(Vehiculo.getVehiculos()[indxVehiculo])
        messagebox.showinfo("Confirmacion", f"Se ha asignado  {Vehiculo.getVehiculos()[indxVehiculo].getPlaca()} con exito")

        

    def MatarTodo(self, frameUsado):
        for frame in self.winfo_children():
            frame.pack_forget()
        frameUsado.pack(fill=BOTH,expand=True)