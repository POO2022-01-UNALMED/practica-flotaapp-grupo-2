from src import*

class Silla():
    _sillas = []
    
    def __init__(self,numeroSilla: int =  0, tipo: bool =  False, ubicacion = None):
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

    def getUbicacion(self):
        return self._ubicacion
    
    @classmethod

    def getSillas(cls):
        return Silla._sillas


    def __str__(self) -> str:
        return f"Silla (numeroSilla: {self._numeroSilla} - tipo: {self._tipo} - ubicacion: {self._ubicacion})"

        
