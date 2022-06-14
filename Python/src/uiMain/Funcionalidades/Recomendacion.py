from gestorAplicacion.Ciudad import Ciudad
from gestorAplicacion.Comprador import Comprador

class Recomendacion():
    visitadas = {}

    @classmethod()
    def recomendarViaje(cls, cc: int = 0):
        recomendadisima = Ciudad()
        aRecomendar = Comprador() 