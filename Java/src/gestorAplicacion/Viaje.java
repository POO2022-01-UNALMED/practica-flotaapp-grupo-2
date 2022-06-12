/*
 * Clase con la información de viaje, almacena la lista de tiquetes de acuerdo a la cantiudad de sillas
 * Estructuras: ArrayList, to string
 * 
 * @author: Mateo Hechavarria, Juan Pablo Pineda, Miguel Angel Fonseca, Haison Urrutia
 */


package gestorAplicacion;

import java.time.LocalDate;
import java.util.ArrayList;
import java.time.LocalDate;
import java.io.Serializable;

public class Viaje implements Serializable {
	private static final long serialVersionUID = 109L;
	private int id;
	private int costo;
	private  int precioEstandar;
	private  int precioPremium;
	private Ciudad origen;
	private Ciudad destino;
	private Conductor conductor;
	private int frecuencia;
	private ArrayList<Tiquete> allTiquetes;
	private LocalDate fechaViaje;
	private Vehiculo vehiculo;
	private boolean disponibilidad;
	private static ArrayList<Viaje> viajes;
	static {
		viajes = new ArrayList<Viaje>();
	}

	public Viaje(){}

	public Viaje(int id, int costo, int precioEstandar, int precioPremium, Ciudad origen, Ciudad destino, int frecuencia,
				 Vehiculo vehiculo, LocalDate fechaViaje) {

		this.id = id;
		this.costo = costo;
		this.precioEstandar = precioEstandar;
		this.precioPremium = precioPremium;
		this.origen = origen;
		this.destino = destino;
		this.frecuencia = frecuencia;
		this.fechaViaje = fechaViaje;
		this.vehiculo = vehiculo;
		this.allTiquetes = new ArrayList<>();

		/*
		 * los tiquetes se generan a partir de la cantidad y tipo de sillas en el vehiculo y su respectivo id es el
		 * ï¿½ndice de la silla. El estado al ser un booleano se define como true para premium y false para estandar
		 */


		for (Silla sillaEnVehiculo: this.vehiculo.getSillas()) {
			int genId = this.vehiculo.getSillas().indexOf(sillaEnVehiculo);
			int tipoSilla = precioEstandar;                    // 0 Estandar y 1 premium
			if (sillaEnVehiculo.getTipo()) {
				tipoSilla = precioPremium;
			}
			this.allTiquetes.add(new Tiquete(genId, null, sillaEnVehiculo, this, tipoSilla, fechaViaje));

			/*
			 *  El argumento null ( comrador) se le cambiara el estado al momento de comprar tiquete donde
			 *  se asignarï¿½ el respectivo comprador
			 */
		}
		viajes.add(this);
	}

	public Tiquete tiqueteDisponible(int presupuesto){
		Tiquete tiqueteFinal = new Tiquete();
		for(Tiquete tiquete : allTiquetes){
			if(tiquete.getValor() <= presupuesto && tiquete.getEstado() == false){
				tiqueteFinal =  tiquete;
			}
		}
		return tiqueteFinal;
	}

	public ArrayList<Tiquete> tiquetesDisponibles(){
		ArrayList<Tiquete> tiqueteFinal = new ArrayList<>();
		for(Tiquete tiquete : allTiquetes){
			if(tiquete.getEstado() == false){
				tiqueteFinal.add(tiquete);
			}
		}
		return tiqueteFinal;
	}

	public void eliminarViaje(){
		Viaje.viajes.remove(this);
	}

	// ----- G E T   A N D   S E T -----

	public static ArrayList<Viaje> viajesSinConductor(){
		ArrayList<Viaje> viajes = new ArrayList<>();
		for(Viaje viaje : Viaje.getViajes()){
			if(viaje.getConductor() == null){
				viajes.add(viaje);
			}
		}
		return viajes;
	}

	public int getId() {return id;}

	public int getCosto() {	return costo;}

	public void setCosto(int costo) {this.costo = costo;}

	public Conductor getConductor() {return conductor;	}

	public void setConductor(Conductor conductor) {	this.conductor = conductor;	}

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

	@Override
	public String toString() {
		return "Viaje{" +
				"id=" + id +
				", origen=" + origen +
				", destino=" + destino +
				", fechaViaje=" + fechaViaje +
				'}';
	}
}