package uiMain.funcionalidades;
import gestorAplicacion.Ciudad;
import gestorAplicacion.Usuario;
import gestorAplicacion.Viaje;

import java.util.ArrayList;
import java.util.Date;

public class AdminTiquete {
    private int idEmpresa;

    public static void visualizarEstadisticas(){
        for(Ciudad ciudad : Ciudad.getCiudades()){
            System.out.println("id: " + ciudad.getId() + " - Nombre: "+ciudad.getNombre());
            System.out.println("Numero de Visitante: "+ ciudad.getNumVisitantes());
            int allSillasDisponiblesViajes = 0;
            for(Viaje viaje : Viaje.getViajes()){
                if (viaje.getDestino().getNombre() == ciudad.getNombre()){
                    allSillasDisponiblesViajes += viaje.getAllTiquetes().size();
                }
            }
            if (allSillasDisponiblesViajes == 0){
                float porcentaje = 0;
                System.out.println("Promedio de ocupacion: " + porcentaje + " %");
            } else {
                float porcentaje = (ciudad.getNumVisitantes()*100)/allSillasDisponiblesViajes;
                System.out.println("Promedio de ocupacion: " + porcentaje + " %");
            }
            System.out.println(" ");

        }
    }
}
