class Ciudad():
    __ciudades = []

    def __init__(self, id : int = 0, nombre : str = None, dirTerminal : str = None):
        self._id = id
        self._nombre = nombre
        self._promocion = 0
        self._numVisitantes = 0
        self._dirTerminal = dirTerminal
        Ciudad.__ciudades.append(self)
    
    def getId(self):
        return self._id

    def getNombre(self):
        return self._nombre

    def getNumVisitantes(self):
        return self._numVisitantes

    def anadirVisitantes(self, numVisitantes : int):
	    self._numVisitantes += numVisitantes
    
    def getPromocion(self):
        return self._promocion
    
    def setPromocion(self, promocion : int):
        self._promocion = promocion


    @classmethod
    def quitarCiudad(cls, CiudadName : str):
        if Ciudad.__ciudades != []:
            for ciudad in Ciudad.__ciudades:
                if ciudad.getNombre == CiudadName:
                    Ciudad.__ciudades.remove(ciudad)
    
    @classmethod
    def getCiudades(self):
        return Ciudad.__ciudades

