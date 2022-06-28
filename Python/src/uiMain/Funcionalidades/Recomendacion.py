"""
Recomendacion de viajes a Usuarios
"""
<<<<<<< Updated upstream
from gestorAplicacion.viajes.Ciudad import Ciudad
from gestorAplicacion.personas.Comprador import Comprador
from gestorAplicacion.personas.Usuario import Usuario
from gestorAplicacion.viajes.Viaje import Viaje
from gestorAplicacion.viajes.Tiquete import Tiquete



class Recomendacion():
    
    @staticmethod
    def recomendarViaje(cc: int):
        __visitadas = {}
        print("----- R E C O M E N D A R   V I A J E -----" + "\n")
        for comprador in Comprador.getCompradores():
            if comprador.getCc() == cc:
                masVisitada = Ciudad.getCiudades()[0]
                if comprador.getHistorioViaje() is None:
                    return 
                elif len(comprador.getHistorioViaje()) > 0:
                    for cadaTiquete in comprador.getHistorioViaje():
                        destino = cadaTiquete.getViaje().getDestino()
                        if destino in __visitadas:
                            __visitadas[destino] += 1
                        else:
                            __visitadas[destino] = 1

                    masVisitada = None
                    puntaje = 0
                
                    for cadaCiudad in __visitadas.keys():
                        puntajeInterno = __visitadas[cadaCiudad]*0.8 + cadaCiudad.getPuntaje() * 0.2
                        if puntajeInterno >= puntaje:
                            masVisitada = cadaCiudad
                            puntaje = puntajeInterno
                
                else:
                    masVisitada = None
                    puntaje = 0
                    
                    for cadaCiudad in Ciudad().getCiudades():
                        if cadaCiudad.getPuntaje() >= puntaje:
                            masVisitada = cadaCiudad
                            puntaje = cadaCiudad.getPuntaje()

                return print(f"Te recomendamos viajar a: {masVisitada.__str__()} \n")

        print("ID DE USUARIO NO ENCONTRADO")
=======
from gestorAplicacion.Ciudad import Ciudad
from gestorAplicacion.Comprador import Comprador
from gestorAplicacion.Usuario import Usuario
from gestorAplicacion.Viaje import Viaje
from gestorAplicacion.Tiquete import Tiquete



class Recomendacion():
    __visitadas = {}
    
    
    @staticmethod()
    def recomendarViaje(cls, cc: int = 0):
        print("----- R E C O M E N D A R   V I A J E -----" + "\n")
        recomendadisima = Ciudad()
        aRecomendar = Comprador()
        for comprador in Comprador.getComprador():
            if comprador.getCC == cc:
                aRecomendar = comprador
                
            if (aRecomendar in Comprador().getComprador()) and (len(aRecomendar.getHistocioViaje()) > 0 and aRecomendar != None):
                for cadaTiquete in aRecomendar.getHistocioViaje():
                    if not Recomendacion().__visitadas:
                        Recomendacion.__visitadas.setdefault(cadaTiquete().getViaje().getDestino(), 1)
                    elif cadaTiquete().getViaje().getDestino() in Recomendacion().__visitadas:
                        Recomendacion().__visitadas[cadaTiquete().getViaje().getDestino()] = Recomendacion().__visitadas.get(Recomendacion().__visitadas[cadaTiquete().getViaje().getDestino()] + 1) #Agrega 1 a la ciudad
                    else:
                        Recomendacion.__visitadas.setdefault(cadaTiquete().getViaje().getDestino(), 1)
                masVisitada = None
                visitas = 0
            
                for cadaCiudad in Recomendacion().__visitadas.keys():
                    if Recomendacion().__visitadas.get(cadaCiudad) > visitas:
                        masVisitada = cadaCiudad
                        visitas = Recomendacion().__visitadas.get(cadaCiudad)
            
                recomendadisima = masVisitada
            else:
                masVisitada: Ciudad = None
                visitas = 0
                
                for cadaCiudad in Ciudad().getCiudades():
                    if cadaCiudad.getNumVisitantes() > visitas:
                        masVisitada = cadaCiudad
                        visitas = cadaCiudad.getNumVisitantes()
                recomendadisima = masVisitada
            print("Te recomendamos viajar a: " + recomendadisima.__str__())
                        
              
                        
                
        
        
>>>>>>> Stashed changes
