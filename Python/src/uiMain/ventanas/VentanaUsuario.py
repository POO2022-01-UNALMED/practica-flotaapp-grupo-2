from tkinter import *
from uiMain.ventanas.Gestionar import GestionarCiudades, GestionarViajes
from uiMain.ventanas.Inicio import Inicio
from uiMain.ventanas.VisualizarEstadistica import VisualizarEstadistica
from uiMain.ventanas.VisualizacionLista import VisualizarCompradores, VisualizarConductores, VisualizarEspecialistas
from uiMain.ventanas.ComprarTiquete import ComprarTiquete
from baseDatos.serializador import Serializador

class VentanaUsuario(Tk):
    def __init__(self) :
        super().__init__()
        self.geometry("680x440")
        self.title("Flota-APP")
        self.option_add("*tearOff",  FALSE)


        def open_popup():
            top= Toplevel(self)
            top.grid_rowconfigure(0, weight=1)
            top.geometry("450x250")
            top.resizable(False,False)
            top.title("Ayuda")
            Label(top, text= "AUTORES:\nMateo Echavarria Sierra\nMiguel Angel Fonseca Aldana\nJuan Pablo Pineda Lopera\nHaison Urrutia Manyoma", font=('Times 18 bold')).pack(fill=BOTH, expand=True)

        def aplicacion_popup():
            top= Toplevel(self)
            top.geometry("580x320")
            top.resizable(False,False)
            top.title("Aplicación")
            Label(top, text= textonimo , font=('Times 12')).pack(fill=BOTH, expand=True)
        textonimo = """Estimado usuario, bienvenido a FlotaAPP. 
Somos una APP que gestiona los diferentes servicios de una flota 
de autobuses con diferentes funcionalidades como:  automatizar la 
compra de tiquetes, la ocupación y disponibilidad de viajes, 
guardar registros de sus viajes e implementar recomendaciones 
personalizadas en cada usuario y desarrollar las distintas 
estadísticas por ciudad y por viaje. Todo esto, con el objetivo de 
facilitar y mejorar la calidad del tedioso proceso de organizar un viaje."""

        def salir():
            Serializador.serializar()
            from uiMain.ventanas.ventanaInicio.Inicio import VentanaInicio
            framesAMatar = []
            self.destroy()
            ventana = VentanaInicio()
            ventana.mainloop()
       
        #Barra menu superior
        menubar = Menu()
        menuarchivo = Menu(self)
        menuprocesos = Menu(self)
        menuayuda = Menu(self)
        
        menubar.add_cascade(menu = menuarchivo,
                            label='Archivo')
        menubar.add_cascade(menu = menuprocesos,
                            label = 'Procesos y Consultas')
        menubar.add_cascade(menu = menuayuda,
                            label='Ayuda')

        #submenu de procesos y consultas
        submenu = Menu(self)

        menuarchivo.add_command(label = "Aplicacion", command = aplicacion_popup)
        menuarchivo.add_command(label = "Guardar y salir", command = salir)
        
        menuprocesos.add_cascade(label = "Visualizaciones", menu = submenu)

        submenu.add_command(label = "Visualizar Estadisticas", command = self.visualizarEstadisticas)
        submenu.add_command(label = "Visualizar Compradores", command = self.visualizarCompradores)
        submenu.add_command(label = "Visualizar Conductores", command = self.visualizarConductores)
        submenu.add_command(label = "Visualizar Especialistas", command = self.visualizarEspecialistas)

        menuprocesos.add_command(label = "Gestionar Ciudades", command = self.gestionarCiudades)
        menuprocesos.add_command(label = "Gestionar Viajes", command = self.gestionarViajes)
        menuprocesos.add_command(label = "Comprar Tiquete", command = self.comprarTiquete)

        menuayuda.add_command(label = "Acerca de", command = open_popup)

        frameUso = Frame(self)
        interfazInicio = Inicio(self)
        interfazInicio.pack()

        self['menu'] = menubar

    def visualizarEstadisticas(self):
        vsE = VisualizarEstadistica(self)
        self.MatarTodo(vsE)
    
    def visualizarCompradores(self):
        vsC = VisualizarCompradores(self)
        self.MatarTodo(vsC)
    
    def visualizarConductores(self):
        vsC = VisualizarConductores(self)
        self.MatarTodo(vsC)
    
    def visualizarEspecialistas(self):
        vsE = VisualizarEspecialistas(self)
        self.MatarTodo(vsE)
    
    def comprarTiquete(self):
        coT = ComprarTiquete(self)
        self.MatarTodo(coT)
    
    def gestionarCiudades(self):
        gesC = GestionarCiudades(self)
        self.MatarTodo(gesC)
    
    def gestionarViajes(self):
        gesV = GestionarViajes(self)
        self.MatarTodo(gesV)
    
    def MatarTodo(self, frameUsado):
        for frame in self.winfo_children():
            frame.pack_forget()
        frameUsado.pack(fill=BOTH,expand=True)
    