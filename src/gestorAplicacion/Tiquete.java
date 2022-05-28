package gestorAplicacion;

import java.io.Serializable;
import java.util.Date;
//import java.util.ArrayList;

public class Tiquete implements Serializable {
	protected int id;
	protected Comprador comprador;
	protected Silla sillaTiquete;
	protected Viaje viaje;
	protected int valor;
	protected Date fechaCompra;

	public  Tiquete(){
		System.out.println("No se encontraron tiquetes disponibles");
	}

	public Tiquete(int id, Silla sillaTiquete, Viaje viaje, int valor) {
		this.id = id;
		this.sillaTiquete = sillaTiquete;
		this.viaje = viaje;
		this.valor = valor;
	}

	// ----- G E T   A N D   S E T -----

	public Silla getSillaTiquete() {return sillaTiquete;}

	public Viaje getViaje() {return viaje;	}

	public Comprador getUsuario() {return comprador;}

	public void setComprador(Comprador comprador) {this.comprador = comprador;}

	public int getValor() {	return valor;}


}

