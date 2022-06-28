from uiMain.ventanas.field_frame import FieldFrame
from uiMain.ventanas.Inicio import Inicio
from uiMain.ventanas.VisualizarEstadistica import VisualizarEstadistica
from uiMain.ventanas.GestionarEspecialistas import GestionarEspecialistas
from uiMain.ventanas.GestionarConductores import GestionarConductor
from baseDatos.serializador import Serializador
from gestorAplicacion.personas.Especialista import Especialista, Especialidad
from gestorAplicacion.personas.Comprador import Comprador

from ctypes import resize
from tkinter import *
from numpy import diag
from random import choice, random, randint
from tkinter import messagebox, ttk

from uiMain.ventanas.ManejoErrores import ErrorAplicacion, ExceptionPopUp, ClientIncorrectoException


if len(Especialista.getEspecialistas()) == 0:
    dependiente = Especialista(7, "Mateo Echavarria Sierra", "maechavarrias@unal.edu.co", 0, 0, Especialidad.ADMINISTRADOR)
    tecnico = Especialista(27, "Jose", "emailMecanico1@example.com", 3224568585, 3500, Especialidad.MECANICO)
    tecnico2 = Especialista(78, "Maria", "emailElectrico1@example.com", 3224567585, 4000, Especialidad.ELECTRICO)
        

def outPut(string, text):
    text.delete("1.0", "end")
    text.insert(INSERT, string)
    text.pack(fill=X, expand=True)



def iniciar_ventana_usuario():
    #Ventana principal
    window = Tk()
    window.geometry("680x440")
    window.title("Flota-APP")
    window.option_add("*tearOff",  FALSE)


    #Métodos sin argumentos para poder ejecutarlos-------------------------------------


    framesAMatar = []

    def matarloTodo(frameUtilizado):

        for frame in framesAMatar:
            frame.pack_forget()
        frameUtilizado.pack(fill=BOTH,expand=True)

    
    def visualizarEstadisticas():
        vEstadistica = VisualizarEstadistica(window)
        vEstadistica.pack()
        matarloTodo(vEstadistica)
    
    def gestionarEspecialistas():
        vEspecialista = GestionarEspecialistas(window)
        vEspecialista.pack()
        matarloTodo(vEspecialista)
    
    def gestionarConductor():
        vConductor = gestionarConductor(window)
        vConductor.pack()
        matarloTodo(vConductor)
        
    

    #Abre la pestana de dialogo con los nombres de los integrantes del equipo
    def open_popup():
        top= Toplevel(window)
        top.grid_rowconfigure(0, weight=1)
        top.geometry("450x250")
        top.resizable(False,False)
        top.title("Ayuda")
        Label(top, text= """AUTORES:
        Mateo Echavarria Sierra

""", font=('Times 18 bold')).pack(fill=BOTH, expand=True)

    #Abre la pestana de dialogo con la informacion del programa y su funcionalidad. 
    def aplicacion_popup():
        top= Toplevel(window)
        top.geometry("580x320")
        top.resizable(False,False)
        top.title("Aplicación")
        Label(top, text= textonimo , font=('Times 12')).pack(fill=BOTH, expand=True)
    textonimo = "Flota-APP es una empresa............."


    #----------------------------------------------------------------------------------
    def salir():
        Serializador.serializar()
        from uiMain.ventanas.ventanaInicio.Inicio import VentanaInicio
        framesAMatar = []
        window.destroy()
        ventana = VentanaInicio()
        ventana.mainloop()
        
    def evento():
        pass

    frame_a = Frame()#master = window
    
    frame_a.pack()
    #Barra menu superior
    menubar = Menu()

    menuarchivo = Menu(window)
    menuprocesos = Menu(window)
    menuayuda = Menu(window)
    

    menubar.add_cascade(menu = menuarchivo,
                        label='Archivo',
                        command = evento)
    menubar.add_cascade(menu = menuprocesos,
                        label = 'Procesos y Consultas',
                        command = evento)
    menubar.add_cascade(menu = menuayuda,
                        label='Ayuda',
                        command = evento)

    #submenu de procesos y consultas
    submenu = Menu(window)

    menuarchivo.add_command(label = "Aplicacion", command = aplicacion_popup)
    menuarchivo.add_command(label = "Guardar y salir", command = salir)


    menuprocesos.add_command(label = "Visualizar Estadisticas", command = visualizarEstadisticas)
    ####
    menuprocesos.add_command(label = "Gestionar Especialistas", command = gestionarEspecialistas)
    menuprocesos.add_command(label = "Gestionar Conductores", command = gestionarConductor)

    menuayuda.add_command(label = "Acerca de", command = open_popup)

    window['menu'] = menubar


    #Interfaz de inicio----------------------------------------------------------------
    interfazInicio = Inicio(window)

    framesAMatar.append(interfazInicio)
    #----------------------------------------------------------------------------------


    