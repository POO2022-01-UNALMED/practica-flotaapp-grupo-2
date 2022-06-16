from matplotlib import pyplot as plt
import sys
sys.path.append("../practica-flotaapp-grupo-2/Python/src")

from gestorAplicacion.Comprador import Comprador
from gestorAplicacion.Tiquete import Tiquete
from gestorAplicacion.Vehiculo import Vehiculo
from gestorAplicacion.Viaje import Viaje
from gestorAplicacion.Ciudad import Ciudad
from gestorAplicacion.Conductor import Conductor
from gestorAplicacion.Especialista import Especialista

class VisualizarEstadisticas():

    @staticmethod
    def visualizarEstadisticas():
        print("----- V I S U A L I Z A R   E S T A D I S T I C A S -----")
        print("[1] Ciudades , [2] Viajes")
        aux = int(input())
        if aux == 1:
            nombresCiudades= [str(ciudad.getNombre()) for ciudad in Ciudad.getCiudades()]
            numVisitantes = [int(ciudad.getNumVisitantes()) for ciudad in Ciudad.getCiudades()]
            plt.bar(nombresCiudades, numVisitantes)
            plt.ylabel("Numero de Visitantes")
            plt.xlabel("Nombre de Ciudades")
            plt.title("Visualozar Estadisticas Ciudades")
            plt.show()
            
        elif aux == 2:
            nombreViaje = [ f"{viaje.getOrigen().getNombre()} \n {viaje.getDestino().getNombre()}"  for viaje in Viaje.getViajes()]
            tiquetesComprador = [int(len(viaje.getAllTiquetes())- len(viaje.tiquetesDisponibles())) for viaje in Viaje.getViajes()]
            tiquetesDisponibles = [ int(len(viaje.getAllTiquetes())) for viaje in Viaje.getViajes()]
            plt.barh(nombreViaje, tiquetesDisponibles, color = "c")
            plt.barh(nombreViaje, tiquetesComprador, color = "r")
            plt.ylabel("Viaje : Origen - Destino")
            plt.xlabel("Cantidad de Tiquetes")
            plt.title("Visualozar Estadisticas Viajes")
            plt.show()

            gananciasGeneradas = [ viaje.gananciasGeneradas() for viaje in Viaje.getViajes()]
            plt.barh(nombreViaje, gananciasGeneradas, color = "c")
            plt.ylabel("Viaje : Origen - Destino")
            plt.xlabel("Ganancias Generadas")
            plt.title("Visualizar Estadisticas Conductores")
            plt.show()
            