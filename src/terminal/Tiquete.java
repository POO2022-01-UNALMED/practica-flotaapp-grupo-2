package terminal;

import java.util.Date;
import java.util.ArrayList;

public class Tiquete {
	private int idTiquete;
	private Usuario usuario;
	private Viaje viaje;
	private int valor;
	private Date fechaCompra;
	private static ArrayList<Tiquete> tiquetes = new ArrayList<>();
	
	
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
