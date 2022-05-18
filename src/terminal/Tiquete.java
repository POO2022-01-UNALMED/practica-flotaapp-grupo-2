package terminal;

import java.util.Date;
import java.util.ArrayList;

public class Tiquete {
	private int idTiquete;
	private Usuario usuario;
	private Viaje viaje;
	private int valor;
	private Date fechaCompra;
	private static ArrayList<Tiquete> tiquetes = new ArrayList<>();
	
	
	public Tiquete(int idTiquete, Usuario usuario, Viaje viaje, int valor, Date fechaCompra) {
		this.idTiquete = idTiquete; 
		this.usuario = usuario;
		this.viaje = viaje;
		this.valor = valor;
		this.fechaCompra = fechaCompra;
		tiquetes.add(this);		
	}
	
	//public void crearTiquete(Tiquete nuevo) {
		
	//k}
	
	

}
