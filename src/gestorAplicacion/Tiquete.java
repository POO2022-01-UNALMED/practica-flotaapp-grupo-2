package gestorAplicacion;

import java.io.Serializable;
import java.time.LocalDate;
import java.util.ArrayList;


public class Tiquete implements Serializable {
		private int idTiquete;
		protected Comprador comprador;
		protected Silla sillaTiquete;
		protected Viaje viaje;
		protected int valor;
		protected LocalDate fechaCompra;
		private static ArrayList<Tiquete> tiquetes;
		static {
			tiquetes = new ArrayList<Tiquete>();
		}

		public Tiquete(){}

		public Tiquete(int idTiquete, Comprador comprador, Silla sillaTiquete, Viaje viaje, int valor, LocalDate fechaCompra) {
			this.idTiquete = idTiquete;
			this.comprador = comprador;
			this.sillaTiquete = sillaTiquete;
			this.viaje = viaje;
			this.valor = valor;
			this.fechaCompra = fechaCompra;
			Tiquete.tiquetes.add(this);
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

	public static ArrayList<Tiquete> getTiquetes() {return tiquetes;	}

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

