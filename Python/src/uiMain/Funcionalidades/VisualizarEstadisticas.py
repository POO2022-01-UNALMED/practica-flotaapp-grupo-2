from matplotlib import pyplot as plt
from gestorAplicacion.viajes.Viaje import Viaje
from gestorAplicacion.viajes.Ciudad import Ciudad

class VisualizarEstadisticas():
    """
    VisualizarEstadisticas : Contiene informacion de: 
        Se puede visuaizar estadisticas por Ciudad y por Viaje, mostrando por medio de una grafica el porcentaje de visitas por cada ciudad
        y calculando la utilidad de cada viaje teniendo en cuenta el valor generado por compra de tiquetes menos
        el costo por cada viaje 
    
    """

    @staticmethod
    def visualizarEstadisticas():
        print("----- V I S U A L I Z A R   E S T A D I S T I C A S -----")
        print("[1] Ciudades , [2] Viajes")
        aux = int(input())
        if aux == 1:
            nombresCiudades= [str(ciudad.getNombre()) for ciudad in Ciudad.getCiudades()]
            numeroVisitantes = [ciudad.getNumVisitantes() for ciudad in Ciudad.getCiudades()]
            plt.bar(nombresCiudades, numeroVisitantes)
            plt.ylabel("Numero de Visitantes")
            plt.xlabel("Nombre de Ciudades")
            plt.title("Visualizar Estadisticas Ciudades")
            plt.show()
            
        elif aux == 2:
            nombreViaje = [ f"{viaje.getOrigen().getNombre()} \n {viaje.getDestino().getNombre()}"  for viaje in Viaje.getViajes()]
            tiquetesComprador = [int(len(viaje.getAllTiquetes())- len(viaje.tiquetesDisponibles())) for viaje in Viaje.getViajes()]
            tiquetesDisponibles = [ int(len(viaje.getAllTiquetes())) for viaje in Viaje.getViajes()]
            plt.barh(nombreViaje, tiquetesDisponibles, color = "c")
            plt.barh(nombreViaje, tiquetesComprador, color = "r")
            plt.ylabel("Viaje : Origen - Destino")
            plt.xlabel("Cantidad de Tiquetes")
            plt.title("Visualizar Estadisticas Viajes")
            plt.show()

            gananciasGeneradas = [ viaje.gananciasGeneradas() for viaje in Viaje.getViajes()]
            plt.barh(nombreViaje, gananciasGeneradas, color = "c")
            plt.ylabel("Viaje : Origen - Destino")
            plt.xlabel("Ganancias Generadas")
            plt.title("Visualizar Estadisticas Conductores")
            plt.show()         
            