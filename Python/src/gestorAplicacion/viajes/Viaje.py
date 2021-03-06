from datetime import datetime
from gestorAplicacion.viajes.Vehiculo import Vehiculo
from gestorAplicacion.viajes.Ciudad import Ciudad

class Viaje():
    '''
    Viaje : Contiene la informacion de: 
        - Ciudad : Ciudad: Origen - Destino
        - Vehiculo : Vehiculo
        - Conductor : Conductor
        - Fecha del Viaje : Datetime
        - Tiquetes : Tiquete: Ocupados y aun sin Ocupar
    Su funcionalidad sera de servir como intermediario para realización de diferentes funcionalidades como lo son:
        - Compra de Tiquetes
        - Asignación de Viaje a un Conductor
        - Visualizar Estadisticas : Aumentar o disminuir frecuencia
    '''
    __viajes = []
    __tiquetesTotales = 0
    def __init__(self, idViaje : int = 0, costo : int = 0, precioEstandar : int = 0, precioPremium : int = 0, origen : Ciudad = None, destino : Ciudad = None, frecuencia : int = 0, vehiculo : Vehiculo = None, fechaViaje : datetime = None) -> None:
        from gestorAplicacion.viajes.Tiquete import Tiquete
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
        self._allTiquetes = [Tiquete(silla.getNumeroSilla()+self.__tiquetesTotales, None, silla, self, self._precioPremium, None) for silla in self.getVehiculo().getSillas() if silla.getTipo()] + [Tiquete(silla.getNumeroSilla()+self.__tiquetesTotales, None, silla, self, self._precioEstandar, None) for silla in self.getVehiculo().getSillas() if silla.getTipo() == False]
        Viaje.__tiquetesTotales += len(self._allTiquetes)
        Viaje.__viajes.append(self)
        
    def tiquetesDisponibles(self):
        return [tiquete for tiquete in self._allTiquetes if tiquete.getEstado() == False]

    def tiquetesComprador(self):
        return [tiquete for tiquete in self._allTiquetes if tiquete.getEstado() == True]
    
    def tiqueteDisponible(self, presupuesto : int):
        for tiquete in self.getAllTiquetes():
            if tiquete.getValor() <= presupuesto and tiquete.getEstado() == False:
                return tiquete

    def gananciasGeneradas(self):
        costos = self._costo
        compras = 0
        for tiquete in self.tiquetesComprador():
            compras += tiquete.getValor()
        if costos >= compras:
            return 0
        else: 
            return compras - costos

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
    
    def getFechaViaje(self):
        return self._fechaViaje

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

    def getDestino(self) -> Ciudad:
        return self._destino
    
    @classmethod
    def getViajes(cls):
        return cls.__viajes
    
    @classmethod
    def setViajes(cls, viajes):
        cls.__viajes = viajes
    
    @classmethod
    def viajeSinConductor(cls):
        viajesin = []
        for viaje in cls.getViajes():
            if(viaje.getConductor() == None):
                viajesin.append(viaje)
        return viajesin
        #return [viaje for viaje in Viaje.getViajes() if viaje.getConductor == None]
        #Corregí el metodo porque siempre devolvia una lista vacia
    
    def __str__(self):
        return "Origen {} - Destino {}".format(self.getOrigen(), self.getDestino())
