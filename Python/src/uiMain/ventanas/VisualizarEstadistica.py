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
        self._vTop = tk.Frame(self._window)
        self._fEstadistica = tk.Frame(self._window)
        
        title = tk.Label(self._vTop, text="V I S U A L I Z A R   E S T A D I S T I C A S").grid(row=0, column=0 , columnspan=2)
        bCiudad = tk.Button(self._vTop, text="Ciudades", command=self.visualizarCiudades).grid(row=1, column=0)
        bViajes = tk.Button(self._vTop, text="Viajes", command = self.visualizarViajes).grid(row=1, column=1)

        self._vTop.pack(side="top")

    def visualizarCiudades(self):
        os.remove("visEstadisticaCiudad.png")
        self._window.geometry("640x480")
        self._fEstadistica.destroy()
        self._fEstadistica = tk.Frame(self._window)
        nombresCiudades= [ self.abreviacionCiudad[str(ciudad.getNombre())] for ciudad in Ciudad.getCiudades()]
        numeroVisitantes = [ciudad.getNumVisitantes() for ciudad in Ciudad.getCiudades()]
        plt.clf()
        plt.bar(nombresCiudades, numeroVisitantes)
        plt.ylabel("Numero de Visitantes")
        plt.xlabel("Nombre de Ciudades")
        plt.title("Visualozar Estadisticas Ciudades")
        plt.savefig("visEstadisticaCiudad.png")
        img = ImageTk.PhotoImage(Image.open('visEstadisticaCiudad.png').resize((600, 400)))
        tk.Label(self._fEstadistica, width=600, height=400, image= img).pack()
        self._fEstadistica.pack(side="top")
            
    
    def visualizarViajes(self):
        os.remove("visEstadisticaViaje.png")
        os.remove("visEstadisticaViaje2.png")
        self._window.geometry("880x400")
        self._fEstadistica.destroy()
        self._fEstadistica = tk.Frame(self._window)
        nombreViaje = [ f"{viaje.getOrigen().getNombre()} \n {viaje.getDestino().getNombre()}"  for viaje in Viaje.getViajes()]
        gananciasGeneradas = [ viaje.gananciasGeneradas() for viaje in Viaje.getViajes()]
        plt.clf()
        plt.barh(nombreViaje, gananciasGeneradas, color = "c")
        plt.ylabel("Viaje : Origen - Destino")
        plt.xlabel("Ganancias Generadas")
        plt.title("Visualizar Estadisticas Viajes")  
        plt.savefig("visEstadisticaViaje.png") 
        img = ImageTk.PhotoImage(Image.open('visEstadisticaViaje.png').resize((400, 300)))
        tk.Label(self._fEstadistica, width=400, height=300, image= img).grid(column=0, row=0, padx=20 , pady= 20)

        tiquetesComprador = [int(len(viaje.getAllTiquetes())- len(viaje.tiquetesDisponibles())) for viaje in Viaje.getViajes()]
        tiquetesDisponibles = [ int(len(viaje.getAllTiquetes())) for viaje in Viaje.getViajes()]
        plt.clf()
        plt.barh(nombreViaje, tiquetesDisponibles, color = "c")
        plt.barh(nombreViaje, tiquetesComprador, color = "r")
        plt.ylabel("Viaje : Origen - Destino")
        plt.xlabel("Cantidad de Tiquetes")
        plt.title("Visualozar Estadisticas Viajes")
        plt.savefig("visEstadisticaViaje2.png") 
        img2 = ImageTk.PhotoImage(Image.open('visEstadisticaViaje2.png').resize((400, 300)))
        tk.Label(self._fEstadistica, width=400, height=300, image= img2).grid(column=1, row=0, padx= 20, pady= 20)


        self._fEstadistica.pack(side="top")
              
            