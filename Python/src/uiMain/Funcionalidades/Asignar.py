from datetime import datetime
import sys
sys.path.append("../practica-flotaapp-grupo-2/Python/src")

from gestorAplicacion.Comprador import Comprador
from gestorAplicacion.Tiquete import Tiquete
from gestorAplicacion.Vehiculo import Vehiculo
from gestorAplicacion.Viaje import Viaje
from gestorAplicacion.Conductor import Conductor
from gestorAplicacion.Especialista import Especialista



class Asignar():
    @staticmethod
    def asignarTiquete(comprador : Comprador, tiquete : Tiquete):
        tiquete.setComprador(comprador)
        tiquete.setFechaCompra(datetime.now())
        tiquete.setEstado(True)
        comprador.anadirTiqueteHistoria(tiquete)
        tiquete.getViaje().getDestino().anadirVisitantes(1)
    
    @staticmethod
    def asignarVehiculoConductor(conductor : Conductor, viaje : Viaje):
        viaje.setConductor(conductor)
        conductor.anadirViajeHistoria(viaje)
    
    @staticmethod
    def asignarVehiculoEspecialista(especialista : Especialista, vehiculo : Vehiculo):
        especialista.anadirVehiculoHistoria(vehiculo)