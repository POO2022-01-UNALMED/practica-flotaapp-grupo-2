package gestorAplicacion;

import java.io.Serializable;
import java.util.Date;
import java.util.ArrayList;

public class Tiquete implements Serializable {
	private int idTiquete;
	private Comprador comprador;
	private Viaje viaje;
	private int valor;
	private Date fechaCompra;
	private static ArrayList<Tiquete> tiquetes = new ArrayList<>();
	static {
		tiquetes = new ArrayList<Tiquete>();
	}

	public Tiquete(int idTiquete, Viaje viaje, int valor, Date fechaCompra) {
		this.idTiquete = idTiquete;
		this.viaje = viaje;
		this.valor = valor;
		this.fechaCompra = fechaCompra;
		tiquetes.add(this);
	}

	//public void crearTiquete(Tiquete nuevo) {

	//k}


	public Viaje getViaje() {return viaje;	}

	public Comprador getUsuario() {return comprador;}

	public void setComprador(Comprador comprador) {this.comprador = comprador;}



	public static ArrayList<Tiquete> getTiquetes(){	return tiquetes;}

}