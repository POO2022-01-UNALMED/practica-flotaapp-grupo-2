from src import *

from typing import List  


class Usuario():

    def __init__(self, cc, uNombre, email, movil, billetera: int = 0):

        self._cc = cc

        self._uNombre = uNombre

        self._email = email

        self._movil = movil

        self._billetera = billetera


################### Clase Empleado #########################

class Empleado(Usuario):
    
    
    def __init__(self, cc, uNombre, email, movil, billetera):

        super(). __init__(cc, uNombre, email, movil, billetera)
    

    def renunciar(self):
        self.renunciar()
    
    def bonoSueldo(self):
        self._billetera += self._billetera * 0.1
    


################### Clase Especialista ######################
import random

class Especialista(Empleado):
    
    __historialiVehiculosRevisados = []
    __especialistas = []
    
    def __init__(self, cc, uNombre, email, movil, billetera, especialidad1 = Especialidad(especialidad1)): #Se está casteando bien los enumeradores?
        super().__init__(cc, uNombre, email, movil, billetera)
        especialidad = especialidad1
        Especialista.__especialistas.append(self)

    def renunciar(self):
        Especialista.__especialistas.remove(self)
        
    @classmethod
    def desvincularEmpleado(cls, especialistaC: Especialista(especialistaC)):
        Especialista.__especialistas.remove(especialista1)
     
    ## ---- M E T O D O S ---- ##
    def revisionVehiculo(self, vehiculoE = Vehiculo(vehiculoE)):
        mesage = "El vehiculo " + VehiculoE.getPlaca() +" esta en buenas condiciones"
        random_int = random.randint(1, 254) * 100000 # Por que se multiplica por 100000 ????
        if (random_int == 13):
            mesage = "Al vehiculo " + vehiculoE.getPlaca + " se le necesitan hacer reparaciones"
        
        return mesage
    
    def despedir(self, especialistaE = Especialista(especialistaE)):
        
        mesage = ""
        if (especialistaE.especialidad == Especialidad.ADMINISTRADOR.value):
                mesage = "Empleado " + especialistaE._uNombre + " despedido."
                especialistaE._billetera += 3000
                Especialista.desvincularEmpleado(especialistaE)
        else:
            mesage = "Solo los ADMINISTRADORES pueden despedir usuarios"
        
        return mesage     
        
################### Clase Conductor #########################

class Conductor(Empleado):

    def __init__(self, cc, uNombre, email, movil, billetera):

        super().__init__(cc, uNombre, email, movil, billetera)
        



################### Clase Conductor #########################
from enum import Enum


class Especialidad(Enum):

    ELECTRICO = "ELECTRICO"

    MECANICO = "MECANICO"

    SILLETERIA = "SILLETERIA"

    ADMINISTRADOR = "ADMINISTRADOR"
