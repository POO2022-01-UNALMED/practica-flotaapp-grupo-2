
class Vehiculo():
    '''
    Vehiculo : Contiene la informacion de: 
        - Placa : str
        - Sillas : List(Silla)
    Su funcionalidad sera de servir como medio para saber cuales son las sillas disponibles
    y con base a esto crear la cantidad de tiquetes justa para un viaje.
    De igual forma como objeto que se le asigna a un Empleado para una revision.
    '''
    _vehiculos = []

    def __init__(self, placa: str = None, sillas=None): #Se inicializa en none 
        self._placa = placa
        self._sillas = sillas
        Vehiculo._vehiculos.append(self)

    def getPlaca(self):
        return self._placa

    def getSillas(self):
        return self._sillas

    def setSillas(self, sillas):
        self._sillas = sillas

    @classmethod
    def getVehiculos(cls):
        return cls._vehiculos
    
    @classmethod
    def setVehiculos(cls, vehiculos):
        cls._vehiculos = vehiculos