from src import *

from typing import List  


class Usuario():

    def __init__(self, cc: int=0, uNombre: str=None, email: str=None, movil: int = 0, billetera: int = 0):

        self._cc = cc

        self._uNombre = uNombre

        self._email = email

        self._movil = movil

        self._billetera = billetera


