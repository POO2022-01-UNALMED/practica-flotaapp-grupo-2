package gestorAplicacion;

import java.io.Serializable;
import java.util.Date;
import java.util.ArrayList;

public class Tiquete implements Serializable {
	private Comprador comprador;
	private Silla sillaTiquete;
	private Viaje viaje;
	private int valor;
	private Date fechaCompra;

	public  Tiquete(){
		System.out.println("No se encontraron tiquetes disponibles");
	}

	public Tiquete(Silla sillaTiquete, Viaje viaje, int valor) {
		this.sillaTiquete = sillaTiquete;
		this.viaje = viaje;
		this.valor = valor;
	}

	//public void crearTiquete(Tiquete nuevo) {

	//k}

	public Silla getSillaTiquete() {return sillaTiquete;}

	public Viaje getViaje() {return viaje;	}

	public Comprador getUsuario() {return comprador;}

	public void setComprador(Comprador comprador) {this.comprador = comprador;}

	public int getValor() {	return valor;}


}
