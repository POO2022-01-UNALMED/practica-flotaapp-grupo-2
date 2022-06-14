from gestorAplicacion.Usuario import Usuario

class Comprador(Usuario):
    _compradores = []

    def __init__(self,cc: int = 0, uNombre : str = None, email : str = None, movil: int = 0, billetera: int = 0, historicoViajes = None):
        super().__init__(cc, uNombre, email, movil, billetera)
        self._historicoViajes = historicoViajes # -historicoViajes: List(Tiquetes)
        Comprador._compradores.append(self)

    #def buscarTiquete(self):

    #def comprarTiquete(self):

    def getHistocioViaje(self):
        return self._historicoViajes