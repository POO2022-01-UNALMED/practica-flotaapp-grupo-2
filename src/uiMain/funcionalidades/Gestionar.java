package uiMain.funcionalidades;

import gestorAplicacion.*;

import java.util.ArrayList;
import java.util.Locale;
import java.util.Scanner;

public class Gestionar {
    public void gestionarCompradores(){

    }

    public void gestionarViajes(){

    }

    public static void gestionarEspecialistas(){
        System.out.println("[1] Electrico, [2] Mecanico, [3] Silleteria");
        Scanner aux = new Scanner(System.in);
        int uno = aux.nextInt();
        switch (uno){

            case 1: {
                for(Especialista especialista : Especialista.getEspecialistas()){
                    if(especialista.getEspecialidad() == Especialidad.ELECTRICO){
                        Gestionar.visualizarEspecialista(especialista);
                    }
                } break;
            }
            case 2:{
                for(Especialista especialista : Especialista.getEspecialistas()){
                    if(especialista.getEspecialidad() == Especialidad.MECANICO){
                        Gestionar.visualizarEspecialista(especialista);
                    }
                } break;
            }
            case 3:{
                for(Especialista especialista : Especialista.getEspecialistas()){
                    if(especialista.getEspecialidad() == Especialidad.SILLETERIA){
                        Gestionar.visualizarEspecialista(especialista);
                    }
                }
            }break;
        }
    }

    public static void visualizarEspecialista(Especialista especialista) {
        System.out.println(" ");
        System.out.println(especialista.getEspecialidad().toString() + " -  CC: " + especialista.getCc() + " - Nombre: " + especialista.getuNombre());
        System.out.println("Cantidad de vehiculos revisados: " + especialista.getHistorialVehiculosRevisados().toArray().length);
        if (especialista.getHistorialVehiculosRevisados().isEmpty()) {
            System.out.println("[4] Asignar un vehiculo a revisar, [5] Despedir");
            Scanner aux = new Scanner(System.in);
            switch (aux.nextInt()) {
                case 4: {
                    System.out.println("Tipo Revision: " + especialista.getEspecialidad().toString() + " - La revision se realizara prontemente");
                    Asignar.asignarVehiculo(especialista, Vehiculo.getVehiculoRevisar());
                }
                break;

                case 5: {
                    Administrador.despedir(especialista);
                }
            }
        }
    }
}


