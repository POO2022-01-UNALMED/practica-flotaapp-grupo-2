import pickle
from gestorAplicacion.personas.Comprador import Comprador
from gestorAplicacion.viajes.Ciudad import Ciudad
from gestorAplicacion.viajes.Vehiculo import Vehiculo
from gestorAplicacion.viajes.Viaje import Viaje
from gestorAplicacion.personas.Conductor import Conductor
from gestorAplicacion.personas.Especialista import Especialista
import pathlib
import os
""""
 * Se utiliza para serializar todos los objetos creados durante la ejecucion
 * del proyecto
 * @author Erik Gonzalez
 * @author Felipe Miranda
 * @author Esteban Garcia
 * @author Emilio Porras
 */"""
class Serializador():
    
    def serializar():
        """ Método encargado de guardar los datos del
            sistema al cerrar la app"""

        datos = {
                "compradores": Comprador.getCompradores(),
                "ciudades" : Ciudad.getCiudades(),
                "vehiculos" : Vehiculo.getVehiculos(),
                "viajes" : Viaje.getViajes(),
                "conductores" : Conductor.getConductores(),
                "especialistas" : Especialista.getEspecialistas(),
                }

        for archivo, dato in datos.items():
            picklefile = open(os.path.join(pathlib.Path(__file__).parent.absolute(), f"temp\\{archivo}"),"wb")
            pickle.dump(dato, picklefile)
            picklefile.close()


