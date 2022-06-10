from src import*

class Vehiculo():
    _vehiculos = []

    def __init__(self, placa, sillas):
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
        return Vehiculo._vehiculos

    @classmethod
    def getVehiculoRevisar(cls):
        return Vehiculo.getVehiculos().get(0)