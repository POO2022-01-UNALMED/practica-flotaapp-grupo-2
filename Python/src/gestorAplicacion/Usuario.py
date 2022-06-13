from src import *

from typing import List  


class Usuario():

    def __init__(self, cc: int=0, uNombre: str=None, email: str=None, movil: int = 0, billetera: int = 0):

        self._cc = cc

        self._uNombre = uNombre

        self._email = email

        self._movil = movil

        self._billetera = billetera


################### Clase Empleado #########################

class Empleado(Usuario):
    
    
    def __init__(self, cc: int=0, uNombre: str=None, email: str=None, movil: int = 0, sueldo: int = 0):
        super(). __init__(cc, uNombre, email, movil)
        self._sueldo = sueldo
    

    def renunciar(self):
        self.renunciar()
    
    def bonoSueldo(self): # Polimorfismo
        self.bonoSueldo()
    


################### Clase Especialista ######################
import random

class Especialista(Empleado):
    
    __historialiVehiculosRevisados = []
    __especialistas = []
    
    def __init__(self, cc: int=0, uNombre: str=None, email: str=None, movil: int = 0, sueldo: int =0, especialidad: Especialidad = None): #Se está casteando bien los enumeradores?
        super().__init__(cc, uNombre, email, movil, sueldo)
        self._especialidad = especialidad
        Especialista.__especialistas.append(self)

    def renunciar(self):
        Especialista.__especialistas.remove(self)
        
    @classmethod
    def desvincularEmpleado(cls, especialistaC: Especialista=None):
        Especialista.__especialistas.remove(especialistaC)
     
    ## ---- M E T O D O S ---- ##
    
    def revisionVehiculo(self, vehiculoE: Vehiculo = None):
        mesage = "El vehiculo " + VehiculoE.getPlaca() +" esta en buenas condiciones"
        random_int = random.randint(1, 10)#   * 100000  Por que se multiplica por 100000 ????
        if (random_int == 7):
            mesage = "Al vehiculo " + vehiculoE.getPlaca + " se le necesitan hacer reparaciones"
        
        return mesage
    
    def despedir(self, especialistaE: Especialista = None):
        mesage = ""
        if (especialistaE.especialidad == Especialidad.ADMINISTRADOR.value):
                mesage = "Empleado " + especialistaE._uNombre + " despedido."
                especialistaE._billetera += 3000
                Especialista.desvincularEmpleado(especialistaE)
        else:
            mesage = "Solo los ADMINISTRADORES pueden despedir usuarios"
        
        return mesage     
    
    ## G E T   AND S E T ##
    
    def anadirVehiculoHistoria(self, vehiculoE: Vehiculo = None):
        self.__historialiVehiculosRevisados.append(vehiculoE)
    
    def getEspecialidad(self):
        return self._especialidad
    
    def getHistoricoVehiculosRevisados(self):
        return self.__historialiVehiculosRevisados
    
    @staticmethod()
    def getEspecialistas(cls):
        return cls.__especialistas
    
    def __str__(self) -> str: 
        return "Nombre: {}  \n Sueldo: {} \n Especialidad: {}".format( self._uNombre, self._sueldo, self._especialidad)
        
    ################### Clase Conductor #########################
 
class Conductor(Empleado):
    
    __historiaViajesRealizados = []
    __conductores = []

    def __init__(self, cc = 0, uNombre: str = None, email: str = None, movil: int = None, sueldo=0, categoria: Categoria = None): # categoria = Categoria(categoria)
        super().__init__(cc, uNombre, email, movil, sueldo)
        self._categoria = categoria
        Conductor.__conductores.append(self)
    
    def anadirViajeHistoria(self, viaje=Viaje(viaje)):
        self.__historiaViajesRealizados.append(viaje)
    
    ## M E T O D O S ##

    
    def bonoSueldo(self):
        sueldo += sueldo * 0.15
        superConductor = None
        for  cadaConductor in Conductor.__conductores:
             if superConductor == None:
                    superConductor = cadaConductor
             elif len(cadaConductor.__historiaViajesRealizados) > len(superConductor.__historiaViajesRealizados):
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
    
    @classmethod()
    def getConductores(cls):
        return Conductor.__conductores
    
    def getHistoricoViajesRealizados(self):
        return self.__historiaViajesRealizados
    
    def __str__(self): 
        return "CC: {} \n Nombre {} \n Sueldo: {} \n Categoria : {} \n Viajes realizado : {}".format(self._cc, self._uNombre, self._sueldo, self._categoria,self.__historiaViajesRealizados) 
               



################### Clase Especialidad #########################
from enum import Enum

class Especialidad(Enum):

    ELECTRICO = "ELECTRICO"

    MECANICO = "MECANICO"

    SILLETERIA = "SILLETERIA"

    ADMINISTRADOR = "ADMINISTRADOR"

################### Clase Categoria #########################
from enum import Enum

class Categoria(Enum):
    B2 = "B2"
    B3 = "B3"
    C1 = "C1"
    C2 = "C2"
    C3 = "C3"