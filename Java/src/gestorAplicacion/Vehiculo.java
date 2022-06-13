/*
 * Clase con la informacion de Vehiculo y sillas totales por viaj
 * Estructuras: ArrayList y sys funciones
 * 
 * @author: Mateo Hechavarria, Juan Pablo Pineda, Miguel Angel Fonseca, Haison Urrutia
 */



package gestorAplicacion;

import java.io.Serializable;
import java.util.ArrayList;

public class Vehiculo implements Serializable {
    private String placa;
    private ArrayList<Silla> sillas;
    private static final long serialVersionUID = 9L;
    private static  ArrayList<Vehiculo> vehiculos = new ArrayList<>();
    static {
        vehiculos = new ArrayList<Vehiculo>();
    }

    public Vehiculo(String placa, ArrayList<Silla> sillas){
        this.placa = placa;
        this.sillas = sillas;
        Vehiculo.vehiculos.add(this);
    }


    public String getPlaca() {
        return placa;
    }

    public ArrayList<Silla> getSillas() {
        return sillas;
    }

    public void setSillas(ArrayList<Silla> sillas) {
        this.sillas = sillas;
    }


    //public Silla selecionarSilla() {}

    public static ArrayList<Vehiculo> getVehiculos() {
        return vehiculos;
    }

    public static Vehiculo  getVehiculoRevisar(){
        return Vehiculo.getVehiculos().get(0);
    }
}