"""
Recomendacion de viajes a Usuarios
"""
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