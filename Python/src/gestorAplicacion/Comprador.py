import string
from typing import List
from gestorAplicacion import Usuario, Tiquete

class Comprador(Usuario):
    _compradores = []

    def __init__(self,cc: int = 0, uNombre : string = None, email : string = None, movil: int = 0, billetera: int = 0, historicoViajes : List(Tiquete) = []):
        super().__init__(cc, uNombre, email, movil, billetera)
        self._historicoViajes = historicoViajes # -historicoViajes: List(Tiquetes)
        Comprador._compradores.append(self)

    #def buscarTiquete(self):

    #def comprarTiquete(self):

    #def histocioViaje(self):

    #def historicoViaje(self):

