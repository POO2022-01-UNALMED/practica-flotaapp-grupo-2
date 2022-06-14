<<<<<<< HEAD
from src import *

from typing import List  


class Usuario():

    def __init__(self, cc: int=0, uNombre: str=None, email: str=None, movil: int = 0, billetera: int = 0):

        self._cc = cc

        self._uNombre = uNombre

        self._email = email

        self._movil = movil

        self._billetera = billetera
=======

class Usuario():

    def __init__(self, cc: int = 0, uNombre : str = None, email : str = None, movil: int = 0, billetera: int = 0):

        self.cc = cc
        self.uNombre = uNombre
        self.email = email
        self.movil = movil
        self.billetera = billetera

    #def agregarSaldo(self):

    # GETTER Y SETTER 


    def getCc(self):
        return self.cc

    def getuNombre(self):
        return self.uNombre

    def getEmail(self):
        return self.email

    def getMovil(self):
        return self.movil

    def setBilletera(self,billetera):
        self.billetera = billetera


    def getBilletera(self):
        return self.billetera


>>>>>>> master


