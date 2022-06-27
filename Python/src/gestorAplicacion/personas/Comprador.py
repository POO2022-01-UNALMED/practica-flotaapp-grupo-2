from datetime import datetime
from gestorAplicacion.viajes.Viaje import Viaje
from gestorAplicacion.personas.Usuario import Usuario
from gestorAplicacion.viajes.Tiquete import Tiquete
from gestorAplicacion.viajes.Ciudad import Ciudad

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
    __compradores = []

    def __init__(self,cc: int = 0, uNombre : str = None, email : str = None, movil: int = 0, billetera: int = 0, historicoViajes = None):

        super().__init__(cc, uNombre, email, movil, billetera)
        self._historicoViajes = historicoViajes # -historicoViajes: List(Tiquetes)
        Comprador.__compradores.append(self)

    def anadirTiqueteHistoria(self, tiquete : Tiquete):
        if self._historicoViajes == None:
            self._historicoViajes = [tiquete]
        else:
            self._historicoViajes.append(tiquete)
    
    def eliminarTiqueteHistoria(self, tiquete):
        self.getHistorioViaje().remove(tiquete)

    #def buscarTiquete(self):

    def comprarTiquete(self, origen : Ciudad, destino : Ciudad, presupuesto : int):
        for viaje in Viaje.getViajes():
            if viaje.getDestino() == destino and viaje.getOrigen() == origen and viaje.getFechaViaje() > datetime.now():
                tiqueteFinal = viaje.tiqueteDisponible(presupuesto)
                if tiqueteFinal != None:
                    from uiMain.Funcionalidades.Asignar import Asignar
                    Asignar.asignarTiquete(self, tiqueteFinal)
                    return tiqueteFinal

    def getHistorioViaje(self):
        return self._historicoViajes
    
    @classmethod
    def getCompradores(cls):
        return cls.__compradores
    
    @classmethod
    def setCompradores(cls, compradores):
        cls.__compradores = compradores

    def getCC(self):
        return self.cc

    def __str__(self):
        return " Cedula: {} \n Nombre: {} \n Correo: {} \n Celular: {}".format(self.getCc(), self.getuNombre(), self.getEmail(), self.getMovil())

