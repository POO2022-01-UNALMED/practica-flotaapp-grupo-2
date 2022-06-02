package uiMain.funcionalidades;
import gestorAplicacion.Ciudad;
import gestorAplicacion.Viaje;
import gestorAplicacion.Tiquete;

import java.util.Scanner;

import java.io.IOException;

public class AdminViaje {
    private int idEmpresa;

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

                    float porcentaje = ((viaje.getVehiculo().getSillas().size() - viaje.getVehiculo().sillasDisponibles().size())*100)/viaje.getVehiculo().getSillas().size();
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
            System.out.println("[1] Eliminar Viaje, [2] Tener FÃ© ");
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
    
  public static void rentabilidadViaje(Viaje viaje) {
	  int valorTiquetes = 0;
	  int sillasOcupadas = 0;
	  for (Tiquete tiqueteViaje: viaje.getAllTiquetes()) {
		  if (tiqueteViaje.getEstado()) {
			  valorTiquetes += tiqueteViaje.getValor();
			  sillasOcupadas++;
		  }else {
			  continue;
		  }
	  }
	  System.out.println(viaje.toString());
	  System.out.println( "Ocupación del vehiculo : " + (100 / viaje.getAllTiquetes().size() * sillasOcupadas) + "%" + "," + 
	  "con" + viaje.getAllTiquetes().size() + "sillas disponibles. ");
	  System.out.println("Para este viaje se generó $" + valorTiquetes + "y su costo fue de " + viaje.getCosto() + 
			  "y su uilidad fue del " + (valorTiquetes - viaje.getCosto()));
	  
	  // promedio  por ruta ruta
	  int ocupacionT = 0;
	  int cantViajes = 0;
	  int costoTot = 0;
	  int gananciaT = 0;
	  for(Viaje cadaViaje: Viaje.getViajes()) {
		  if(cadaViaje.getOrigen().equals(viaje) && cadaViaje.getDestino().equals(viaje)) {
			  int valorTaux = 0;
			  int ocupadasAux = 0;
			  for (Tiquete tiqueteAux: cadaViaje.getAllTiquetes()) {
				  if (tiqueteAux.getEstado()) {
					  valorTaux +=  tiqueteAux.getValor();
					  ocupadasAux++;
				  }else {
					  continue;
				  }				  			  
			  }
			  ocupacionT += 100/cadaViaje.getAllTiquetes().size()*ocupadasAux;
			  cantViajes++;
			  costoTot += cadaViaje.getCosto();
			  gananciaT += valorTaux;
			  
		  }else {
			  continue;
		  }
		  System.out.println("La ocupación promedio de la ruta es: " + ocupacionT/cantViajes + 
				  " y su utilidad" + (gananciaT -costoTot));
	  }
   }
  

}
