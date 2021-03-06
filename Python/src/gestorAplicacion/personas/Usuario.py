
class Usuario():
    """
     Usuario : Contiene la informacion de: 
        - ID : int
        - Nombre : String
        - email : String
        - movil : int
        - billetera : int
    Es una clase abstracta con la cual se hara referencia en Empleado y en Comprador
    """
    
    def __init__(self, cc: int = 0, uNombre : str = None, email : str = None, movil: int = 0, billetera: int = 0):

        self._cc = cc
        self._uNombre = uNombre
        self._email = email
        self._movil = movil
        self._billetera = billetera


    # GETTER Y SETTER 


    def getCc(self):
        return self._cc

    def getuNombre(self):
        return self._uNombre

    def getEmail(self):
        return self._email

    def getMovil(self):
        return self._movil

    def setBilletera(self,billetera):
        self._billetera = billetera


    def getBilletera(self):
        return self._billetera
    
    def agregarSaldo(self, dinero):
        self._billetera += dinero