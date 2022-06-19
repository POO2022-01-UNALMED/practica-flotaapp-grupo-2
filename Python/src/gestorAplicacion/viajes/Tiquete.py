from gestorAplicacion.viajes.Viaje import Viaje
import datetime

class Tiquete():                        #Comprador , Silla, Viaje
    '''
    Tiquete : Contiene la informacion de: 
        - Viaje
        - Comprador
        - Valor
    Su funcionalidad sera de servir como evidencia de la reserva (compra) de una silla en un viaje
    '''
    __tiquetes = []

    def __init__(self, idTiquete : int = 0, comprador = None, sillaTiquete =None, viaje : Viaje = None, valor : int = 0, fechaCompra : datetime = None):

        self._idTiquete = idTiquete
        self._comprador = comprador
        self._sillaTiquete = sillaTiquete
        self._viaje = viaje
        self._valor = valor
        self._estado = False
        self._fechaCompra = fechaCompra
        Tiquete.__tiquetes.append(self)
    
    def getEstado(self) -> bool: 
        return self._estado
    
    def setEstado(self, estado : bool):
        self._estado = estado
    
    def getSillaTiquete(self):
        return self._sillaTiquete

    def getViaje(self) -> Viaje:
        return self._viaje

    def getComprador(self):
        return self._comprador

    def setComprador(self, comprador):
        self._comprador = comprador

    def getValor(self) -> int:
        return self._valor
    
    def setFechaCompra(self, fechaCompra : datetime):
        self._fechaCompra = fechaCompra

    @classmethod
    def tiquetes(cls):
        return Tiquete.__tiquetes

    def __str__(self) -> str:
        return f"Tiquete = ID : {self._idTiquete} - SILLA : {self._sillaTiquete} \n VIAJE = {self._viaje} - valor : {self._valor} - fechaCompra : {self._fechaCompra}"