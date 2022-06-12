from src import*

class Silla():
    _sillas = []
    
    def __init__(self,numeroSilla: 0, tipo: False, ubicacion: None):
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

        
