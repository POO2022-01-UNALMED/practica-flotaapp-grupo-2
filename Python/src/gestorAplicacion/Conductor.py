from src import *
from typing import List  
import Empleado
import Categoria

class Conductor(Empleado):
    
    __historiaViajesRealizados = []
    __conductores = []

    def __init__(self, cc = 0, uNombre: str = None, email: str = None, movil: int = None, sueldo=0, categoria: Categoria = None): # categoria = Categoria(categoria)
        super().__init__(cc, uNombre, email, movil, sueldo)
        self._categoria = categoria
        Conductor.__conductores.append(self)
    
    def anadirViajeHistoria(self, viaje=Viaje(viaje)):
        self.__historiaViajesRealizados.append(viaje)
    
    ## M E T O D O S ##

    
    def bonoSueldo(self):
        sueldo += sueldo * 0.15
        superConductor = None
        for  cadaConductor in Conductor.__conductores:
             if superConductor == None:
                    superConductor = cadaConductor
             elif len(cadaConductor.__historiaViajesRealizados) > len(superConductor.__historiaViajesRealizados):
                 superConductor = cadaConductor
             else:
                 continue
        
        if superConductor != None:
            sueldo += sueldo * 0.1    # 10% mas de bono si es el conductor con mas viajes realizados     
    
    
    def renunciar(self):
        Conductor.__conductores.remove(self)
    
    ## G E T  A N D  S E T ##
    
    def setCategoria(self, categoria: Categoria = None):
        self._categoria = categoria
    
    @classmethod()
    def getConductores(cls):
        return Conductor.__conductores
    
    def getHistoricoViajesRealizados(self):
        return self.__historiaViajesRealizados
    
    def __str__(self): 
        return "CC: {} \n Nombre {} \n Sueldo: {} \n Categoria : {} \n Viajes realizado : {}".format(self._cc, self._uNombre, self._sueldo, self._categoria,self.__historiaViajesRealizados) 
               

