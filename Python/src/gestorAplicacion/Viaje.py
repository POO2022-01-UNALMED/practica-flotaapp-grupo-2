import datetime
from src import *
from typing import List

from Python.src.gestorAplicacion.Tiquete import Tiquete


class Viaje():
    '''
    Viaje : Contiene la informacion de: 
        - Ciudad : Origen - Destino
        - Vehiculo
        - Conductor
        - Fecha del Viaje
        - Tiquetes : Ocupados y aun sin Ocupar
    Su funcionalidad sera de servir como intermediario para realización de diferentes funcionalidades como lo son:
        - Compra de Tiquetes
        - Asignación de Viaje a un Conductor
        - Visualizar Estadisticas : Aumentar o disminuir frecuencia
    '''
    __viajes = []
    def __init__(self, idViaje : int = 0, costo : int = 0, precioEstandar : int = 0, precioPremium : int = 0, origen = None, destino = None, frecuencia : int = 0, fechaViaje : datetime = datetime.now(), vehiculo = None) -> None:
        self._idViaje = idViaje
        self._costo = costo
        self._conductor = None
        self._precioEstandar = precioEstandar
        self._precioPremium = precioPremium
        self._origen = origen
        self._destino = destino
        self._frecuencia = frecuencia
        self._fechaViaje = fechaViaje
        self._vehiculo = vehiculo
        self._allTiquetes = []
        #self.allTiquetes = [Tiquete(i.getId(), None, silla, self, self.precioPremium, None) for silla in self.vehiculo.getSillas() if silla.getTipo()] + [Tiquete(i.getId(), None, silla, self, self.precioEstandar, None) for silla in self.vehiculo.getSillas() if !silla.getTipo()]
        Viaje.__viajes.append(self)
        
    def tiquetesDisponibles(self) -> List(Tiquete):
        return [tiquete for tiquete in self._allTiquetes if tiquete.getEstado() == False]
    
    def eliminarViaje(self):
        Viaje.__viajes.remove(self)

    def aumentarFrecuencia(self, aumento : int):
        self._frecuencia += aumento
    
    def disminuirFrecuencia(self, disminucion : int):
        self._frecuencia += disminucion


    @property
    def idViaje(self) -> int:
        return self._idViaje
    
    @property
    def costo(self) -> int :
        return self._costo

    @property
    def conductor(self) -> int:
        return self._conductor
    
    @conductor.setter
    def conductor(self, conductor):
        self._conductor = conductor
    
    @property
    def allTiquetes(self) -> List(Tiquete):
        return self._allTiquetes
    
    @property
    def precioEstandar(self) -> int :
        return self._precioEstandar
    
    @property
    def precioPremium(self) -> int :
        return self._precioPremium
    
    @property
    def fechaViaje(self) -> datetime :
        return self._fechaViaje

    @property
    def vehiculo(self):
        return self._vehiculo
    
    @property
    def origen(self):
        return self._origen

    @property
    def destino(self):
        return self._destino
    
    @classmethod
    def getViajes(cls):
        return Viaje.__viajes
    
    @classmethod
    def viajeSinConductor(cls):
        return [viaje for viaje in Viaje.getViajes() if viaje.conductor == None]