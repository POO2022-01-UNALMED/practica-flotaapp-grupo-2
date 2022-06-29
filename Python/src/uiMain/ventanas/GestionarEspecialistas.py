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



""""
GestionarConductor: Contiene informacion de:
    Su funcionalidad consiste en poder mostrar los vehiculos  asignados, despedir un especialista  o asignar un vehiculo para revisión del especialista 
    
"""



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
        
        
    def gestionarE(self):
        self._window.geometry("640x480")
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
        self._vTop = tk.Frame(self._window)
        historicoR = tk.Button(self._vEspecialista, text="Revisados", command=lambda:self.visualizarHistorialViajesAsignados(ccAgestionar)).pack() 
        despedirE = tk.Button(self._vEspecialista, text="Despedir", command= lambda: self.despedir(int(ccAgestionar))).pack()
        asignarV = tk.Button(self._vEspecialista, text="Asignar Viaje", command=lambda: self.asignarViaje(ccAgestionar)).pack()
        self._vEspecialista.pack()
        
    
    def visualizarHistorialViajesAsignados(self, cc):
        gHistoricoRevisados = [] 
        for espC in Especialista.getEspecialistas(): # Se busca el especialista seleccionado en el combobox, y se itera la lista de vehiculos revisados para traer sus placas
            print("entra en el for") #eliminar
            if int(cc) == int(espC.getCc()):
                for vehi in espC.getHistoricoVehiculosRevisados():
                    print("entra en el for mas interno")
                    gHistoricoRevisados.append(vehi.getPlaca())
                break
        tk.Label(self._vEspecialista, text=f"Vehiculos revisados: {gHistoricoRevisados}").pack()
     
            
    def despedir(self, cc):
        for espC in Especialista.getEspecialistas():
            if int(cc) == int(espC.getCc()):
                Especialista.getEspecialistas().remove(espC)
                messagebox.showinfo("Despedir", f"Especialista {espC.getuNombre()} despedido")
                
            
    def asignarViaje(self, cc):
        for espC in Especialista.getEspecialistas():
            if int(cc) == int(espC.getCc()):
                indice = 0
                for vehi in Vehiculo.getVehiculos():
                    cadaV = tk.Label(self._vEspecialista, text=f"id: {indice} - Placa: {vehi.getPlaca()}").pack(side="top")
                    indice+=1
                
                vAsignar = tk.Entry(self._vEspecialista).pack(side="top")
                
                aVasignarBot = tk.Button(self._vEspecialista, text="Asignar Vehiculo", command=lambda: print(vAsignar.get())).pack(side="top")#command=lambda: self.asignarVE(espC, int(vAsignar.get()))).pack(side="top")
                # por que el vAsignar.get() no me trae la entrada
    """
    def asignarVE(self, espcialista, indxVehiculo):
        
        Asignar.asignarVehiculoEspecialista(espcialista, Vehiculo.getVehiculos[indxVehiculo])
        espcialista.revisionVehiculo(Vehiculo.getVehiculos[indxVehiculo])
        messagebox.showinfo("Confirmacion", "Se ha asignado  {Vehiculo.getVehiculos[indxVehiculo].getPlaca()} con exito")
        """
        
    
        
        

    def MatarTodo(self, frameUsado):
        for frame in self.winfo_children():
            frame.pack_forget()
        frameUsado.pack(fill=BOTH,expand=True)
        