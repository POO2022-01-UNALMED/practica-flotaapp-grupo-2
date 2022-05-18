package terminal;

import java.util.ArrayList;
import java.util.Date;
import java.io.Serializable;

public class Viaje {
	
	private int id;
	private int costo;
	private Ciudad origen;
    private static  ArrayList<Ciudad> destino = new ArrayList<>();
    private Tiquete tiquete;
    private Date fechaViaje;
    private Vehiculo vehiculo; 
    private boolean escala;
    private boolean disponibilidad;
    
    public Viaje(int id, int costo, Ciudad origen, ArrayList<Ciudad> destino,
    		Tiquete tiquete, Date fechaViaje, Vehiculo vehiculo, boolean escala, boolean disponibilidad) {
    	
    	this.id = id;
    	this.costo = costo;
    	this.origen = origen;
    	this.destino = destino;
    	this.tiquete = tiquete;
    	this.fechaViaje = fechaViaje;
    	this.vehiculo = vehiculo; 
    	this.escala = escala;
    	this.disponibilidad = disponibilidad;
    }
    //public Viaje crearViaje(		)
}
