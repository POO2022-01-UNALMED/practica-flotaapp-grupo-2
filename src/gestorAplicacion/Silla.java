package gestorAplicacion;

import java.io.Serializable;
import java.util.ArrayList;

public class Silla implements Serializable {
	private enum ubicacion {PASILLO, VENTANA, INTERMEDIO}

    private int numeroSilla;
    private boolean tipo; //0 (false) -> Estandar , 1 (true) - Premium
    private Ubicacion ubicacion; //0 - V , 1 - P
    private boolean estado;
	private static  ArrayList<Silla> sillas;
	static {
		sillas = new ArrayList<Silla>();
	}


	public Silla(int numeroSilla, boolean tipo, Ubicacion ubicacion) {
    	this.setNumeroSilla(numeroSilla);
    	this.setTipo(tipo);
    	this.setUbicacion(ubicacion);
    	this.estado = false;
    	Silla.sillas.add(this);
    }

    public int getNumeroSilla() {      return numeroSilla;   }

    public boolean getTipo() { return  tipo;}

    public boolean getEstado() {
        return estado;
    }
    
    public void setEstado(boolean estado) {
    	this.estado = estado;
    }

	public void setNumeroSilla(int numeroSilla) {
		this.numeroSilla = numeroSilla;
	}

	public boolean isTipo() {
		return tipo;
	}

	public void setTipo(boolean tipo) {
		this.tipo = tipo;
	}

	public Ubicacion getUbicacion() {
		return ubicacion;
	}

	public void setUbicacion(Ubicacion ubicacion) {
		this.ubicacion = ubicacion;
	}

	public static ArrayList<Silla> getSillas() {	return sillas;	}

	@Override
    public String toString() {
        return "Silla{" +
                "numeroSilla=" + numeroSilla +
                ", tipo=" + tipo +
                ", ubicacion=" + ubicacion +
                ", estado=" + estado +
                '}';
    }
}
