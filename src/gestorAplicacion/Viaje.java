package gestorAplicacion;

import java.time.LocalDateTime;
import java.util.ArrayList;
import java.time.LocalDate;
import java.io.Serializable;

public class Viaje implements Serializable {
	private final int id;
	private int costo;
	private  int precioEstandar;
	private  int precioPremium;
	private Ciudad origen;
    private Ciudad destino;
    private int frecuencia;
    private ArrayList<Tiquete> allTiquetes = new ArrayList<>();
    private LocalDate fechaViaje;
    private Vehiculo vehiculo; 
    public static ArrayList<Viaje> viajes = new ArrayList<>();
    
    /*
     * Se almacenar� en el atributo de clase viajes, todos los viajes disponibles para una vez terminada la ejecuci�n 
     * del programa se serialice en os arcjvos txt, esto aunque no es una manera optima ya que el ideal es hacer el CRUD 
     * directamente en los archivos txt es una solucion viable para este ejemplo.
     */
    
    
    
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

    	/*
    	 * los tiquetes se generan a partir de la cantidad y tipo de sillas en el vehiculo y su respectivo id es el 
    	 * �ndice de la silla. El estado al ser un booleano se define como true para premium y false para estandar
    	 */
   
    	
    	for (Silla sillaEnVehiculo: this.vehiculo.getSillas()) {
			int genId = this.vehiculo.getSillas().indexOf(sillaEnVehiculo);
    		int tipoSilla = precioEstandar;                    // 0 Estandar y 1 premium
    		if (sillaEnVehiculo.getEstado()) {
    			tipoSilla = precioPremium;
    		}
    		this.allTiquetes.add(new Tiquete(genId, null, sillaEnVehiculo, this, tipoSilla, fechaViaje));
    		
    		/*
    		 *  El argumento null ( comrador) se le cambiara el estado al momento de comprar tiquete donde 
    		 *  se asignar� el respectivo comprador 
    		 */
    	}
    	viajes.add(this); 
    }
    
    /*
     * Como hacer que el contains compare por la llave primaria que es el identifciador desde un contains 
     */
    
    
    	
    public static void eliminarViaje(int idViaje) {
    	for (Viaje cadaViaje: viajes) {
    		if (cadaViaje.id == idViaje) {
    			viajes.remove(cadaViaje);
    		}
    	}
    }
   
    
    //// Setters and Getters
    
	public int getId() {
		return id;
	}

	public Tiquete tiqueteDisponible(int presupuesto){
		Tiquete tiqueteFinal = new Tiquete(0, null, null, null, 0, null);
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

	public int getCosto() {
		return costo;
	}

	public void setCosto(int costo) {
		this.costo = costo;
	}

	
	public LocalDate getFechaViaje() {
		return fechaViaje;
	}

	public Vehiculo getVehiculo() {	return vehiculo;}


	public int getPrecioEstandar() {
		return precioEstandar;
	}

	public void setPrecioEstandar(int precioEstandar) {
		this.precioEstandar = precioEstandar;
	}

	public int getPrecioPremium() {
		return precioPremium;
	}

	public void setPrecioPremium(int precioPremium) {
		this.precioPremium = precioPremium;
	}

	public Ciudad getOrigen() {
		return origen;
	}

	public void setOrigen(Ciudad origen) {
		this.origen = origen;
	}

	public Ciudad getDestino() {
		return destino;
	}

	public void setDestino(Ciudad destino) {
		this.destino = destino;
	}

	public int getFrecuencia() {
		return frecuencia;
	}

	public void setFrecuencia(int frecuencia) {
		this.frecuencia = frecuencia;
	}

	public static ArrayList<Viaje> getViajes() {return viajes;}

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
