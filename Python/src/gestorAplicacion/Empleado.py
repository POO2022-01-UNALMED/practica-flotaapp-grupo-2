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