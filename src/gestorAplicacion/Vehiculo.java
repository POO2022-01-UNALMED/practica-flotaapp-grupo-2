package gestorAplicacion;

import java.util.ArrayList;

public class Vehiculo {
    private String placa;
    private Conductor conductor;
    private ArrayList<Silla> sillaEstandar;
    private ArrayList<Silla> sillaPremium;

    public void Vehiculo(String placa, ArrayList<Silla> sillaEstandar, ArrayList<Silla> sillaPremium){
        this.placa = placa;
        this.sillaEstandar = sillaEstandar;
        this.sillaPremium = sillaPremium;
    }

    public Conductor getConductor() { return conductor;  }

    public void setConductor(Conductor conductor) {
        this.conductor = conductor;
    }

    //public Silla selecionarSilla() {}

}