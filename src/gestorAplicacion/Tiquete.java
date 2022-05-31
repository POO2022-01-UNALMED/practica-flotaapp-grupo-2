package gestorAplicacion;

import java.io.Serializable;
<<<<<<< HEAD
import java.util.Date;
//import java.util.ArrayList;
=======
import java.time.LocalDate;
import java.util.ArrayList;
>>>>>>> master

public class Tiquete implements Serializable {
	private final int idTiquete;
	protected Comprador comprador;
	protected Silla sillaTiquete;
	protected Viaje viaje;
	protected int valor;
<<<<<<< HEAD
	protected Date fechaCompra;
	
	
		/*
		public  Tiquete(){
			System.out.println("No se encontraron tiquetes disponibles");
		}
		*/
=======
	protected LocalDate fechaCompra;
>>>>>>> master

<<<<<<< HEAD
		public Tiquete(int idTiquete, Comprador comprador, Silla sillaTiquete, Viaje viaje, int valor, Date fechaCompra) {
			this.idTiquete = idTiquete;
			this.comprador = comprador;
			this.sillaTiquete = sillaTiquete;
			this.viaje = viaje;
			this.valor = valor;
			this.fechaCompra = fechaCompra;
		}
	/*
	public  Tiquete(){
		System.out.println("No se encontraron tiquetes disponibles");
	}
	
	
=======
	public Tiquete(){}

>>>>>>> master
	public Tiquete(Silla sillaTiquete, Viaje viaje, int valor) {
		this.sillaTiquete = sillaTiquete;
		this.viaje = viaje;
		this.valor = valor;
	}
	*/

	// ----- G E T   A N D   S E T -----

	

	public Silla getSillaTiquete() {return sillaTiquete;}

	public Viaje getViaje() {return viaje;	}

	public Comprador getComprador() {return comprador;}

	public void setComprador(Comprador comprador) {this.comprador = comprador;}

	public int getValor() {	return valor;}

<<<<<<< HEAD
	public int getIdTiquete() {
		return idTiquete;
	}

=======
	public void setFechaCompra(LocalDate fechaCompra) {	this.fechaCompra = fechaCompra;	}
>>>>>>> master

}

