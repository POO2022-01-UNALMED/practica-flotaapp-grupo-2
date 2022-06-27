from cProfile import label
import tkinter as tk
from matplotlib import pyplot as plt
from PIL import Image, ImageTk
from setuptools import Command
from gestorAplicacion.viajes.Ciudad import Ciudad
from gestorAplicacion.viajes.Viaje import Viaje
import os
import pathlib
from unittest import TestCase

class VisualizarEstadistica(tk.Frame):
    abreviacionCiudad = {
        "MEDELLIN" : "MED",
        "POPAYAN"  : "PYAN",
        "CALI"     : "CAL",
        "MANIZALES": "MZL",
        "MONTERIA" : "MONT",
        "PASTO"    : "PSTO",
        "CARTAGENA": "CTG",
        "BELLO"    : "BLL0",
        "BARRANQUILLA" : "BQLLA"
        }

    def __init__(self, window):
        super().__init__(window)
        self._window = window
        self._fEstadistica = tk.Frame(self)
        
        title = tk.Label(self, text="V I S U A L I Z A R   E S T A D I S T I C A S").place(relx=0.1, rely=0.05, relwidth=0.8, relheight=0.1)
        bCiudad = tk.Button(self, text="Ciudades", command=self.visualizarCiudades).place(relx=0.05, rely=0.15, relwidth=0.4, relheight=0.08)
        bViajes = tk.Button(self, text="Viajes", command = self.visualizarViajes).place(relx=0.55, rely=0.15, relwidth=0.4, relheight=0.08)

        self.pack(side="top")

    def visualizarCiudades(self):

        self._window.geometry("780x620")
        self._fEstadistica.destroy()
        self._fEstadistica = tk.Frame(self)
        nombresCiudades= [ self.abreviacionCiudad[str(ciudad.getNombre())] for ciudad in Ciudad.getCiudades()]
        numeroVisitantes = [ciudad.getNumVisitantes() for ciudad in Ciudad.getCiudades()]
        plt.clf()
        plt.bar(nombresCiudades, numeroVisitantes)
        plt.ylabel("Numero de Visitantes")
        plt.xlabel("Nombre de Ciudades")
        plt.title("Visualizar Estadisticas Ciudades")
        plt.savefig("visEstadisticaCiudad.png")
        img = ImageTk.PhotoImage(Image.open('visEstadisticaCiudad.png').resize((600, 400)))
        tk.Label(self._fEstadistica, width=600, height=400, image= img).pack()
        self._fEstadistica.place(relx=0.1, rely=0.25, relwidth=0.8, relheight=0.65)

        os.remove("visEstadisticaCiudad.png")
            
    def visualizarViajes(self):

        self._window.geometry("1100x500")
        self._fEstadistica.destroy()
        self._fEstadistica = tk.Frame(self)
        nombreViaje = [ f"{viaje.getOrigen().getNombre()} \n {viaje.getDestino().getNombre()}"  for viaje in Viaje.getViajes()]
        gananciasGeneradas = [ viaje.gananciasGeneradas() for viaje in Viaje.getViajes()]
        plt.clf()
        plt.barh(nombreViaje, gananciasGeneradas, color = "c")
        plt.ylabel("Viaje : Origen - Destino")
        plt.xlabel("Ganancias Generadas")
        plt.title("Visualizar Estadisticas Viajes")  
        plt.savefig("visEstadisticaViaje.png") 
        img = ImageTk.PhotoImage(Image.open('visEstadisticaViaje.png').resize((480, 300)))
        tk.Label(self._fEstadistica, width=480, height=300, image= img).place(relx=0, rely=0.05, relwidth=0.5, relheight=0.9)

        tiquetesComprador = [int(len(viaje.getAllTiquetes())- len(viaje.tiquetesDisponibles())) for viaje in Viaje.getViajes()]
        tiquetesDisponibles = [ int(len(viaje.getAllTiquetes())) for viaje in Viaje.getViajes()]
        plt.clf()
        plt.barh(nombreViaje, tiquetesDisponibles, color = "c", label="Total Tiquetes")
        plt.barh(nombreViaje, tiquetesComprador, color = "r", label = "Tiquetes Comprados")
        plt.ylabel("Viaje : Origen - Destino")
        plt.xlabel("Cantidad de Tiquetes")
        plt.title("Visualizar Estadisticas Viajes")
        plt.legend()
        plt.savefig("visEstadisticaViaje2.png") 
        img2 = ImageTk.PhotoImage(Image.open('visEstadisticaViaje2.png').resize((480, 300)))
        tk.Label(self._fEstadistica, width=480, height=300, image= img2).place(relx=0.50, rely=0.05, relwidth=0.5, relheight=0.9)
        self._fEstadistica.place(relx=0, rely=0.25, relwidth=1, relheight=0.65)

        os.remove("visEstadisticaViaje.png")
        os.remove("visEstadisticaViaje2.png")
              
            