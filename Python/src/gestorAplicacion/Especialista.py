import random
from enum import Enum
from types import NoneType
from gestorAplicacion.Empleado import Empleado
from gestorAplicacion.Vehiculo import Vehiculo

class Especialidad(Enum):

    ELECTRICO = "ELECTRICO"

    MECANICO = "MECANICO"

    SILLETERIA = "SILLETERIA"

    ADMINISTRADOR = "ADMINISTRADOR" 

class Especialista(Empleado):

    __especialistas = []

    def __init__(self, cc = 0, uNombre = "ESPECIALISTA NO REGISTRADO", email = "", movil = 666, billetera = 0, especialidad : Especialidad = Especialidad.ADMINISTRADOR, historialVehiculosRevisados = None): #Se está casteando bien los enumeradores?
        super().__init__(cc, uNombre, email, movil, billetera)
        self._historialiVehiculosRevisados = historialVehiculosRevisados
        self._especialidad = especialidad
        Especialista.__especialistas.append(self)

    def renunciar(self):
        Especialista.__especialistas.remove(self)

    @classmethod
    def desvincularEmpleado(cls, especialistaC):
        Especialista.__especialistas.remove(especialistaC)

    ## ---- M E T O D O S ---- ##
    def despedir(self, especialistaE):
        mesage = ""
        if (self.getEspecialidad() == Especialidad.ADMINISTRADOR):
                mesage = f"Empleado {especialistaE.getuNombre()} despedido."
                especialistaE._billetera += 3000
                Especialista.desvincularEmpleado(especialistaE)
        else:
            mesage = "Solo los ADMINISTRADORES pueden despedir usuarios"

        return mesage    

    def revisionVehiculo(self, vehiculoE : Vehiculo):
        mesage = f"El vehiculo {vehiculoE.getPlaca()} esta en buenas condiciones"
        random_int = random.randint(1, 10)#   * 100000  Por que se multiplica por 100000 ????
        if (random_int == 7):
            mesage = f"Al vehiculo {vehiculoE.getPlaca} se le necesitan hacer reparaciones"

        return mesage

    ## G E T   AND S E T ##

    def getuNombre(self):
        return super().getuNombre()

    def getHistorialVehiculosRevisados(self):
        return self._historialiVehiculosRevisados 


    def getEspecialidad(self):
        return self._especialidad

    @classmethod
    def getEspecialistas(cls):
        return Especialista.__especialistas


    def anadirVehiculoHistoria(self, vehiculoE: Vehiculo):
        if self.getHistorialVehiculosRevisados() == None:
            self._historialiVehiculosRevisados = [vehiculoE]
        else:
            self._historialiVehiculosRevisados.append(vehiculoE)


    def __str__(self) : 
        return "Nombre: {}  \n Sueldo: {} \n Especialidad: {}".format(self._uNombre, self._sueldo, self._especialidad) 