import sys
sys.path.append("../practica-flotaapp-grupo-2/Python/src")

from gestorAplicacion.Comprador import Comprador
from gestorAplicacion.Tiquete import Tiquete
from gestorAplicacion.Ciudad import Ciudad
from gestorAplicacion.Vehiculo import Vehiculo
from gestorAplicacion.Silla import Silla, Ubicacion
from gestorAplicacion.Viaje import Viaje
from gestorAplicacion.Conductor import Conductor, Categoria
from gestorAplicacion.Especialista import Especialidad, Especialista
from Funcionalidades.Asignar import Asignar


from datetime import datetime
from datetime import timedelta

class Gestionar():

    @staticmethod
    def desicionEspecialista(especialista):
        if especialista.getuNombre() == "ESPECIALISTA NO REGISTRADO" :
            print(especialista.getuNombre())
            return 
                
        print("[4] Visualizar Historial de vehiculos Asignados \n[5] Asignar un Vehiculo \n[6] Despedir")
        aux2 = int(input())
        if aux2 == 4:
            if especialista.getHistorialVehiculosRevisados() == None: 
                return

            for vehiculo in especialista.getHistorialVehiculosRevisados():
                print(f'PLACA VEHICULO : {vehiculo.getPlaca()}')
        elif aux2 == 5:
            print(f"Tipo Revision: {especialista.getEspecialidad()}");
            for i in range(len(Vehiculo.getVehiculos())):
                print(f'[{i}] : {Vehiculo.getVehiculos()[i].getPlaca()}')
            idVehiculo = int(input("Vehiculo a asignar: "))
            Asignar.asignarVehiculoEspecialista(especialista,Vehiculo.getVehiculos()[idVehiculo])
            especialista.revisionVehiculo(Vehiculo.getVehiculos()[idVehiculo])
        elif aux2 == 6:
            administrador = Especialista()
            print(administrador.despedir(especialista))

    @staticmethod
    def visualizarEspecialista(especialista):
        print(" ")
        print(f'{especialista.getEspecialidad()} -  CC: {especialista.getCc()} - Nombre: {especialista.getuNombre()}');
        if especialista.getHistoricoVehiculosRevisados() == None :
            print(f"Cantidad de vehiculos revisados: 0")
        else:   
            print(f"Cantidad de vehiculos revisados: {len(especialista.getHistoricoVehiculosRevisados())}")

    @classmethod
    def gestionarEspecialistas(cls):
        print("----- G E S T I O N A R   E S P E C I A L I S T A S -----")
        print(" ")
        print("[1] Electrico, [2] Mecanico, [3] Silleteria")
        especialidades = [Especialidad.ELECTRICO, Especialidad.MECANICO, Especialidad.SILLETERIA]
        aux = int(input())
        for especialista in Especialista.getEspecialistas():
            if especialista.getEspecialidad() == especialidades[aux-1]:
                Gestionar.visualizarEspecialista(especialista)


        print("\n Dime la CC del especialista que deseas gestionar : ");
        espe = int(input())
        especialistaAux = Especialista()
        for especialista1 in Especialista.getEspecialistas():
            if especialista1.getCc() == espe:
                especialistaAux = especialista1
        Gestionar.desicionEspecialista(especialistaAux)

    @classmethod
    def gestionarConductores(cls):
        for conductor in Conductor.getConductores():
            print(" ")
            print("CC:" + str(conductor.getCc()) + " - Nombre: " + conductor.getuNombre())
            print("Cantidad de Viajes asigandos: " + str(len(conductor.getHistoricoViajesRealizados())))

        print(" ")
        print("Dime la CC del conductor que deseas gestionar : ")
        cond = int(input())
        conductor = Conductor()
        for conductor1 in Conductor.getConductores():
            if(conductor1.getCc() == cond):
                conductor = conductor1
        
        Gestionar.desicionConductor(conductor)

    @staticmethod
    def desicionConductor(conductor):
        if(conductor.getuNombre() == "CONDUCTOR NO REGISTRADO"):
            print(conductor.getuNombre())
            pass
        print("[4] Visualizar Historial de viajes Asignados \n[5] Asignar un Viaje \n[6] Despedir")
        aux = int(input())
        while True:
            if(aux == 4):
                print("--- HISTORIAL VIAJES REALIZADOS ---")
                for viaje in conductor.getHistoricoViajesRealizados():
                    print(viaje)
                break
                
            elif(aux == 5):
                if(len(Viaje.viajeSinConductor()) == 0):
                    print("Actualmente todos los viajes tienen Conductor")
                    break
                else:
                    for i in range(len(Viaje.viajeSinConductor())):
                        print(" ")
                        print("id : [" + str(i) +"] =" + Viaje.viajeSinConductor()[i].__str__())
                
                print(" ")
                des = int(input())
                viajesDisponibles = Viaje.viajeSinConductor()
                for viaje in conductor.getHistoricoViajesRealizados():
                    if(viaje.getFechaViaje().strftime("%Y") == viajesDisponibles[des].getFechaViaje().strftime("%Y") and viaje.getFechaViaje().strftime("%m") == viajesDisponibles[des].getFechaViaje().strftime("%m") and viaje.getFechaViaje().strftime("%d") == viajesDisponibles[des].getFechaViaje().strftime("%d")):
                        print("Lo siento este conductor ya tiene un viaje para esta fecha")
                    break   
                Asignar.asignarVehiculoConductor(conductor, viajesDisponibles[des])
                print("VIAJE: " + viajesDisponibles[des].__str__())
                break

            elif(aux == 6):
                administrador = Especialista()
                administrador.despedir(conductor)
                print("EMPLEADO DESPEDIDO")
                break

            else:
                break

    @staticmethod
    def comprarTiqueteTerminal():
        compradorBase = Comprador(0, "FLOTAAPPCOMPRADOR", "FLOTA@app.com", 999)
        nombreCiudad = input("Ciudad a la que desea viajar: ")
        finalTiquete = Tiquete()
        for viaje in Viaje.getViajes():
            #No esta entrando en este if de aquí abajo, en el main, me pide el id, pero no me muestra los tiquetes disponibles
            #El problema está en la comparación de los destinos desafortunadamente no lo supe solucionar! :(
            if (viaje.getDestino().getNombre() == nombreCiudad and viaje.getOrigen().getNombre() == "MEDELLIN" and viaje.getFechaViaje() > datetime.now()):
                for i in range(len(Viaje.tiquetesDisponibles())):
                    print("id : [" +  str(i)  + "] = " +  viaje.tiquetesDisponibles()[i].__str__())

            cambio = int(input("ingrese el id: "))
            if(cambio >= len(viaje.tiquetesDisponibles())):
                print("ID NO VALIDO")
                return finalTiquete

            else:
                tiquete = viaje.tiquetesDisponibles()[cambio]
                Asignar.asignarTiquete(compradorBase, tiquete)
                print(tiquete)
                return tiquete

        print("NO HAY TIQUETES DISPONIBLES PARA EL VIAJE QUE DESEAS");
        return finalTiquete

