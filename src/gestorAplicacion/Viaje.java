package gestorAplicacion;

import java.util.ArrayList;
import java.util.Date;
import java.io.Serializable;

public class Viaje implements Serializable {
	private final int id;
	private int costo;
	private  int precioEstandar;
	private  int precioPremium;
	private Ciudad origen;
    private Ciudad destino;
    private ArrayList<Ciudad> ruta = new ArrayList<>();
    private Date frecuencia;
    private ArrayList<Tiquete> allTiquetes = new ArrayList<>();
    private Date fechaViaje;
    private Vehiculo vehiculo; 
    private boolean disponibilidad;
    
    public static ArrayList<Viaje> viajes = new ArrayList<>();
    
    /*
     * Se almacenará en el atributo de clase viajes, todos los viajes disponibles para una vez terminada la ejecución 
     * del programa se serialice en os arcjvos txt, esto aunque no es una manera optima ya que el ideal es hacer el CRUD 
     * directamente en los archivos txt es una solucion viable para este ejemplo.
     */
    
    
    
    public Viaje(int id, int costo, int precioEstandar, int precioPremium, Ciudad origen, Ciudad destino, ArrayList<Ciudad> ruta, Date frecuencia,
    	Date fechaViaje, Vehiculo vehiculo, boolean disponibilidad) {
    	
    	this.id = id;
    	this.costo = costo;
    	this.setPrecioEstandar(precioEstandar);
    	this.setPrecioPremium(precioPremium);
    	this.setOrigen(origen);
    	this.setDestino(destino);
    	this.setRuta(ruta);
    	this.setFrecuencia(frecuencia);
    	this.fechaViaje = fechaViaje;
    	this.vehiculo = vehiculo;
    	this.disponibilidad = disponibilidad;
    	
    	/*
    	 * los tiquetes se generan a partir de la cantidad y tipo de sillas en el vehiculo y su respectivo id es el 
    	 * índice de la silla. El estado al ser un booleano se define como true para premium y false para estandar
    	 */
   
    	
    	for (Silla sillaEnVehiculo: this.vehiculo.getSillas()) {
    		int genId = this.vehiculo.getSillas().indexOf(sillaEnVehiculo);
    		int tipoSilla = 0;                    // 0 Estandar y 1 premium
    		if (sillaEnVehiculo.getEstado()) {
    			tipoSilla = precioPremium;
    		}
    		this.allTiquetes.add(new Tiquete(genId, null, sillaEnVehiculo, this, tipoSilla, fechaViaje)); 
    		
    		/*
    		 *  El argumento null ( comrador) se le cambiará el estado al momento de comprar tiquete donde 
    		 *  se asignará el respectivo comprador 
    		 */
    	}
    	
    	viajes.add(this); // Para este caso no se está validando si la ciudad ya existe
    	
    
    }
    
    /*
     * Como hacer que el contains compare por la llave primaria que es el identifciador desde un contains 
     */
    
    
    /*
     * Validar ciudades compara si cada ciudad asignada en la ruta hace parte de las ciudades a las cuales 
     * ya se hacen viajes
     */
    
    
    	
    public void eliminarViaje(int id) { 
    	for (Viaje cadaViaje: viajes) {
    		if (cadaViaje.id == id) {
    			viajes.remove(this);
    		}
    	}
    }
   
    
    //// Setters and Getters
    
	public int getId() {
		return id;
	}


	public int getCosto() {
		return costo;
	}

	public void setCosto(int costo) {
		this.costo = costo;
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


	public boolean isDisponibilidad() {
		return disponibilidad;
	}

	public void setDisponibilidad(boolean disponibilidad) {
		this.disponibilidad = disponibilidad;
	}

	public ArrayList<Ciudad> getRuta() {
		return ruta;
	}

	public void setRuta(ArrayList<Ciudad> ruta) {
		this.ruta = ruta;
	}

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

	public Date getFrecuencia() {
		return frecuencia;
	}

	public void setFrecuencia(Date frecuencia) {
		this.frecuencia = frecuencia;
	}
}
	