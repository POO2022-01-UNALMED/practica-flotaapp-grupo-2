package gestorAplicacion;

import java.io.Serializable;
import java.time.LocalDate;
import java.util.ArrayList;


	public class Tiquete implements Serializable {
		private final int idTiquete;
		protected Comprador comprador;
		protected Silla sillaTiquete;
		protected Viaje viaje;
		protected int valor;
		protected LocalDate fechaCompra;
	
	public Tiquete(int idTiquete, Comprador comprador, Silla sillaTiquete, Viaje viaje, int valor, LocalDate fechaCompra) {
		this.idTiquete = idTiquete;
		this.comprador = comprador;
		this.sillaTiquete = sillaTiquete;
		this.viaje = viaje;
		this.valor = valor;
		this.fechaCompra = fechaCompra;
	}

	// ----- G E T   A N D   S E T -----

	

	public Silla getSillaTiquete() {return sillaTiquete;}

	public Viaje getViaje() {return viaje;	}

	public Comprador getComprador() {return comprador;}

	public void setComprador(Comprador comprador) {this.comprador = comprador;}

	public int getValor() {	return valor;}

	public int getIdTiquete() {
		return idTiquete;
	}

	public void setFechaCompra(LocalDate fechaCompra) {	this.fechaCompra = fechaCompra;	}

	public String toString() {
		return "Tiquete{" +
				"comprador=" + comprador + "\n" +
				"	sillaTiquete=" + sillaTiquete + "\n" +
				"	viaje=" + viaje +
				", valor=" + valor +
				", fechaCompra=" + fechaCompra +
				'}';
	}
}

