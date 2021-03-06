/*
 * Clase con las funciones de Tiquete  necesarias para determinar la ocupaci�n de un viaje, generar estadisticas, asignar viaje a usuario
 * Estructuras: ArrayList y sus funciones, LocalDate
 * 
 * @author: Mateo Hechavarria, Juan Pablo Pineda, Miguel Angel Fonseca, Haison Urrutia
 */


package gestorAplicacion;

import java.io.Serializable;
import java.time.LocalDate;
import java.util.ArrayList;

public class Tiquete implements Serializable {
		
		private static final long serialVersionUID = 7L;
		private int idTiquete;
		protected Comprador comprador;
		protected Silla sillaTiquete;
		protected Viaje viaje;
		protected int valor;
		protected LocalDate fechaCompra;
		private boolean estado;
		private static ArrayList<Tiquete> tiquetes;
		private static final long serialVersionUID = 7L;
		static {
			tiquetes = new ArrayList<Tiquete>();
		}

	public  Tiquete(){}

	public Tiquete(Silla sillaTiquete, Viaje viaje, int valor) {
		this.sillaTiquete = sillaTiquete;
		this.viaje = viaje;
		this.estado = false;
		this.valor = valor;
	}

		public Tiquete(int idTiquete, Comprador comprador, Silla sillaTiquete, Viaje viaje, int valor, LocalDate fechaCompra) {
			this.idTiquete = idTiquete;
			this.comprador = comprador;
			this.sillaTiquete = sillaTiquete;
			this.viaje = viaje;
			this.valor = valor;
			this.estado = false;
			this.fechaCompra = fechaCompra;
			Tiquete.tiquetes.add(this);
		}

	// ----- G E T   A N D   S E T -----

	public Silla getSillaTiquete() {return sillaTiquete;}

	public Viaje getViaje() {return viaje;	}

	public Comprador getUsuario() {return comprador;}

	public boolean getEstado() {
		return estado;
	}

	public void setEstado(boolean estado) {
		this.estado = estado;
	}

	public void setComprador(Comprador comprador) {this.comprador = comprador;}

	public int getValor() {	return valor;}

	public Comprador getComprador() {	return comprador;}

	public void setFechaCompra(LocalDate fechaCompra) {	this.fechaCompra = fechaCompra;	}

	public static ArrayList<Tiquete> getTiquetes() {return tiquetes;	}

	@Override
	public String toString() {
		return "Tiquete = " +"ID : " + idTiquete + ", SILLA :" + sillaTiquete + "\n" +
				"	VIAJE =" + viaje + 
				", valor : " + valor +
				", fechaCompra : " + fechaCompra;
	}
}
