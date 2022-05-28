package gestorAplicacion;

import java.io.Serializable;
import java.util.ArrayList;

public class Vehiculo implements Serializable {
    private String placa;
    private Conductor conductor;
    private ArrayList<Silla> sillas;

    public Vehiculo(String placa, ArrayList<Silla> sillas){
        this.placa = placa;
        this.sillas = sillas;
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

    // ----- G E T   A N D   S E T -----

    public String getPlaca() {   return placa;  }

    public Conductor getConductor() { return conductor;  }

    public ArrayList<Silla> getSillas() {    return sillas;   }

    public void setConductor(Conductor conductor) {
        this.conductor = conductor;
    }

}