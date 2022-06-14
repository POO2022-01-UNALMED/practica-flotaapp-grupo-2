from datetime import datetime
from typing import List
from gestorAplicacion.Viaje import Viaje
from gestorAplicacion.Usuario import Usuario
from gestorAplicacion.Tiquete import Tiquete
from gestorAplicacion.Ciudad import Ciudad

class Comprador(Usuario):
    '''
    Comprador : Contiene la informacion de: 
        - ID : int
        - Nombre : String
        - email : String
        - movil : int
        - Billetera : int
        - Historico de Viajes : List(Tiquetes)
    Su funcionalidad sera de servir como objeto de referencia para un Usuario de tipo Comprador 
    el cual podra acceder a los servicios de Comprar un Tiquete y sus derivados.
    '''
    _compradores = []

    def __init__(self,cc: int = 0, uNombre : str = None, email : str = None, movil: int = 0, billetera: int = 0, historicoViajes = None):
        super().__init__(cc, uNombre, email, movil, billetera)
        self._historicoViajes = historicoViajes # -historicoViajes: List(Tiquetes)
        Comprador._compradores.append(self)

    def anadirTiqueteHistoria(self, tiquete : Tiquete):
        self._historicoViajes.append(tiquete)

    #def buscarTiquete(self):

    def comprarTiquete(self, origen : Ciudad, destino : Ciudad, presupuesto : int):
        for viaje in Viaje.getViajes():
            if viaje.getDestino() == destino and viaje.getOrigen() == origen and viaje.getFechaViaje() > datetime.now():
                tiqueteFinal = viaje.tiqueteDisponible(presupuesto)
                if tiqueteFinal != None:
                    return tiqueteFinal

    def getHistocioViaje(self):
        return self._historicoViajes