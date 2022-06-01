package uiMain.funcionalidades;
import gestorAplicacion.Ciudad;
import gestorAplicacion.Comprador;
import gestorAplicacion.Tiquete;
import gestorAplicacion.Viaje;

import java.lang.reflect.Array;
import java.time.LocalDate;
import java.util.ArrayList;
import java.util.Scanner;

import java.io.IOException;

public class AdminViaje {
    private int idEmpresa;

    public static Tiquete comprarTiqueteTerminal(){
        Comprador compradorBase = new Comprador(0, "FLOTAAPPCOMPRADOR", "FLOTA@app.com", 999);
        System.out.println("Ciudad a la que desea viajar: ");
        Scanner aux = new Scanner(System.in);
        String nombreCiudad = aux.nextLine();
        Tiquete finalTiquete = new Tiquete();
        for(Viaje viaje : Viaje.getViajes()){
            if(viaje.getDestino().getNombre().equals(nombreCiudad) && viaje.getOrigen().getNombre() == "MEDELLIN" && viaje.getFechaViaje().isAfter(LocalDate.now())){
                for(int i = 0; i < viaje.getAllTiquetes().size() ; i++){
                    System.out.println("id : ["+i+"] = " + viaje.getAllTiquetes().get(i).toString() );
                }
                Scanner cambio = new Scanner(System.in);
                int auxnum = cambio.nextInt();
                Tiquete tiquete = viaje.getAllTiquetes().get(auxnum);

                Asignar.asignarTiquete( compradorBase , tiquete);
                tiquete.setComprador(null);
                System.out.println(tiquete);
                return tiquete;
            }
        }
        return finalTiquete;
    }


    public static void visualizarEstadisticas(){
        System.out.println("----- V I S U A L I Z A R   E S T A D I S T I C A S -----");
        for(Ciudad ciudad : Ciudad.getCiudades()){
            System.out.println(" ");
            System.out.println("id: " + ciudad.getId() + " - Nombre: "+ciudad.getNombre());
            System.out.println("Numero de Visitante: "+ ciudad.getNumVisitantes());
            int allSillasDisponiblesViajes = 0;
            for(Viaje viaje : Viaje.getViajes()){
                if (viaje.getDestino() == ciudad && viaje.getDestino() != null){
                    System.out.println(" ");
                    allSillasDisponiblesViajes += viaje.getAllTiquetes().size();
                    System.out.println("    Viaje: "+ viaje.getId() + " - Origen: " + viaje.getOrigen() + " - Destino: " + viaje.getDestino() );

                    float porcentaje = ((viaje.getVehiculo().getSillas().size() - viaje.getVehiculo().sillasDisponibles().size()) * 100 )/viaje.getVehiculo().getSillas().size();
                    System.out.println("    Promedio de ocupacion: " + porcentaje + " %");
                    evaluarPorcentajeOcupacion(viaje, porcentaje);


                }
            }
        }
    }

    public static Viaje evaluarPorcentajeOcupacion(Viaje viaje, float porcentaje){
        if (porcentaje >= 85){
            viaje.aumentarFrecuencia(1);
            return viaje;
        }else if(porcentaje >= 40 && porcentaje < 60){
            viaje.disminuirFrecuencia(2);
            //APLICAR LO DEL BONO
            return viaje;
        }else if(porcentaje < 10){
            System.out.println("[1] Eliminar Viaje, [2] Tener Fé ");
            Scanner aux = new Scanner(System.in);
            int propuesta = aux.nextInt();
            if ( propuesta == 1) {
                viaje.eliminarViaje();
            }else{
                System.out.println("Esperemos que no genere muchas Perdidas");
            }
        }
        return viaje;
    }
}
