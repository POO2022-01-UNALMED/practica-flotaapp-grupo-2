from gestorAplicacion.Usuario import Usuario
from typing import List   
 #Superclase Empleado

class Empleado(Usuario):
    sueldo = 0

    def __init__(self, cc, uNombre, email, movil, billetera):
        super(). __init__(cc, uNombre, email, movil, billetera)

    def renunciar(claseR):
        claseR.renunciar()
    
    def bonoSueldo(self):
        self._billetera += self._billetera * 0.1