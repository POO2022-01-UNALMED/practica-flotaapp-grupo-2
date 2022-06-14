from gestorAplicacion.Usuario import Usuario
 #Superclase Empleado

class Empleado(Usuario):
    def __init__(self, cc: int=0, uNombre: str=None, email: str=None, movil: int = 0, sueldo: int = 0):
        super(). __init__(cc, uNombre, email, movil)
        self._sueldo = sueldo

    def renunciar(self):
        self.renunciar()

    def bonoSueldo(self): # Polimorfismo
        self.bonoSueldo()