"""
Recomendacion de viajes a Usuarios
"""

class Recomendacion():
    visitadas = {}
    
    @classmethod()
    def recomendarViaje(cls, cc: int = 0):
        recomendadisima = Ciudad()
        aRecomendar = Comprador()