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
    	this.precioEstandar = precioEstandar;
    	this.precioPremium = precioPremium;
    	this.origen = origen;
    	this.destino = destino;
    	this.ruta = ruta;
    	this.frecuencia = frecuencia;
    	this.fechaViaje = fechaViaje;
    	this.vehiculo = vehiculo;
    	this.disponibilidad = disponibilidad;
    	
    	/*
    	 * los tiquetes se generan a partir de la cantidad y tipo de sillas en el vehiculo y su respectivo id es el 
    	 * índice de la silla. El estado al ser un booleano se define como true para premium y false para estandar
    	 */
    	
    	for (Silla s: this.vehiculo.getSillas()) {
    		int genId = this.vehiculo.getSillas().indexOf(s);
    		int auxValor = 0;
    		if (s.getEstado()) {
    			auxValor = precioPremium;
    		}
    		this.allTiquetes.add(new Tiquete(genId, null, s, this, auxValor, fechaViaje)); 
    		/*
    		 *  El argumento null ( comrador) se le cambiará el estado al momento de comprar tiquete donde 
    		 *  se asignará el respectivo comprador 
    		 */
    	}
    
    }
    // Se valida por cada Ciudad de destino que ya esté creado en Ciudad
    /*
     * Como hacer que el contains compare por la llave primaria que es el identifciador desde un contains 
     */
    
    public boolean validarDestino() {
    	boolean aux = false;
    	for(Ciudad c: ruta) {
    		if (Ciudad.getCiudad().contains(c)) {
    			aux = true;
    		}
    	}
    	return aux; 
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
}
	