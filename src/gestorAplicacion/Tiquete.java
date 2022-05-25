package gestorAplicacion;

import java.io.Serializable;
import java.util.Date;
import java.util.ArrayList;

public class Tiquete implements Serializable {
	private int idTiquete = 0;
	private Comprador comprador;
	private Silla sillaTiquete;
	private Viaje viaje;
	private int valor;
	private Date fechaCompra;
	private static ArrayList<Tiquete> tiquetes = new ArrayList<>();
	static {
		tiquetes = new ArrayList<Tiquete>();
	}

	public  Tiquete(){
		System.out.println("No se encontraron tiquetes disponibles");
	}

	public Tiquete(Silla sillaTiquete, Viaje viaje, int valor) {
		this.idTiquete += 1;
		this.sillaTiquete = sillaTiquete;
		this.viaje = viaje;
		this.valor = valor;
		tiquetes.add(this);
	}

	//public void crearTiquete(Tiquete nuevo) {

	//k}


	public Silla getSillaTiquete() {return sillaTiquete;}

	public Viaje getViaje() {return viaje;	}

	public Comprador getUsuario() {return comprador;}

	public void setComprador(Comprador comprador) {this.comprador = comprador;}

	public int getValor() {	return valor;}

	public static ArrayList<Tiquete> getTiquetes(){	return tiquetes;}

}
