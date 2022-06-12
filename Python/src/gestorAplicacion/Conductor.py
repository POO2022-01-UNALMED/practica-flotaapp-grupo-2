from gestorAplicacion.Empleado import Empleado

class Conductor(Empleado):

    def __init__(self, cc, uNombre, email, movil, billetera):

        super().__init__(cc, uNombre, email, movil, billetera)