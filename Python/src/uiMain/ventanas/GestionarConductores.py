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
        
        title = tk.Label(self._vTop, text="G E S T I O N A R   CONDUCTORES").grid(row=0, column=1,pady=10)
        ccConductor = []
        for conduc in Conductor.getConductores():
            tk.Label(self._vTop, text=f"{conduc.__str__()}").grid()
            ccConductor.append(conduc.getCc())
            
        self.valorDefecto = tk.StringVar(value="Seleccione Especialidad")
        comboC = ttk.Combobox(self._vTop,  state="readonly", values=ccConductor, textvariable=self.valorDefecto).grid()
        
        self._vTop.grid()        


