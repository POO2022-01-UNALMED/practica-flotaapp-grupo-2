
import tkinter as tk
#from matplotlib import pyplot as plt
from PIL import Image, ImageTk
from setuptools import Command
import os
import pathlib
from unittest import TestCase
from gestorAplicacion.viajes.Tiquete import Tiquete
from gestorAplicacion.personas.Comprador import Comprador
from gestorAplicacion.viajes.Ciudad import Ciudad
from gestorAplicacion.viajes.Vehiculo import Vehiculo
from gestorAplicacion.viajes.Silla import Silla, Ubicacion
from gestorAplicacion.viajes.Viaje import Viaje
from gestorAplicacion.personas.Conductor import Conductor, Categoria
from gestorAplicacion.personas.Especialista import Especialidad, Especialista
from uiMain.Funcionalidades.Gestionar import Gestionar
from datetime import datetime
from datetime import timedelta

class GestionarViajes(tk.Frame):

    def __init__(self, window):
        super().__init__(window)
        self._window = window
        self._vTop = tk.Frame(self._window)
        self._vTop1 = tk.Frame(self._window)
        self._vTop2 = tk.Frame(self._window)
        self._vTop3 = tk.Frame(self._window)
        self._vTop4 = tk.Frame(self._window)
        self.entrada = tk.StringVar()
        self.entrada1 = tk.StringVar()
        self.entrada2 = tk.StringVar()
        
        def boton():
            valor = int(self.entrada.get())
            if valor in listadeviajeros:
                Ventana1()
            else:
                sinregistro = tk.Label(self._vTop, text="la cédula no esta registrado").grid(row=5, column=1, padx=10, pady=10)
            return int(self.entrada.get())

        def boton1():
            valor = int(self.entrada.get())
            if valor == 1:
                ventana2()
            else:
                print("no el ID no esta registrado")

        def Ventana1():
            self._window.geometry("640x420")
            self._vTop.destroy()
            title1 = tk.Label(self._vTop1, text="G E S T I O N A R   V I A J E S ").grid(row=0,column=0)
            buscar1 = tk.Button(self._vTop1, text="Buscar", command= boton1).grid(row=3, column=0, padx=10, pady=10)
            info1 = tk.Entry(self._vTop1, borderwidth=2, textvariable =self.entrada1).grid(row=1, column=1)
            viaje1 = tk.Label(self._vTop1, text="Ingrese el ID que quiere gestionar ").grid(row=1, column=0,padx=10, pady=10)
        
        def boton2():
            Ventana3()

        def boton2_2():
            sinregistro1 = tk.Label(self._vTop2, text="Tu tiquete ha sido cancelado").grid(row=5, column=1)

            
    

        def ventana2():
            self._window.geometry("640x420")
            self._vTop1.destroy()
            title2 = tk.Label(self._vTop2, text="G E S T I O N A R   V I A J E S ").grid(row=0,column=1)
            buscar2 = tk.Button(self._vTop2, text="[1] Cambiar Tiquete", command= boton2).grid(row=1, column=0,padx=10, pady=10)
            buscar2_2 = tk.Button(self._vTop2, text="[2] Cancelar Tiquete", command= boton2_2).grid(row=1, column=4,padx=10, pady=10)
            
        
        def boton3():
            valor = int(self.entrada2.get())
            if valor == 1:
                Ventana4()
            else:
                sinregistro1 = tk.Label(self._vTop3, text="No ingresaste bien el el número").grid(row=5, column=1)

        def boton4():
            

      

        def Ventana3():
            self._window.geometry("640x420")
            self._vTop2.destroy()
            title3 = tk.Label(self._vTop3, text="G E S T I O N A R   V I A J E S ").grid(row=0,column=0)
            buscar3 = tk.Button(self._vTop3, text="Buscar", command= boton3).grid(row=3, column=0, padx=10, pady=10)
            info3 = tk.Entry(self._vTop3, borderwidth=2, textvariable =self.entrada2).grid(row=1, column=1)
            viaje3 = tk.Label(self._vTop3, text="Escoge un tiquete por el cual cambiarlo ").grid(row=1, column=0,padx=10, pady=10)


        def boton4():
            self.destroy()
            ventana7 = GestionarViajes()
            .mainloop()
        """    
        def boton4():
            sinregistro2 = tk.Label(self._vTop4, text="Ya lograste cambiar el tiquete").grid(row=5, column=0)
        """
            
        
        def Ventana4():
            self._window.geometry("640x420")
            self._vTop3.destroy()
            title3 = tk.Label(self._vTop4, text="G E S T I O N A R   V I A J E S ").grid(row=0,column=0)
            buscar3 = tk.Button(self._vTop4, text="Volver a pantalla gestionar viajes", command=boton4).grid(row=6, column=0)
            viaje3 = tk.Label(self._vTop4, text="Escoge un tiquete por el cual cambiarlo ").grid(row=1, column=0)

        

        self._vTop1.pack()
        self._vTop2.pack()
        self._vTop3.pack()
        self._vTop4.pack()

        title = tk.Label(self._vTop, text="G E S T I O N A R   V I A J E S").grid(row=0, column=0)
        viaje = tk.Label(self._vTop, text="Gestionar viaje con la cédula: ").grid(row=1, column=0,padx=10, pady=10)
        info = tk.Entry(self._vTop, borderwidth=2, textvariable =self.entrada).grid(row=1, column=1)
        buscar = tk.Button(self._vTop, text="Buscar", command= boton).grid(row=3, column=0, padx=10, pady=10)
        
        listadeviajeros = [ccComprador.getComprador().getCc() for ccComprador in Tiquete.getTiquetes() if ccComprador.getComprador() != None]
        print(listadeviajeros)  

        self._vTop.pack()

    



        






    






   