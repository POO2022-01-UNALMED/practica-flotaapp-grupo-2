from gestorAplicacion.Empleado import Empleado
from enum import Enum

class Categoria(Enum):

    B2 = "B2"

    B3 = "B3"

    C1 = "C1"

    C2 = "C2"

class Conductor(Empleado):

    def __init__(self, cc, uNombre, email, movil, billetera, categoria):

        super().__init__(cc, uNombre, email, movil, billetera)
        self._categoria = categoria