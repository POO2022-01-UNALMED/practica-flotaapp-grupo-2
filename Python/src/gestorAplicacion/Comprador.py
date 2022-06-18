from gestorAplicacion.Usuario import Usuario
from gestorAplicacion.Tiquete import Tiquete

class Comprador(Usuario):
    __compradores = []

    def __init__(self,cc: int = 0, uNombre : str = None, email : str = None, movil: int = 0, billetera: int = 0, historicoViajes: list(Tiquete())=None):
        super().__init__(cc, uNombre, email, movil, billetera)
        self._historicoViajes = historicoViajes # -historicoViajes: List(Tiquetes)
        Comprador.__compradores.append(self)

    #def buscarTiquete(self):

    #def comprarTiquete(self):

    def getHistocioViaje(self):
        return self._historicoViajes
    
    @classmethod()
    def getComprador():
        return Comprador.__compradores
    
    def getCC(self):
        return self.cc