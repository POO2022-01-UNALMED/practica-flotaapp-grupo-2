<<<<<<< HEAD
from src import *
from typing import List 
import Usuario

                        
class Empleado(Usuario):
    
    
    def __init__(self, cc: int=0, uNombre: str=None, email: str=None, movil: int = 0, sueldo: int = 0):
        super(). __init__(cc, uNombre, email, movil)
        self._sueldo = sueldo
    

    def renunciar(self):
        self.renunciar()
    
    def bonoSueldo(self): # Polimorfismo
        self.bonoSueldo()
    

=======
from gestorAplicacion.Usuario import Usuario
 #Superclase Empleado

class Empleado(Usuario):
    def __init__(self, cc, uNombre, email, movil, billetera):
        super(). __init__(cc, uNombre, email, movil, billetera)
        self._sueldo = 0

    def renunciar(claseR):
        claseR.renunciar()
    
    def bonoSueldo(self):
        self._billetera += self._billetera * 0.1
>>>>>>> master
