import sys
sys.path.append("../practica-flotaapp-grupo-2/Python/src")

from gestorAplicacion.Comprador import Comprador
from gestorAplicacion.Ciudad import Ciudad
from gestorAplicacion.Vehiculo import Vehiculo
from gestorAplicacion.Silla import Silla, Ubicacion
from gestorAplicacion.Viaje import Viaje
from gestorAplicacion.Conductor import Conductor, Categoria
from gestorAplicacion.Especialista import Especialidad, Especialista


class Gestionar():

    @staticmethod
    def desicionEspecialista(especialista):
        if especialista.getuNombre() == "ESPECIALISTA NO REGISTRADO" :
            print(especialista.getuNombre())
            return 
        
        print("[4] Visualizar Historial de viajes Asignados \n[5] Asignar un Viaje \n[6] Despedir")
        aux2 = int(input())
        if aux2 == 4:
            for vehiculo in especialista.getHistorialVehiculosRevisados():
                print(vehiculo.getPlaca())
        elif aux2 == 5:
            print(f"Tipo Revision: {especialista.getEspecialidad()}");
            #Asignar.asignarVehiculoEmpleados(especialista);
        elif aux2 == 6:
            administrador = Especialista()
            print(administrador.despedir(especialista))

    @staticmethod
    def visualizarEspecialista(especialista):
        print(" ")
        print(f'{especialista.getEspecialidad()} -  CC: {especialista.getCc()} - Nombre: {especialista.getuNombre()}');
        print(f"Cantidad de vehiculos revisados: {len(especialista.getHistorialVehiculosRevisados())}")

    @classmethod
    def gestionarEspecialistas(cls):
        print("----- G E S T I O N A R   E S P E C I A L I S T A S -----")
        print(" ")
        print("[1] Electrico, [2] Mecanico, [3] Silleteria")
        especialidades = [Especialidad.ELECTRICO, Especialidad.MECANICO, Especialidad.ADMINISTRADOR]
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