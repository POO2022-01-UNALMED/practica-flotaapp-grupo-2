package terminal;

import java.util.ArrayList;
import java.util.Date;
import java.io.Serializable;

public class Viaje {
								// Para unir las clases es necesario un ArrayList en cada clase?
	private int id;
	private int costo;
	private Ciudad origen;
    private static  ArrayList<Ciudad> destino = new ArrayList<>();
    private Tiquete tiquete;
    private Date fechaViaje;
    private Vehiculo vehiculo; 
    private boolean escala;
    private boolean disponibilidad;
    public static ArrayList<Viaje> viajes = new ArrayList<>();
    
    
    
    public Viaje(int id, int costo, Ciudad origen, ArrayList<Ciudad> destino,
    		Tiquete tiquete, Date fechaViaje, Vehiculo vehiculo, boolean escala, boolean disponibilidad) {
    	
    	this.setId(id);
    	this.setCosto(costo);
    	this.origen = origen;
    	this.destino = destino;
    	this.setTiquete(tiquete);
    	this.setFechaViaje(fechaViaje);
    	this.setVehiculo(vehiculo); 
    	this.setEscala(escala);
    	this.setDisponibilidad(disponibilidad);
    }
    // Se valida por cada Ciudad de destino que ya esté creado en Ciudad
    
    public boolean validarDestino() {
    	boolean aux = false;
    	for(Ciudad c: destino) {
    		if (Ciudad.getCiudad().contains(c)) {
    			aux = true;
    		}
    	}
    	return aux; 
    }
    
    
    public void crearViaje() { // Si la lista está vacia y origen y destino están en Ciudad se agrega el viaje 
    	/*
    	if(viajes.isEmpty() && Ciudad.getCiudad().contains(origen) && this.validarDestino()) {
    		viajes.add(this);
    	} */
    	if(Ciudad.getCiudad().contains(origen) && this.validarDestino()) {
    		viajes.add(this);
    		
    	}
    	else {
    		return;
    	}
    }
    	
    public void eliminarViaje() { // Elimina viaje desde una instancia 
    	if (viajes.contains(this)) {
    		viajes.remove(this);    			
    	}else {
    		return;
    	}
    }
    
    public void suspenderViaje() {
    	if(viajes.contains(this)) {
    		this.setDisponibilidad(false);
    		System.out.println("Se ha cambiado la disponibilidad con exito");
    	}else {
    		System.out.println("No se puede suspender, el viaje no existe");
    	}
    }
    
    public void activarViaje() {
    	if(viajes.contains(this)) {
    		this.setDisponibilidad(true);
    		System.out.println("Se ha cambiado la disponibilidad con exito");
    	}else {
    		System.out.println("No se puede suspender, el viaje no existe");
    	}
    }
    
    public ArrayList<Ciudad>  consultarCiudad() { //Es cnsultar ciudad o consultar ciudades?
    	return Ciudad.getCiudad();
    }
    //// Setters and Getters
    
	public int getId() {
		return id;
	}

	public void setId(int id) {
		this.id = id;
	}

	public int getCosto() {
		return costo;
	}

	public void setCosto(int costo) {
		this.costo = costo;
	}

	public Tiquete getTiquete() {
		return tiquete;
	}

	public void setTiquete(Tiquete tiquete) {
		this.tiquete = tiquete;
	}

	public Date getFechaViaje() {
		return fechaViaje;
	}

	public void setFechaViaje(Date fechaViaje) {
		this.fechaViaje = fechaViaje;
	}

	public Vehiculo getVehiculo() {
		return vehiculo;
	}

	public void setVehiculo(Vehiculo vehiculo) {
		this.vehiculo = vehiculo;
	}

	public boolean isEscala() {
		return escala;
	}

	public void setEscala(boolean escala) {
		this.escala = escala;
	}

	public boolean isDisponibilidad() {
		return disponibilidad;
	}

	public void setDisponibilidad(boolean disponibilidad) {
		this.disponibilidad = disponibilidad;
	}

    
}

