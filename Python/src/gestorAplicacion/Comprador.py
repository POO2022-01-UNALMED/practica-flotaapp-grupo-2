from src import *

class Comprador(Usuario):
    _historicoViajes = []
    _compradores = []

    def __init__(self,cc: int = 0, uNombre = None, email = None, movil: int = 0, billetera: int = 0):
        super().__init__(cc, uNombre, email, movil, billetera)
        Comprador._historicoViajes.append(Tiquetes) # -historicoViajes: List(Tiquetes)
        Comprador._compradores.append(self)

    def darseBaja(self):

    def buscarTiquete(self):

    def comprarTiquete(self):

    def histocioViaje(self):

    def historicoViaje(self):

