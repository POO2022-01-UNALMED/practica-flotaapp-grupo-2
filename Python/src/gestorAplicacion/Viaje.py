import datetime
from gestorAplicacion.Vehiculo import Vehiculo

class Viaje():
    '''
    Viaje : Contiene la informacion de: 
        - Ciudad : Origen - Destino
        - Vehiculo
        - Conductor
        - Fecha del Viaje
        - Tiquetes : Ocupados y aun sin Ocupar
    Su funcionalidad sera de servir como intermediario para realización de diferentes funcionalidades como lo son:
        - Compra de Tiquetes
        - Asignación de Viaje a un Conductor
        - Visualizar Estadisticas : Aumentar o disminuir frecuencia
    '''
    __viajes = []
    def __init__(self, idViaje : int = 0, costo : int = 0, precioEstandar : int = 0, precioPremium : int = 0, origen = None, destino = None, frecuencia : int = 0, vehiculo : Vehiculo = None, fechaViaje : datetime = None) -> None:
        from gestorAplicacion.Tiquete import Tiquete
        self._idViaje = idViaje
        self._costo = costo
        self._conductor = None
        self._precioEstandar = precioEstandar
        self._precioPremium = precioPremium
        self._origen = origen
        self._destino = destino
        self._frecuencia = frecuencia
        self._fechaViaje = fechaViaje
        self._vehiculo = vehiculo
        self._allTiquetes = []
        self.allTiquetes = [Tiquete(silla.getNumeroSilla(), None, silla, self, self._precioPremium, None) for silla in self.getVehiculo().getSillas() if silla.getTipo()] + [Tiquete(silla.getNumeroSilla(), None, silla, self, self._precioEstandar, None) for silla in self.getVehiculo().getSillas() if silla.getTipo() == False]
        Viaje.__viajes.append(self)
        
    def tiquetesDisponibles(self):
        return [tiquete for tiquete in self._allTiquetes if tiquete.getEstado() == False]
    
    def eliminarViaje(self):
        Viaje.__viajes.remove(self)

    def aumentarFrecuencia(self, aumento : int):
        self._frecuencia += aumento
    
    def disminuirFrecuencia(self, disminucion : int):
        self._frecuencia += disminucion


    def getIdViaje(self) -> int:
        return self._idViaje
    
    def getCosto(self) -> int :
        return self._costo

    def getConductor(self) -> int:
        return self._conductor
    
    def setConductor(self, conductor):
        self._conductor = conductor

    def getAllTiquetes(self):
        return self._allTiquetes

    def getPrecioEstandar(self) -> int :
        return self._precioEstandar

    def getPrecioPremium(self) -> int :
        return self._precioPremium

    def getFechaViaje(self) -> datetime :
        return self._fechaViaje

    def getVehiculo(self) -> Vehiculo:
        return self._vehiculo
    
    def getOrigen(self):
        return self._origen

    def getDestino(self):
        return self._destino
    
    @classmethod
    def getViajes(cls):
        return Viaje.__viajes
    
    @classmethod
    def viajeSinConductor(cls):
        viajesin = []
        for viaje in Viaje.getViajes():
            if(viaje.getConductor() == None):
                viajesin.append(viaje)
        return viajesin
        #return [viaje for viaje in Viaje.getViajes() if viaje.getConductor == None]
        #Corregí el metodo porque siempre devolvia una lista vacia
    
    def __str__(self):
        return "\n IdViaje: {} \n Origen {} \n Destino {} \n Fecha Viaje {}".format(self.getIdViaje(),self.getOrigen(), self.getDestino(), self.getFechaViaje())
