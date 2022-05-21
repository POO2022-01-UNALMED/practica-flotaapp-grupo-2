package gestorAplicacion;

import java.io.Serializable;
import java.util.ArrayList;

public class Vehiculo implements Serializable {
    private String placa;
    private Conductor conductor;
    private ArrayList<Silla> sillaEstandar;
    private ArrayList<Silla> sillaPremium;

    public Vehiculo(String placa, ArrayList<Silla> sillaEstandar, ArrayList<Silla> sillaPremium){
        this.placa = placa;
        this.sillaEstandar = sillaEstandar;
        this.sillaPremium = sillaPremium;
    }

    public String getPlaca() {   return placa;  }

    public Conductor getConductor() { return conductor;  }

    public void setConductor(Conductor conductor) {
        this.conductor = conductor;
    }

    //public Silla selecionarSilla() {}

}