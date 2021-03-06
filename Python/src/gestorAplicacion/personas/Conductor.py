from gestorAplicacion.personas.Empleado import Empleado
from gestorAplicacion.viajes.Viaje import Viaje
from enum import Enum

class Categoria(Enum):
    """
    Categoria : enum
        - almacena el tipo de licencia de conducir para cada Conductor
    """

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
        
    Conductor hereda de Empleado que a su vez hereda de Usuario. Su objetivo es  
    referenciar Empleados de tipo Conductor 
    '''

    __conductores = []

    def __init__(self, cc = 0, uNombre: str = "CONDUCTOR NO REGISTRADO", email: str = "", movil: int = 666, sueldo=0, categoria: Categoria = None, historiaViajesRealizados = None): 
        super().__init__(cc, uNombre, email, movil, sueldo)
        self._categoria = categoria
        self._historiaViajesRealizados = historiaViajesRealizados
        if uNombre != "CONDUCTOR NO REGISTRADO":
            Conductor.__conductores.append(self)

    def anadirViajeHistoria(self, viaje : Viaje):
        if self._historiaViajesRealizados == None:
            self._historiaViajesRealizados = [viaje]
        else:
            self._historiaViajesRealizados.append(viaje)

    ## M E T O D O S ##
    def bonoSueldo(self):
        sueldo += sueldo * 0.15      # -Bonifica al empleado en un 15% mas a su sueldo
        superConductor = None
        for  cadaConductor in Conductor.__conductores:
             if superConductor == None:
                    superConductor = cadaConductor
             elif len(cadaConductor._historiaViajesRealizados) > len(superConductor._historiaViajesRealizados):
                 superConductor = cadaConductor
             else:
                 continue

        if superConductor != None:
            sueldo += sueldo * 0.1    # -Incrementa 10%  adicional al sueldo si es el conductor con mas viajes realizados     


    def renunciar(self):
        Conductor.__conductores.remove(self)

    ## G E T  A N D  S E T ##

    def setCategoria(self, categoria: Categoria = None):
        self._categoria = categoria
    
    @staticmethod
    def buscarConductor(id):
        for i in Conductor.getConductores():
            if i.getCc() == id:
                return i
    
    @classmethod
    def desvincularConductor(cls, conductor):
        cls.__conductores.remove(conductor)

    @classmethod
    def getConductores(cls):
        return cls.__conductores
    
    @classmethod
    def setConductores(cls, conductores):
        cls.__conductores = conductores

    def getHistoricoViajesRealizados(self):
        if self._historiaViajesRealizados == None:
            return []
        else:
            return self._historiaViajesRealizados 

    def __str__(self): 
        return "CC: {} - Nombre {} - Sueldo: {} - Categoria : {} - Viajes realizado : {}".format(self._cc, self._uNombre, self._sueldo, self._categoria,self._historiaViajesRealizados) 
