<<<<<<< HEAD:src/terminal/Tiquete.java
package terminal;

import java.util.Date;
import java.util.ArrayList;

public class Tiquete {
	private int idTiquete;
	private Usuario usuario;
=======
package gestorAplicacion;

import java.io.Serializable;
import java.util.Date;
import java.util.ArrayList;

public class Tiquete implements Serializable {
	private int idTiquete;
	private Comprador comprador;
>>>>>>> master:src/gestorAplicacion/Tiquete.java
	private Viaje viaje;
	private int valor;
	private Date fechaCompra;
	private static ArrayList<Tiquete> tiquetes = new ArrayList<>();
<<<<<<< HEAD:src/terminal/Tiquete.java
	
	
	public Tiquete(int idTiquete, Usuario usuario, Viaje viaje, int valor, Date fechaCompra) {
		this.setIdTiquete(idTiquete); 
		this.setUsuario(usuario);
		this.setViaje(viaje);
		this.setValor(valor);
		this.setFechaCompra(fechaCompra);
		tiquetes.add(this);		
	}
	
	/*
	public void crearTiquete() {    //Se puede pasar como argumento el id
									// Se debe validar que el viaje este activo y que la silla no este ocupada.
		if ((!tiquetes.contains(this)) &&  ) {
			tiquetes.add(this);
		}else {
			System.out.println("El tiquete ya ha sido creado");
		}
	}*/
//////////////////
	public int getIdTiquete() {
		return idTiquete;
	}

	public void setIdTiquete(int idTiquete) {
		this.idTiquete = idTiquete;
	}

	public Usuario getUsuario() {
		return usuario;
	}

	public void setUsuario(Usuario usuario) {
		this.usuario = usuario;
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
	
	

}
=======
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
>>>>>>> master:src/gestorAplicacion/Tiquete.java
