package uiMain.funcionalidades;

import gestorAplicacion.*;

import java.time.LocalDate;
import java.util.ArrayList;
import java.util.Scanner;

public class Gestionar {
    public static void gestionarConductores(){
    	for(Conductor conductor: Conductor.getConductores()) {
            System.out.println(" ");
            System.out.println("CC: " + conductor.getCc() + " - Nombre: " + conductor.getuNombre());
            System.out.println("Cantidad de Viajes asignados: " + conductor.getHistoriaViajesRealizados().toArray().length);
            if (conductor.getHistoriaViajesRealizados().isEmpty()) {
                System.out.println("[4] Asignar un Viaje, [5] Despedir");
                Scanner aux = new Scanner(System.in);
                switch (aux.nextInt()) {
                    case 4: {
                        if (Viaje.viajesSinConductor().isEmpty()) {
                            System.out.println("Actualmente todos los viajes tienen Conductor");
                        } else {
                            for (int i = 0; i < Viaje.viajesSinConductor().size(); i++) {
                                System.out.println(" ");
                                System.out.println("id : [" + i + "] = " + Viaje.viajesSinConductor().get(i).toString());
                            }
                            System.out.println(" ");
                            Scanner des = new Scanner(System.in);
                            int num = des.nextInt();
                            Asignar.asignarViaje(conductor, Viaje.viajesSinConductor().get(num));
                            System.out.println("VIAJE: " + Viaje.viajesSinConductor().get(num));
                        }
                    }
                    break;

                    case 5: {
                        Administrador.despedir(conductor);
                    }
                }
            }
        }
    }


    public static void gestionarViajes(int cc){
        System.out.println("----- G E S T I O N A R   V I A J E S -----");

            Comprador comprador = new Comprador();
            for(Comprador comprador1 : Comprador.getCompradores()){
                if(comprador1.getCc() == cc){ comprador = comprador1;}
            }
            System.out.println("CC : " + comprador.getCc() + " - " + comprador.getuNombre());
            ArrayList<Tiquete> viajesActivos = new ArrayList<>();
            for(Tiquete tiquete : comprador.getHistoricoViajes()){
                if(tiquete.getViaje().getFechaViaje().isAfter(LocalDate.now())){
                    viajesActivos.add(tiquete);

                }
            }
            for(int i = 0; i < viajesActivos.size() ; i++){
                System.out.println("id : ["+i+"] = " + viajesActivos.get(i).toString() );
                gestionarTiquete(viajesActivos.get(i));
            }
        }

    public static void gestionarEspecialistas(){
        System.out.print("\033[H\033[2J");
        System.out.flush();
        System.out.println("----- G E S T I O N A R   E S P E C I A L I S T A S -----");
        System.out.println(" ");
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

    public static void gestionarTiquete(Tiquete tiquete){
        System.out.println("[1] Cambiar Tiquete, [2] Cancelar Tiquete");
        Scanner aux = new Scanner(System.in);
        switch (aux.nextInt()) {
            case 1: {
                ArrayList<Tiquete> tiquetesDisponibes = new ArrayList<>();
                for(Viaje viaje : Viaje.getViajes()){
                    for(Tiquete tiqueteViaje : viaje.getAllTiquetes()){
                        if( tiqueteViaje.getViaje().getDestino() == tiquete.getViaje().getDestino() &&  tiqueteViaje.getViaje().getOrigen() == tiquete.getViaje().getOrigen() && !tiqueteViaje.getSillaTiquete().getEstado())
                        {
                            tiquetesDisponibes.add(tiqueteViaje);
                        }
                    }
                }
                for(int i = 0; i < tiquetesDisponibes.size() ; i++){
                    System.out.println("id : ["+i+"] = " + tiquetesDisponibes.get(i).toString() );
                }
                if(tiquetesDisponibes.isEmpty()){
                    System.out.println("Lo siento, no hay Tiquetes disponibles para esa fecha - valor - origen - destino");
                } else {
                    System.out.println("Escoge un tiquete por el cual cambiarlo");
                    Scanner cambio = new Scanner(System.in);
                    int auxnum = cambio.nextInt();
                    Asignar.asignarTiquete( tiquete.getComprador() , tiquetesDisponibes.get(auxnum));
                    tiquete.getComprador().eliminarTiqueteHistoria(tiquete);
                    tiquete.getSillaTiquete().setEstado(false);
                    tiquete.setComprador(null);
                    System.out.println(tiquetesDisponibes.get(auxnum));
                }
            }
            break;

            case 2: {
                if(tiquete.getViaje().getFechaViaje().plusDays(7).isAfter(tiquete.getViaje().getFechaViaje())){
                    System.out.println("El tiquete a sido cancelado y su dinero devuelto");
                    tiquete.getComprador().agregarSaldo(tiquete.getValor());
                    tiquete.getComprador().eliminarTiqueteHistoria(tiquete);
                    tiquete.getSillaTiquete().setEstado(false);
                    tiquete.setComprador(null);
                } else if(tiquete.getViaje().getFechaViaje().isBefore(LocalDate.now())) {
                    System.out.println("La fecha del viaje es muy cercana, por lo que solo podremos devolverle el 30% del valor de su Tiquete");
                    tiquete.getComprador().agregarSaldo(tiquete.getValor()*0.3);
                    tiquete.getComprador().eliminarTiqueteHistoria(tiquete);
                    tiquete.getSillaTiquete().setEstado(false);
                    tiquete.setComprador(null);
                } else{
                    System.out.println("El viaje ya se a realizado, no se puede hacer devuelta de su dinero");

                }

            }
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
                    System.out.println("VEHICULO: " + Vehiculo.getVehiculoRevisar().getPlaca());
                }
                break;

                case 5: {
                    Administrador.despedir(especialista);
                }
            }
        }
    }
}


