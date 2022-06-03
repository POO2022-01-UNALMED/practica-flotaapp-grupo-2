/*
 * Clase con las funciones de registrar usuario, cambiar o cancelr tiquete, consultar tareas de Especialista y asignar
 * Estructuras: ArrayList, Scanner, LocalDate
 * 
 * @author: Mateo Hechavarria, Juan Pablo Pineda, Miguel Angel Fonseca, Haison Urrutia
 */


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

        }
        System.out.println(" ");
        System.out.println("Dime la CC del conductor que deseas gestionar : ");
        Scanner cond = new Scanner(System.in);
        int conductorcc = cond.nextInt();
        Conductor conductor = new Conductor();
        for(Conductor conductor1 : Conductor.getConductores()){
            if(conductor1.getCc() == conductorcc){ conductor = conductor1;}
        }
        desicionConductor(conductor);
    }

    public static void desicionConductor(Conductor conductor){
        if(conductor.getuNombre().equals("CONDUCTOR NO REGISTRADO")){
            System.out.println(conductor.getuNombre());
            return;
        }
            System.out.println("[4] Visualizar Historial de viajes Asignados \n[5] Asignar un Viaje \n[6] Despedir");
            Scanner aux = new Scanner(System.in);
            switch (aux.nextInt()) {
                case 4: {
                    System.out.println("--- HISTORIAL VIAJES ASIGNADOS ---");
                    for(Viaje viaje: conductor.getHistoriaViajesRealizados()){
                        System.out.println(viaje);
                    }

                } break;
                case 5: {
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
                        ArrayList<Viaje> viajesDisponibles = Viaje.viajesSinConductor();
                        for(Viaje viaje: conductor.getHistoriaViajesRealizados()){
                            if(viaje.getFechaViaje().getYear() == viajesDisponibles.get(num).getFechaViaje().getYear() && viaje.getFechaViaje().getMonthValue() == viajesDisponibles.get(num).getFechaViaje().getMonthValue() && viaje.getFechaViaje().getDayOfMonth() == viajesDisponibles.get(num).getFechaViaje().getDayOfMonth()){
                                System.out.println("Lo siento este conductor ya tiene un viaje para esa fecha");
                                return;
                            }
                        }
                        Asignar.asignarVehiculo(conductor, viajesDisponibles.get(num));
                        System.out.println("VIAJE: " + viajesDisponibles.get(num));
                    }
                }
                break;

                case 6: {
                    Especialista administrador = new Especialista();
                    administrador.despedir(conductor); //System.out.println("EMPLEADO DESPEDIDO");
                    
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
            }

            System.out.println("Dime el ID del viaje que deseas gestionar :  ");
            Scanner tiqueteIdS = new Scanner(System.in);
            int tiqueteID = tiqueteIdS.nextInt();
            if( tiqueteID > viajesActivos.size()){
                System.out.println("VIAJE NO REGISTRADO");
            }
            else{
                gestionarTiquete(viajesActivos.get(tiqueteID));
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
                        if( tiqueteViaje.getViaje().getDestino().getNombre().equals(tiquete.getViaje().getDestino().getNombre()) &&  tiqueteViaje.getViaje().getOrigen().getNombre().equals(tiquete.getViaje().getOrigen().getNombre()) && !tiqueteViaje.getEstado())
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
                    tiquete.setEstado(false);
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
                    tiquete.setEstado(false);
                    tiquete.setComprador(null);
                } else if(tiquete.getViaje().getFechaViaje().isBefore(LocalDate.now())) {
                    System.out.println("La fecha del viaje es muy cercana, por lo que solo podremos devolverle el 30% del valor de su Tiquete");
                    tiquete.getComprador().agregarSaldo(tiquete.getValor()*0.3);
                    tiquete.getComprador().eliminarTiqueteHistoria(tiquete);
                    tiquete.setEstado(false);
                    tiquete.setComprador(null);
                } else{
                    System.out.println("El viaje ya se a realizado, no se puede hacer devuelta de su dinero");

                }

            }
        }
    }

    public static void gestionarEspecialistas(){
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
        System.out.println(" ");
        System.out.println("Dime la CC del especialista que deseas gestionar : ");
        Scanner espe = new Scanner(System.in);
        int especialistacc = espe.nextInt();
        Especialista especialista = new Especialista();
        for(Especialista especialista1 : Especialista.getEspecialistas()){
            if(especialista1.getCc() == especialistacc){ especialista = especialista1;}
        }
        desicionEspecialistas(especialista);
    }


    public static void visualizarEspecialista(Especialista especialista) {
        System.out.println(" ");
        System.out.println(especialista.getEspecialidad().toString() + " -  CC: " + especialista.getCc() + " - Nombre: " + especialista.getuNombre());
        System.out.println("Cantidad de vehiculos revisados: " + especialista.getHistorialVehiculosRevisados().toArray().length);
    }

    public static void desicionEspecialistas(Especialista especialista){
        if(especialista.getuNombre().equals("ESPECIALISTA NO REGISTRADO")){
            System.out.println(especialista.getuNombre());
            return;
        }
        System.out.println("[4] Visualizar Historial de viajes Asignados \n[5] Asignar un Viaje \n[6] Despedir");
            Scanner aux = new Scanner(System.in);
            switch (aux.nextInt()) {
                case 4: {
                    for(Vehiculo vehiculo: especialista.getHistorialVehiculosRevisados()){
                        System.out.println(vehiculo.getPlaca());
                    }

                } break;
                case 5: {
                    System.out.println("Tipo Revision: " + especialista.getEspecialidad().toString());
                    asignarVehiculoEmpleados(especialista);
                }
                break;

                case 6: {
                    Especialista administrador = new Especialista();
                    administrador.despedir(especialista); //System.out.println("EMPLEADO DESPEDIDO");
                }
            }
    }

    public static void asignarVehiculoEmpleados(Empleado empleado){

            for(int i = 0 ;i < Vehiculo.getVehiculos().size() ; i++){
                System.out.println("id : ["+i+"] = " + Vehiculo.getVehiculos().get(i).getPlaca());
            }
            System.out.println("Vehiculo a Asignar: ");
            Scanner cambio = new Scanner(System.in);
            int vehiculo = cambio.nextInt();
            Asignar.asignarVehiculo((Especialista) empleado, Vehiculo.getVehiculos().get(vehiculo));
            System.out.println("VEHICULO: " + Vehiculo.getVehiculos().get(vehiculo).getPlaca() + " Estara en revision.");
    }
}


