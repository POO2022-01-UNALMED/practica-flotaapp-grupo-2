from tkinter import *
from uiMain.ventanas.Gestionar import GestionarCiudades, GestionarViajes
from uiMain.ventanas.VisualizarEstadistica import VisualizarEstadistica
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
            Label(top, text= "AUTORES:\nMateo Echavarria Sierra", font=('Times 18 bold')).pack(fill=BOTH, expand=True)

        def aplicacion_popup():
            top= Toplevel(self)
            top.geometry("580x320")
            top.resizable(False,False)
            top.title("Aplicación")
            Label(top, text= textonimo , font=('Times 12')).pack(fill=BOTH, expand=True)
        textonimo = "Flota-APP es una empresa............."

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

        menuprocesos.add_command(label = "Visualizar Estadisticas", command = self.visualizarEstadisticas)
        menuprocesos.add_command(label = "Gestionar Ciudades", command = self.gestionarCiudades)
        menuprocesos.add_command(label = "Gestionar Viajes", command = self.gestionarViajes)

        menuayuda.add_command(label = "Acerca de", command = open_popup)

        frameUso = Frame(self)

        self['menu'] = menubar

    def visualizarEstadisticas(self):
        vsE = VisualizarEstadistica(self)
        self.MatarTodo(vsE)
    
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
    