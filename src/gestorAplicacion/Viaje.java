package gestorAplicacion;

import java.util.ArrayList;
import java.util.Date;
import java.io.Serializable;

public class Viaje implements Serializable {
	private int id;
	private int costo;
	private Ciudad origen;
	private static  ArrayList<Ciudad> destino = new ArrayList<>();
	private Date fechaViaje;
	private Vehiculo vehiculo;
	private boolean escala;
	private boolean disponibilidad;
	private static ArrayList<Viaje> viajes;
	static {
		viajes = new ArrayList<Viaje>();
	}


	public Viaje(int costo, Ciudad origen, ArrayList<Ciudad> destino, Vehiculo vehiculo,
				 Date fechaViaje, boolean escala) {

		this.id = 1 + Viaje.getViajes().size();
		this.costo = costo;
		this.origen = origen;
		this.destino = destino;
		this.fechaViaje = fechaViaje;
		this.vehiculo = vehiculo;
		this.escala = escala;
		this.disponibilidad = true;
	}


	//public Viaje crearViaje(		)


	public Date getFechaViaje() {return fechaViaje;	}

	public Vehiculo getVehiculo() {	return vehiculo; }

	public static ArrayList<Ciudad> getDestino() {return destino;}

	public static ArrayList<Viaje> getViajes() {return viajes;}
}