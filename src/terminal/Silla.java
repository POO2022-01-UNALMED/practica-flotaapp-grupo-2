package terminal;

import java.util.ArrayList;

public class Silla {
	private enum ubicacion {PASILLO, VENTANA, INTERMEDIO}

    private int numeroSilla;
    private boolean tipo; //0 - Estandar , 1 - Booleana
    private Ubicacion ubicacion; //0 - V , 1 - P
    private boolean estado;
    
    public Silla(int numeroSilla, boolean tipo, boolean ubicacion, boolean estado) {
    	this.numeroSilla = numeroSilla;
    	this.tipo = tipo;
    	this.ubicacion = ubicacion;
    	this.estado = estado;
    	
    }

    public Silla ocuparSilla(){
        this.estado = true;
        return this;
    }

    public Silla liberarSilla(){
        this.estado = false;
        return this;
    }

    public boolean getEstado() {
        return estado;
    }
    
    public void setEstado(boolean estado) {
    	this.estado = estado;
    }
    
    
}
