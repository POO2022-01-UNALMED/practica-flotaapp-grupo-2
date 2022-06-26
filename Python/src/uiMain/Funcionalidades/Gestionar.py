from gestorAplicacion.personas.Comprador import Comprador
from gestorAplicacion.viajes.Tiquete import Tiquete
from gestorAplicacion.viajes.Vehiculo import Vehiculo
from gestorAplicacion.viajes.Viaje import Viaje
from gestorAplicacion.personas.Conductor import Conductor
from gestorAplicacion.personas.Especialista import Especialidad, Especialista
from uiMain.Funcionalidades.Asignar import Asignar


from datetime import datetime
from datetime import timedelta

class Gestionar():
    
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

    @staticmethod
    def desicionEspecialista(especialista):
        if especialista.getuNombre() == "ESPECIALISTA NO REGISTRADO" :
            print(especialista.getuNombre())
            return 
                
        print("[4] Visualizar Historial de vehiculos Asignados \n[5] Asignar un Vehiculo \n[6] Despedir")
        aux2 = int(input())
        if aux2 == 4:
            if especialista.getHistoricoVehiculosRevisados() == None: 
                return

            for vehiculo in especialista.getHistoricoVehiculosRevisados():
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
            return 
        print("[4] Visualizar Historial de viajes Asignados \n[5] Asignar un Viaje \n[6] Despedir")
        aux = int(input())
        if(aux == 4):
            print("--- HISTORIAL VIAJES REALIZADOS ---")
            for viaje in conductor.getHistoricoViajesRealizados():
                print(viaje)
            
        elif(aux == 5):
            if(len(Viaje.viajeSinConductor()) == 0):
                print("Actualmente todos los viajes tienen Conductor")
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
                    return 
            Asignar.asignarVehiculoConductor(conductor, viajesDisponibles[des])
            print("VIAJE: " + viajesDisponibles[des].__str__())

        elif(aux == 6):
            administrador = Especialista()
            administrador.despedir(conductor)
            print("EMPLEADO DESPEDIDO")

    @staticmethod
    def comprarTiqueteTerminal():
        compradorBase = Comprador(0, "FLOTAAPPCOMPRADOR", "FLOTA@app.com", 999)
        nombreCiudad = input("Ciudad a la que desea viajar: ")
        finalTiquete = Tiquete()
        for viaje in Viaje.getViajes():
            if viaje.getDestino().getNombre() == nombreCiudad and viaje.getOrigen().getNombre() == "MEDELLIN" and viaje.getFechaViaje() > datetime.now():
                for i in range(len(viaje.tiquetesDisponibles())):
                    print("id : [" +  str(i)  + "] = {viaje.tiquetesDisponibles()[i].__str__()}")

                cambio = int(input("ingrese el id: "))
                if(cambio >= len(viaje.tiquetesDisponibles())):
                    print("ID NO VALIDO")
                    return finalTiquete

                else:
                    tiquete = viaje.tiquetesDisponibles()[cambio]
                    Asignar.asignarTiquete(compradorBase, tiquete)
                    print(tiquete)
                    return tiquete

        print("NO HAY TIQUETES DISPONIBLES PARA EL VIAJE QUE DESEAS")
        return finalTiquete

    @staticmethod
    def gestionarTiquete(tiquete: Tiquete = None):
        print("1] Cambiar Tiquete, [2] Cancelar Tiquete")
        aux = int(input())
        if aux == 1:
            tiquetesDisponibles = []
            for viaje in Viaje.getViajes():
                for tiqueteViaje in viaje.getAllTiquetes():
                    if tiqueteViaje.getViaje().getDestino().getNombre() == tiquete.getViaje().getDestino().getNombre() and tiqueteViaje.getViaje().getOrigen().getNombre() == tiquete.getViaje().getOrigen().getNombre() and  not tiqueteViaje.getEstado():
                        tiquetesDisponibles.append(tiqueteViaje)
            
            for i in range(0, len(tiquetesDisponibles)-1):
                print(f"id : {i} = {tiquetesDisponibles[i].__str__}")
                
                if tiquetesDisponibles is None:
                    print("Lo siento, no hay Tiquetes disponibles para esa fecha - valor - origen - destino")
                else:
                    print("Escoge un tiquete por el cual cambiarlo")
                    auxnum = int(input())
                    Asignar().asignarTiquete(tiquete.getComprador(), tiquetesDisponibles[auxnum])
                    tiquete.getComprador().eliminarTiqueteHistoria(tiquete)
                    tiquete.setEstado(False)
                    tiquete.setComprador(None)
                    print(tiquetesDisponibles[auxnum])
        elif aux == 2:
            if (tiquete.getViaje().getFechaViaje() + timedelta(days=7)) >  datetime().now(): 
                print("El tiquete a sido cancelado y su dinero devuelto")
                tiquete.getComprador().agregarSaldo(tiquete.getValor())
                tiquete.getComprador().eliminarTiqueteHistoria(tiquete)
                tiquete.setEstado(False)
                tiquete.setComprador(None)
            elif tiquete.getViaje().getFechaViaje() > datetime().now() and tiquete.getViaje().getFechaViaje() < (tiquete.getViaje().getFechaViaje() + timedelta(days=7)): 
                print("La fecha del viaje es muy cercana, por lo que solo podremos devolverle el 30% del valor de su Tiquete")
                tiquete.getComprador().agregarSaldo(tiquete.getValor()*0.3)
                tiquete.getComprador().eliminarTiqueteHistoria(tiquete)
                tiquete.setEstado(False)
                tiquete.setComprador(None)
            else:
                print("El viaje ya se a realizado, no se puede hacer devuelta de su dinero")
   
    @staticmethod
    def gestionarViajes(cc: int=0): #Se deja los print para cambiarlos por return posteriormente
        print("----- G E S T I O N A R   V I A J E S -----")
        comprador = Comprador()
        for comprador1 in Comprador.getCompradores():
            if comprador1.getCC() == cc:
                comprador = comprador1
        
        print("CC: "+ comprador.getCC + " Nombre: " + comprador.getuNombre())
        viajesActivos = []
        for tiquete in comprador.getHistorioViaje():
            if tiquete.getViaje().getFechaViaje() < datetime.now():
                viajesActivos.append(tiquete)
        
        for i in range(0, len(viajesActivos)-1):
            print(f"id : {i} = {viajesActivos[i].__str__()} \n")
        
        print("Dime el ID del viaje que deseas gestionar :  ")
        tiqueteID = int(input())
        
        if tiqueteID >= len(viajesActivos) or tiqueteID < 0:
            print("VIAJE NO REGISTRADO")
        else:
            gestionarTiquete(viajesActivos[tiqueteID]) 
        
    

                
                    
                    
    

