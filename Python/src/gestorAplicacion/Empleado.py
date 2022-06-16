from gestorAplicacion.Usuario import Usuario
from enum import Enum

class Especialidad(Enum):

    ELECTRICO = "ELECTRICO"

    MECANICO = "MECANICO"

    SILLETERIA = "SILLETERIA"

    ADMINISTRADOR = "ADMINISTRADOR"
 #Superclase Empleado

class Empleado(Usuario):
    def __init__(self, cc, uNombre, email, movil, billetera):
        super(). __init__(cc, uNombre, email, movil, billetera)
        self._sueldo = 0

    def renunciar(claseR):
        claseR.renunciar()
        
    def bonoSueldo(self):
        self._billetera += self._billetera * 0.1

    def getEspecialidad(self):
        return Especialidad