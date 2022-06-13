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