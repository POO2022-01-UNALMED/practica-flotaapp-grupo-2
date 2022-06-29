import tkinter as tk
from matplotlib import pyplot as plt
from PIL import Image, ImageTk
from setuptools import Command

from gestorAplicacion.viajes.Ciudad import Ciudad
from gestorAplicacion.viajes.Viaje import Viaje
from gestorAplicacion.viajes.Vehiculo import Vehiculo

from gestorAplicacion.personas.Usuario import Usuario
from gestorAplicacion.personas.Empleado import Empleado
from gestorAplicacion.personas.Especialista import Especialista, Especialidad
from gestorAplicacion.personas.Conductor import Conductor

from uiMain.Funcionalidades.Asignar import Asignar

from tkinter import messagebox, ttk
from tkinter import *

class GestionarConductor(Frame):
    def __init__(self, window):
        super().__init__(window)
        self._window = window
        self._vTop = Frame(self)
        self.MatarTodo(self._vTop)
        self._frameE = Frame(self._vTop)
        self._vConductor = tk.Frame(self._window)
        
        title = tk.Label(self._vTop, text="G E S T I O N A R   C O N D U C T O R E S").place(relx=0.35, rely=0.01)
        
        for conduc in Conductor.getConductores():
            tk.Label(self._vTop, text=f"{conduc.__str__()}").place(relx=0.4, rely=0.5)
            
            
        self.valorDefecto = tk.StringVar(value="Seleccione Especialidad")
        comboC = ttk.Combobox(self,  state="readonly", values=[conductor.getCc() for conductor in Conductor.getConductores()], textvariable=self.valorDefecto).place(relx=0.4, rely=0.25)
        
        self._vTop.place()
    
    
    
    
    
    def MatarTodo(self, frameUsado):
        for frame in self.winfo_children():
            frame.pack_forget()
        frameUsado.pack(fill=BOTH,expand=True)
            


