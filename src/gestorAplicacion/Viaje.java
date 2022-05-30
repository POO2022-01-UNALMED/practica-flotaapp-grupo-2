package gestorAplicacion;

import java.time.LocalDateTime;
import java.util.ArrayList;
import java.time.LocalDate;
import java.io.Serializable;

public class Viaje implements Serializable {
	private int id;
	private int costo;
	private  int precioEstandar;
	private  int precioPremium;
	private Ciudad origen;
	private Ciudad destino;
	private ArrayList<Ciudad> ruta;
	private int frecuencia;
	private ArrayList<Tiquete> allTiquetes;
	private LocalDate fechaViaje;
	private Vehiculo vehiculo;
	private boolean disponibilidad;
	private static ArrayList<Viaje> viajes;
	static {
		viajes = new ArrayList<Viaje>();
	}


	public Viaje(int id , int costo, int precioEstandar, int precioPremium, Ciudad origen, Ciudad destino,int frecuencia, Vehiculo vehiculo,
				 LocalDate fechaViaje) {

		this.id = id;
		this.costo = costo;
		this.precioEstandar = precioEstandar;
		this.precioPremium = precioPremium;
		this.origen = origen;
		this.destino = destino;
		this.frecuencia = frecuencia;
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

	public Tiquete tiqueteDisponible(int presupuesto){
		Tiquete tiqueteFinal = new Tiquete();
		for(Tiquete tiquete : allTiquetes){
			if(tiquete.getValor() <= presupuesto && tiquete.getSillaTiquete().getEstado() == false){
				tiqueteFinal =  tiquete;
			}
		}
		return tiqueteFinal;
	}

	public void eliminarViaje(){
		Viaje.viajes.remove(this);
	}

	// ----- G E T   A N D   S E T -----


	public int getId() {return id;}

	public int getCosto() {	return costo;}

	public void setCosto(int costo) {this.costo = costo;}

	public ArrayList<Tiquete> getAllTiquetes() {return allTiquetes;	}

	public int getPrecioEstandar() {return precioEstandar;	}

	public int getPrecioPremium() {	return precioPremium;}

	public LocalDate getFechaViaje() {return fechaViaje;	}

	public Vehiculo getVehiculo() {	return vehiculo; }

	public Ciudad getOrigen() {	return origen;	}

	public Ciudad getDestino() {return destino;}

	public static ArrayList<Viaje> getViajes() {return viajes;}

	public boolean isDisponibilidad() {	return disponibilidad;	}

	public void setDisponibilidad(boolean disponibilidad) {	this.disponibilidad = disponibilidad;}

	public void aumentarFrecuencia(int frecuencia) {	this.frecuencia += frecuencia;	}

	public void disminuirFrecuencia(int frecuencia) {	this.frecuencia -= frecuencia;	}
}