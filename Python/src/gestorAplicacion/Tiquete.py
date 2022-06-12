from src import *
from typing import List

class Tiquete():                        #Comprador , Silla, Viaje
    __tiquetes = []

    def __init__(self, idTiquete : int = 0, comprador = None, sillaTiquete =None, viaje = None, valor : int = 0, fechaCompra : datetime = None):

        self._idTiquete = idTiquete
        self._comprador = comprador
        self._sillaTiquete = sillaTiquete
        self._viaje = viaje
        self._valor = valor
        self._estado = False
        self._fechaCompra = fechaCompra
        Tiquete.__tiquetes.append(self)
    
    @property
    def estado(self) -> bool: 
        return self._estado
    
    @estado.setter 
    def estado(self, estado : bool):
        self._estado = estado
    
    @property
    def sillaTiquete(self):
        return self._sillaTiquete

    @property
    def viaje(self):
        return self._viaje

    @property
    def comprador(self):
        return self._comprador

    @comprador.setter 
    def comprador(self, comprador):
        self._comprador = comprador

    @property
    def valor(self) -> int:
        return self._valor
    
    @fechaCompra.setter
    def fechaCompra(self, fechaCompra : datetime):
        self._fechaCompra = fechaCompra

    @classmethod
    def tiquetes(cls) -> List(Tiquete):
        return Tiquete.__tiquetes

    def __str__(self) -> str:
        return f"Tiquete = ID : {self.idTiquete} - SILLA : {self.sillaTiquete} \n VIAJE = {self.viaje} - valor : {self.valor} - fechaCompra : {self.fechaCompra}"