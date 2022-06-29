from tkinter import *
from gestorAplicacion.personas.Comprador import Comprador
from gestorAplicacion.personas.Conductor import Conductor
from gestorAplicacion.personas.Especialista import Especialista

class VisualizarCompradores(Frame):
    def __init__(self, window):
        super().__init__(window)
        self._window = window
        
        Label(self, text="V I S U A L I Z A R   C O M P R A D O R E S").pack()
        for comprador in Comprador.getCompradores():
            Label(self, text=f"{comprador.getCc()} - {comprador.getuNombre()} - {comprador.getEmail()} - {comprador.getMovil()}").pack()
        
        self.pack(side="top")

class VisualizarConductores(Frame):
    def __init__(self, window):
        super().__init__(window)
        self._window = window
        
        Label(self, text="V I S U A L I Z A R   C O N D U C T O R E S").pack()
        for conductor in Conductor.getConductores():
            Label(self, text=f"{conductor.getCc()} - {conductor.getuNombre()} - {conductor.getEmail()} - {conductor.getMovil()}").pack()
        
        self.pack(side="top")

class VisualizarEspecialistas(Frame):
    def __init__(self, window):
        super().__init__(window)
        self._window = window
        
        Label(self, text="V I S U A L I Z A R   E S P E C I A L I S T A S").pack()
        for especialista in Especialista.getEspecialistas():
            Label(self, text=f"{especialista.getEspecialidad().value} - {especialista.getCc()} - {especialista.getuNombre()} - {especialista.getEmail()} - {especialista.getMovil()}").pack()
        
        self.pack(side="top")

