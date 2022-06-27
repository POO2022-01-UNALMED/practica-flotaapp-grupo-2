import tkinter as tk
from matplotlib import pyplot as plt
from PIL import Image, ImageTk
from setuptools import Command
from gestorAplicacion.viajes.Ciudad import Ciudad
from gestorAplicacion.viajes.Viaje import Viaje

from gestorAplicacion.personas.Usuario import Usuario
from gestorAplicacion.personas.Empleado import Empleado
from gestorAplicacion.personas.Especialista import Especialista
from gestorAplicacion.personas.Conductor import Conductor

from tkinter import messagebox, ttk
import os
import pathlib
from unittest import TestCase

class GestionarEspecialistas(tk.Frame):
    def __init__(self, window):
        super().__init__(window)
        self._window = window
        self._vTop = tk.Frame(self._window)
        self._vEspecialista = tk.Frame(self._window)
        
        window.title("Gestion Especialista")
        self.valorDefecto = tk.StringVar(value="Seleccione Especialidad")
        self.combo = ttk.Combobox(self, state="readonly",  values=["ELECTRICO", "MECANICO", "SILLETERIA"], textvariable=self.valorDefecto)
        self.combo.place(x=50, y=100, width=500, height=20)
        self.button = ttk.Button(text="Gestionar", command=self.gestionarE())
        self.button.place(relx=0.33, rely=0.4, width=200, height=50)
        window.config(width=600, height=600)
        
        title = tk.Label(self, text="G E S T I O N A R     E S P E C I A L I S T A S").pack(side="top", pady=35)
        
        self.place(width=600, height=600)
    
    def gestionarE(self):
        print("Si entra en gestionar")   
        selection = self.combo.get()
        if selection == "ELECTRICO":  
            print("ELECTRICOS")      
            
        elif selection == "MECANICO":
            print("MECANICOS")
           
        elif selection == "SILLETERIA":
            print("SILLETERIA")


        