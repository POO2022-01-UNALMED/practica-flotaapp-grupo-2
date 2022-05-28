package uiMain.funcionalidades;
import gestorAplicacion.Ciudad;
import gestorAplicacion.Viaje;

import java.util.Scanner;

public class AdminViaje {
    private int idEmpresa;

    public static void visualizarEstadisticas(){
        System.out.println(" ");
        System.out.println("----- V I S U A L I Z A R   E S T A D I S T I C A S -----");
        for(Ciudad ciudad : Ciudad.getCiudades()){
            System.out.println(" ");
            System.out.println("id: " + ciudad.getId() + " - Nombre: "+ciudad.getNombre());
            System.out.println("Numero de Visitante: "+ ciudad.getNumVisitantes());
            int allSillasDisponiblesViajes = 0;
            for(Viaje viaje : Viaje.getViajes()){
                if (viaje.getDestino().getNombre() == ciudad.getNombre()){
                    System.out.println(" ");
                    allSillasDisponiblesViajes += viaje.getAllTiquetes().size();
                    System.out.println("Viaje: "+ viaje.getId() + " - Origen: " + viaje.getOrigen() + " - Destino: " + viaje.getDestino() );

                    float porcentaje = ((viaje.getVehiculo().getSillas().size() - viaje.getVehiculo().sillasDisponibles().size())*100)/viaje.getVehiculo().getSillas().size();
                    System.out.println("Promedio de ocupacion: " + porcentaje + " %");
                    evaluarPorcentajeOcupacion(viaje, porcentaje);


                }
            }
        }
    }

    public static Viaje evaluarPorcentajeOcupacion(Viaje viaje, float porcentaje){
        if (porcentaje >= 85){
            viaje.setFrecuencia(viaje.getFrecuencia() + 1);
            return viaje;
        }else if(porcentaje >= 40 && porcentaje < 60){
            viaje.setFrecuencia(viaje.getFrecuencia() - 2);
            //APLICAR LO DEL BONO
            return viaje;
        }else if(porcentaje < 10){
            System.out.println("[1] Eliminar Viaje, [2] Tener Fé ");
            Scanner aux = new Scanner(System.in);
            int propuesta = aux.nextInt();
            if ( propuesta == 1) {
                Viaje.eliminarViaje(viaje.getId());
            }else{
                System.out.println("Esperemos que no genere muchas Perdidas");
            }
        }
        return viaje;
    }
}
