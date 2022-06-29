from datetime import datetime
from gestorAplicacion.personas.Comprador import Comprador
from gestorAplicacion.viajes.Tiquete import Tiquete
from gestorAplicacion.viajes.Vehiculo import Vehiculo
from gestorAplicacion.viajes.Viaje import Viaje
from gestorAplicacion.personas.Conductor import Conductor
from gestorAplicacion.personas.Especialista import Especialista

class Asignar():
    '''
    Asignar : Contiene la informacion de: 

    Esta clase tiene como objetivo implementar los metodos se asignacion a Empleado y Comprador para ser llamado
    desde las vemntanas o desde las  funcionalidades
    '''
    
    @staticmethod
    def asignarTiquete(comprador : Comprador, tiquete : Tiquete):
        tiquete.setComprador(comprador)
        tiquete.setFechaCompra(datetime.now())
        tiquete.setEstado(True)
        comprador.anadirTiqueteHistoria(tiquete)
        tiquete.getViaje().getDestino().setNumVisitantes(1)
    
    @staticmethod
    def asignarVehiculoConductor(conductor : Conductor, viaje : Viaje):
        viaje.setConductor(conductor)
        conductor.anadirViajeHistoria(viaje)
    
    @staticmethod
    def asignarVehiculoEspecialista(especialista : Especialista, vehiculo : Vehiculo):
        especialista.anadirVehiculoHistoria(vehiculo)
