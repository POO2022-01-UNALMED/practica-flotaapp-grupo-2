package gestorAplicacion;

import java.io.Serializable;
import java.util.ArrayList;

public class Silla implements Serializable {
	private enum ubicacion {PASILLO, VENTANA, INTERMEDIO}

    private int numeroSilla;
    private boolean tipo; //0 - Estandar , 1 - Premium
    private Ubicacion ubicacion; //0 - V , 1 - P
    private boolean estado;
    
    public Silla(int numeroSilla, boolean tipo, Ubicacion ubicacion) {
    	this.numeroSilla = numeroSilla;
    	this.tipo = tipo;
    	this.ubicacion = ubicacion;
    	this.estado = false;
    	
    }

    public int getNumeroSilla() {      return numeroSilla;   }

    public boolean getTipo() { return  tipo;}

    public boolean getEstado() {
        return estado;
    }
    
    public void setEstado(boolean estado) {
    	this.estado = estado;
    }

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
