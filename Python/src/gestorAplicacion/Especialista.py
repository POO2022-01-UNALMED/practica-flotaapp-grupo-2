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

    def __init__(self, cc, uNombre, email, movil, billetera, especialidad : Especialidad = None, historialVehiculosRevisados = []): #Se está casteando bien los enumeradores?
        super().__init__(cc, uNombre, email, movil, billetera)
        self.__historialiVehiculosRevisados = historialVehiculosRevisados
        self._especialidad = especialidad
        Especialista.__especialistas.append(self)

    def renunciar(self):
        Especialista.__especialistas.remove(self)

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
        if (especialistaE.especialidad == Especialidad.ADMINISTRADOR.value):
                mesage = "Empleado " + especialistaE._uNombre + " despedido."
                especialistaE._billetera += 3000
                Especialista.desvincularEmpleado(especialistaE)
        else:
            mesage = "Solo los ADMINISTRADORES pueden despedir usuarios"

        return mesage    
        


