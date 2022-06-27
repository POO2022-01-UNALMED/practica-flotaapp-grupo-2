import pickle
from gestorAplicacion.personas.Comprador import Comprador
from gestorAplicacion.viajes.Ciudad import Ciudad
from gestorAplicacion.viajes.Vehiculo import Vehiculo
from gestorAplicacion.viajes.Viaje import Viaje
from gestorAplicacion.personas.Conductor import Conductor
from gestorAplicacion.personas.Especialista import Especialista
import pathlib
import os

class Deserializador():
    
    def deserializar():
        """ Método encargado de carcar  los datos del
            sistema al abrir la app"""

        datos = {
                "compradores": lambda x : Comprador.setCompradores(x),
                "ciudades" : lambda x : Ciudad.setCiudades(x),
                "vehiculos" : lambda x : Vehiculo.setVehiculos(x),
                "viajes" : lambda x : Viaje.setViajes(x),
                "conductores" : lambda x : Conductor.setConductores(x),             
                "especialistas" : lambda x : Especialista.setEspecialistas(x),
                }

        for archivo, set in datos.items():
            picklefile = open(os.path.join(pathlib.Path(__file__).parent.absolute(), f"temp\\{archivo}"),"rb")
            dato = pickle.load(picklefile)
            set(dato)
            picklefile.close()