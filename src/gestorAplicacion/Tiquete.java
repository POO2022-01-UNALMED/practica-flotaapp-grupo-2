
package gestorAplicacion;

import java.io.Serializable;
import java.util.Date;
//import java.util.ArrayList;

public class Tiquete implements Serializable {
	private final int idTiquete;
	private Comprador comprador;
	private Silla silla;
	private Viaje viaje;
	private int valor;
	private Date fechaCompra;
	
	//private static ArrayList<Tiquete> tiquetes = new ArrayList<>();

	
	
	public Tiquete(int idTiquete, Comprador comprador,  Silla silla, Viaje viaje, int valor, Date fechaCompra) {
		this.idTiquete = idTiquete;
		this.setComprador(comprador);
		this.setSilla(silla);
		this.viaje = viaje;
		this.valor = valor;
		this.fechaCompra = fechaCompra;
	}
	
	public int getIdTiquete() {
		return idTiquete;
	}

	
	public Viaje getViaje() {
		return viaje;
	}

	public void setViaje(Viaje viaje) {
		this.viaje = viaje;
	}

	public int getValor() {
		return valor;
	}

	public void setValor(int valor) {
		this.valor = valor;
	}

	public Date getFechaCompra() {
		return fechaCompra;
	}

	public void setFechaCompra(Date fechaCompra) {
		this.fechaCompra = fechaCompra;
	}

	public Comprador getComprador() {
		return comprador;
	}

	public void setComprador(Comprador comprador) {
		this.comprador = comprador;
	}

	public Silla getSilla() {
		return silla;
	}

	public void setSilla(Silla silla) {
		this.silla = silla;
	}
	
}	
