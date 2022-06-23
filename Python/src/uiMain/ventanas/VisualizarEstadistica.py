import tkinter as tk
import os
import pathlib
from unittest import TestCase

class VisualizarEstadistica(tk.Frame):
    def __init__(self, window):
        super().__init__(window)
        self._window = window
        self._vTop = tk.Frame(self._window)
        title = tk.Label(self._vTop, text="V I S U A L I Z A R   E S T A D I S T I C A S").grid(row=0, column=0 , columnspan=2)
        bCiudad = tk.Button(self._vTop, text="Ciudades").grid(row=1, column=0)
        bViajes = tk.Button(self._vTop, text="Viajes").grid(row=1, column=1)
        graficaEstadistica = tk.Label(self._window, width=200, height=200, text="TEXTO PRUEBA")
        self._vTop.pack()
        graficaEstadistica.pack()