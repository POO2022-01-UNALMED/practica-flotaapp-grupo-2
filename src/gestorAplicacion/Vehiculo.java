package gestorAplicacion;

import java.io.Serializable;
import java.util.ArrayList;
import java.util.Scanner;

public class Vehiculo implements Serializable {
    private String placa;
    private Conductor conductor;
    private ArrayList<Silla> sillas;
    private static  ArrayList<Vehiculo> vehiculos = new ArrayList<>();
    static {
        vehiculos = new ArrayList<Vehiculo>();
    }

    public Vehiculo(String placa, ArrayList<Silla> sillas){
        this.placa = placa;
        this.sillas = sillas;
        Vehiculo.vehiculos.add(this);
    }


    public ArrayList<Silla> sillasDisponibles(){
        ArrayList<Silla> disponibles = new ArrayList<>();
        for(Silla silla : this.getSillas()){
            if(silla.getEstado() == false){
                disponibles.add(silla);
            }
        }
        return disponibles;
    }
    
    public Silla selceccionarSilla() {
    	Scanner aux = new Scanner(System.in);
    	int numeroSilla = aux.nextInt();
    	if(this.sillasDisponibles().size() > 1) {
    		for(Silla sillas: this.sillasDisponibles()) {
    		if(sillas.getNumeroSilla() == numeroSilla && sillas.getEstado == false) {
    			sillas.setEstado(true);
    		}
    		if(sillas.getEstado() == true) {
    			return sillas;
    			}
    		}
    	}return null;
    }

    // ----- G E T   A N D   S E T -----

    public String getPlaca() {   return placa;  }

    public Conductor getConductor() { return conductor;  }

    public ArrayList<Silla> getSillas() {    return sillas;   }

    public void setConductor(Conductor conductor) {
        this.conductor = conductor;
    }

    public static ArrayList<Vehiculo> getVehiculos() {        return vehiculos;    }

    public static Vehiculo  getVehiculoRevisar(){
        return Vehiculo.getVehiculos().get(0);
    }
}