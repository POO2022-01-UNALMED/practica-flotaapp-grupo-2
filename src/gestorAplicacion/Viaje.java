package gestorAplicacion;

import java.util.ArrayList;
import java.util.Date;
import java.io.Serializable;

public class Viaje implements Serializable {
	private int id;
	private int costo;
	private  int precioEstandar;
	private  int precioPremium;
	private Ciudad origen;
	private Ciudad destino;
	private ArrayList<Ciudad> ruta;
	private Date frecuencia;
	private ArrayList<Tiquete> allTiquetes;
	private Date fechaViaje;
	private Vehiculo vehiculo;
	private boolean disponibilidad;
	private static ArrayList<Viaje> viajes;
	static {
		viajes = new ArrayList<Viaje>();
	}


	public Viaje(int id , int costo, int precioEstandar, int precioPremium, Ciudad origen, Ciudad destino, Vehiculo vehiculo,
				 Date fechaViaje) {

		this.id = id;
		this.costo = costo;
		this.precioEstandar = precioEstandar;
		this.precioPremium = precioPremium;
		this.origen = origen;
		this.destino = destino;
		this.fechaViaje = fechaViaje;
		this.vehiculo = vehiculo;
		this.disponibilidad = true;
		this.allTiquetes = new ArrayList<Tiquete>();
		Viaje.viajes.add(this);

		for (Silla silla : vehiculo.getSillas()){
			if (silla.getTipo() == true){
				allTiquetes.add(new Tiquete(silla, this, precioPremium));
			}else {
				allTiquetes.add(new Tiquete(silla, this, precioEstandar));
			}
		}
	}


	//public Viaje crearViaje(		)

	public int getCosto() {	return costo;}

	public void setCosto(int costo) {this.costo = costo;}

	public ArrayList<Tiquete> getAllTiquetes() {return allTiquetes;	}

	public int getPrecioEstandar() {return precioEstandar;	}

	public int getPrecioPremium() {	return precioPremium;}

	public Date getFechaViaje() {return fechaViaje;	}

	public Vehiculo getVehiculo() {	return vehiculo; }

	public Ciudad getDestino() {return destino;}

	public static ArrayList<Viaje> getViajes() {return viajes;}

	public boolean isDisponibilidad() {	return disponibilidad;	}

	public void setDisponibilidad(boolean disponibilidad) {	this.disponibilidad = disponibilidad;}
}