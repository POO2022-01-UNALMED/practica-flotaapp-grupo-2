from enum import Enum

class Ubicacion(Enum):

    VENTANA = "VENTANA"

    PASILLO = "PASILLO"

    INTERMEDIO = "INTERMEDIO"

class Silla():
    '''
    Comprador : Contiene la informacion de: 
        - Numero Silla : int
        - Tipo : bool
        - Ubicacion : Ubicacion(Enum)
    Esta sirve como medio para saber cuantas sillas se crean en un viaje y de igual manera
    contiene información de las sillas de un bus.
    '''
    _sillas = []
   
    def __init__(self,numeroSilla: int =  0, tipo: bool =  False, ubicacion : Ubicacion = None):
        self._numeroSilla =numeroSilla
        self._tipo = tipo
        self._ubicacion = ubicacion
        Silla._sillas.append(self)

    def getTipo(self):
        return self._tipo

    def getNumeroSilla(self):
        return self._numeroSilla

    def setNumeroSillas(self, numeroSilla):
        self._numeroSilla = numeroSilla

    def setTipo(self, tipo):
        self._tipo = tipo

    def getUbicacion(self):
        return self._ubicacion
    
    def setUbicacion(self,ubicacion):
        self._ubicacion = ubicacion

    @classmethod
    def getSillas(cls):
        return Silla._sillas


    def __str__(self) -> str:
        return f"Silla (numeroSilla: {self._numeroSilla} - tipo: {self._tipo} - ubicacion: {self._ubicacion})"       
