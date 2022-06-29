from gestorAplicacion.personas.Usuario import Usuario
from enum import Enum

class Empleado(Usuario):
    '''
    Empleado : Contiene la informacion de: 
        - ID : int
        - Nombre : String
        - email : String
        - movil : int
        - Sueldo : int
    Es una clase abstracta con la cual se hara referencia en Especialista y Conductor.
    '''

    def __init__(self, cc: int=0, uNombre: str=None, email: str=None, movil: int = 0, sueldo: int = 0):
        super(). __init__(cc, uNombre, email, movil)
        self._sueldo = sueldo

    def renunciar(self):
        self.renunciar()

    def bonoSueldo(self): # Polimorfismo
        self.bonoSueldo()
