from gestorAplicacion.Empleado import Empleado
from gestorAplicacion.Viaje import Viaje
from enum import Enum

class Categoria(Enum):

    B2 = "B2"

    B3 = "B3"

    C1 = "C1"

    C2 = "C2"

class Conductor(Empleado):
    '''
    Comprador : Contiene la informacion de: 
        - ID : int
        - Nombre : String
        - email : String
        - movil : int
        - Sueldo : int
        - Categoria : Categoria(Enum)
        - Historico de Viajes Realizados : List(Viaje)
    Su funcionalidad sera de servir como objeto de referencia para un Usuario de tipo Conductor. 
    A este se le asignara un Viaje. 
    '''

    __conductores = []

    def __init__(self, cc = 0, uNombre: str = None, email: str = None, movil: int = None, sueldo=0, categoria: Categoria = None, historiaViajesRealizados = None): # categoria = Categoria(categoria)
        super().__init__(cc, uNombre, email, movil, sueldo)
        self._categoria = categoria
        self._historiaViajesRealizados = historiaViajesRealizados
        Conductor.__conductores.append(self)

    def anadirViajeHistoria(self, viaje : Viaje):
        if self._historiaViajesRealizados == None:
            self._historiaViajesRealizados = [viaje]
        else:
            self._historiaViajesRealizados.append(viaje)

    ## M E T O D O S ##
    def bonoSueldo(self):
        sueldo += sueldo * 0.15
        superConductor = None
        for  cadaConductor in Conductor.__conductores:
             if superConductor == None:
                    superConductor = cadaConductor
             elif len(cadaConductor._historiaViajesRealizados) > len(superConductor._historiaViajesRealizados):
                 superConductor = cadaConductor
             else:
                 continue

        if superConductor != None:
            sueldo += sueldo * 0.1    # 10% mas de bono si es el conductor con mas viajes realizados     


    def renunciar(self):
        Conductor.__conductores.remove(self)

    ## G E T  A N D  S E T ##

    def setCategoria(self, categoria: Categoria = None):
        self._categoria = categoria

    @classmethod
    def getConductores(cls):
        return Conductor.__conductores

    def getHistoricoViajesRealizados(self):
        if self._historiaViajesRealizados == None:
            return []
        else:
            return self._historiaViajesRealizados 

    def __str__(self): 
        return "CC: {} \n Nombre {} \n Sueldo: {} \n Categoria : {} \n Viajes realizado : {}".format(self._cc, self._uNombre, self._sueldo, self._categoria,self._historiaViajesRealizados) 
