/*
 * Clase con las funciones de Silla necesarias para asignar un tiquete de un viaje
 * Estructuras: ArrayList y sus funciones, enum
 * 
 * @author: Mateo Hechavarria, Juan Pablo Pineda, Miguel Angel Fonseca, Haison Urrutia
 */



package gestorAplicacion;

import java.io.Serializable;
import java.util.ArrayList;

public class Silla implements Serializable {
	private enum ubicacion {PASILLO, VENTANA, INTERMEDIO}

    private int numeroSilla;
    private boolean tipo; //0 - Estandar , 1 - Premium
    private Ubicacion ubicacion; //0 - V , 1 - P
	private static  ArrayList<Silla> sillas;
	static {
		sillas = new ArrayList<Silla>();
	}


	public Silla(int numeroSilla, boolean tipo, Ubicacion ubicacion) {
    	this.setNumeroSilla(numeroSilla);
    	this.setTipo(tipo);
    	this.setUbicacion(ubicacion);

    	Silla.sillas.add(this);
    }

    public boolean getTipo() { return  tipo;}

	public int getNumeroSilla() {	return numeroSilla;	}

	public void setNumeroSilla(int numeroSilla) {
		this.numeroSilla = numeroSilla;
	}

	public boolean isTipo() {
		return tipo;
	}

	public void setTipo(boolean tipo) {
		this.tipo = tipo;
	}

	public Ubicacion getUbicacion() {
		return ubicacion;
	}

	public void setUbicacion(Ubicacion ubicacion) {
		this.ubicacion = ubicacion;
	}

	public static ArrayList<Silla> getSillas() {	return sillas;	}

	@Override
    public String toString() {
        return "Silla{" +
                "numeroSilla=" + numeroSilla +
                ", tipo=" + tipo +
                ", ubicacion=" + ubicacion +
                '}';
    }
}
