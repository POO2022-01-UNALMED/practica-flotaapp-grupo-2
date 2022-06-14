<<<<<<< HEAD
from src import *
from typing import List  
import random
import Empleado
import Especialidad

class Especialista(Empleado):
    
    __historialiVehiculosRevisados = []
    __especialistas = []
    
    def __init__(self, cc: int=0, uNombre: str=None, email: str=None, movil: int = 0, sueldo: int =0, especialidad: Especialidad = None): #Se está casteando bien los enumeradores?
        super().__init__(cc, uNombre, email, movil, sueldo)
=======
import random
from enum import Enum
from gestorAplicacion.Empleado import Empleado

class Especialidad(Enum):

    ELECTRICO = "ELECTRICO"

    MECANICO = "MECANICO"

    SILLETERIA = "SILLETERIA"

    ADMINISTRADOR = "ADMINISTRADOR" 

class Especialista(Empleado):

    __especialistas = []

    def __init__(self, cc = 0, uNombre = "ESPECIALISTA NO REGISTRADO", email = "", movil = 666, billetera = 0, especialidad : Especialidad = Especialidad.ADMINISTRADOR, historialVehiculosRevisados = []): #Se está casteando bien los enumeradores?
        super().__init__(cc, uNombre, email, movil, billetera)
        self.__historialiVehiculosRevisados = historialVehiculosRevisados
>>>>>>> master
        self._especialidad = especialidad
        Especialista.__especialistas.append(self)

    def renunciar(self):
        Especialista.__especialistas.remove(self)
<<<<<<< HEAD
        
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
=======

    @classmethod
    def desvincularEmpleado(cls, especialistaC):
        Especialista.__especialistas.remove(especialistaC)

    ## ---- M E T O D O S ---- ##
    def revisionVehiculo(self, vehiculoE):
        mesage = "El vehiculo " + vehiculoE.getPlaca() +" esta en buenas condiciones"
        random_int = random.randint(1, 254) * 100000 # Por que se multiplica por 100000 ????
        if (random_int == 13):
            mesage = "Al vehiculo " + vehiculoE.getPlaca + " se le necesitan hacer reparaciones"

        return mesage

    def despedir(self, especialistaE):

        mesage = ""
        if (especialistaE.getEspecialidad() == Especialidad.ADMINISTRADOR):
>>>>>>> master
                mesage = "Empleado " + especialistaE._uNombre + " despedido."
                especialistaE._billetera += 3000
                Especialista.desvincularEmpleado(especialistaE)
        else:
            mesage = "Solo los ADMINISTRADORES pueden despedir usuarios"
<<<<<<< HEAD
        
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
    
    def __str__(self) : 
        return "Nombre: {}  \n Sueldo: {} \n Especialidad: {}".format(self._uNombre, self._sueldo, self._especialidad)
=======

        return mesage    

    ## ----- GETTERS ----- ##
    def getuNombre(self):
        return super().getuNombre()

    def getHistorialVehiculosRevisados(self):
        return self.__historialiVehiculosRevisados 


    def getEspecialidad(self):
        return self._especialidad

    @classmethod
    def getEspecialistas(cls):
        return Especialista.__especialistas
>>>>>>> master
