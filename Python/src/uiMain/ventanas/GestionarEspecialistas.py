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

from tkinter import messagebox, ttk
from tkinter import *


class GestionarEspecialistas(Frame):
    def __init__(self, window):
        super().__init__(window)
        self._window = window
        self._vTop = Frame(self)
        self.MatarTodo(self._vTop)
        
        self._frameE = Frame(self._vTop)
        
        self._vEspecialista = tk.Frame(self._window)
        
        self.valorDefecto = tk.StringVar(value="Seleccione Especialidad")
        self.combo = ttk.Combobox(self, state="readonly", values=["ELECTRICO", "MECANICO", "SILLETERIA"], textvariable=self.valorDefecto)
        bGestionar = tk.Button(self._vTop, text="Gestionar", command= self.gestionarE)
        

        self.combo.place(relx=0.2, rely=0.2, relwidth=0.5, relheight=0.08)
        bGestionar.place(relx=0.725, rely=0.2, relwidth=0.1, relheight=0.08)
        
        self._vTop.place(relx=0, rely=0, relwidth=1, relheight=1)
        
        title = tk.Label(self._vTop, text="G E S T I O N A R     E S P E C I A L I S T A S").place(relx=0.25, rely=0.05, relwidth=0.5, relheight=0.1)
        """
        bElectrico = tk.Button(self._vTop, text="ELECTRICO", command=self.gestionarE).grid(row=4, column=0 , columnspan=2, pady=20, padx=10)
        bMecanico = tk.Button(self._vTop, text="MECANICO", command=self.gestionarM).grid(row=4, column=1 , columnspan=2, pady=20, padx=10)
        bSilleteria = tk.Button(self._vTop, text="SILLETERIA", command=self.gestionarS).grid(row=4, column=2 , columnspan=2, pady=20, padx=10)
        
        """
        
        
    def gestionarE(self):
        self._frameE.destroy()
        self._frameE = Frame(self._vTop)
        ccEspecialistas = []
        selection = str(self.combo.get())
        if selection == "MECANICO":
            for espc in Especialista().getEspecialistas():
                if espc.getEspecialidad() == Especialidad.MECANICO:
                    tk.Label(self._frameE, text={espc.__str__()}).pack()
                    tk.Button(self._frameE, text=f"Gestionar : {espc.getCc}").pack()
                    ccEspecialistas.append(espc.getCc())
                    
                    
                    
                    print(espc.getEspecialidad())
                
            print("entra en Mecanico")
            
        elif selection == "ELECTRICO":
            for espc in Especialista().getEspecialistas():
                if espc.getEspecialidad() == Especialidad.ELECTRICO:
                    tk.Label(self._frameE, text={espc.__str__()}).pack()
                    #tk.Button(self._frameE, text=f"Gestionar : {espc.getCc()}").pack()
                    ccEspecialistas.append(espc.getCc())
            
                    
                    
            print("Entra en Electrico")
            
        elif selection == "SILLETERIA":
            for espc in Especialista().getEspecialistas():
                if espc.getEspecialidad() == Especialidad.SILLETERIA:
                    tk.Label(self._frameE, text={espc.__str__()}).pack()
                    ccEspecialistas.append(espc.getCc())
                    
                    
            print("Entra Silletria")
        
        self.valordefectoEmp = StringVar(value="CC")
        self.comboEmp = ttk.Combobox(self, state="readonly", values=ccEspecialistas, textvariable=self.valordefectoEmp)
        self.gestCC = tk.Button(self, text="Gestionar CC",command=self.ventanaGestionar)
          
        self.comboEmp.place(relx=0.05, rely=0.2, relwidth=0.1, relheight=0.05)
        self.gestCC.place(relx=0.005, rely=0.5, relwidth=0.2, relheight=0.1)
        self._frameE.place(relx=0.07, rely=0.35, relwidth=0.9, relheight=0.5)
        
     
            
    def ventanaGestionar(self):
        ccAgestionar = self.comboEmp.get()
        print(ccAgestionar)
        self.combo.destroy()
        self._window.geometry("640x480")
        self._vEspecialista.destroy()
        self._vTop.destroy()
        self._vEspecialista = tk.Frame(self._window)
        historicoR = tk.Button(self._vEspecialista, text="Revisados", command=self.visualizarHistorialViajesAsignados(ccAgestionar)).pack(side="top") #mirar porque se ejecuta automatico
        despedirE = tk.Button(self._vEspecialista, text="Despedir", command=self.despedir(int(ccAgestionar))).pack(side="top")
        self._vEspecialista.pack(side="top")
        
    
    def visualizarHistorialViajesAsignados(self, cc):
        gHistoricoRevisados = [] 
        for espC in Especialista.getEspecialistas(): # Se busca el especialista seleccionado en el combobox, y se itera la lista de vehiculos revisados para traer sus placas
            print("entra en el for") #eliminar
            if int(cc) == int(espC.getCc()):
                for vehi in espC.getHistoricoVehiculosRevisados():
                    print("entra en el for mas interno")
                    gHistoricoRevisados.append(vehi.getPlaca())
                break
        print(gHistoricoRevisados) #eliminar pront 
        print("entra al historico")# eliminar print
            
    def despedir(self, cc):
        for espC in Especialista.getEspecialistas():
            print([ced.getCc() for ced in Especialista.getEspecialistas()])
            if int(cc) == int(espC.getCc()):
                print("entra en el if")
                Especialista.getEspecialistas().remove(espC)
                pamir = [ced.getCc() for ced in Especialista.getEspecialistas()]
                print(pamir)
            
        
        
    def MatarTodo(self, frameUsado):
        for frame in self.winfo_children():
            frame.pack_forget()
        frameUsado.pack(fill=BOTH,expand=True)
        