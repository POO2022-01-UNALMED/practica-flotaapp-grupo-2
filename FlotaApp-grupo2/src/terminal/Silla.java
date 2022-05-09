package terminal;

public class Silla {

    private int numeroSilla;
    private boolean tipo; //0 - Estandar , 1 - Booleana
    private boolean ubicacion; //0 - V , 1 - P
    private boolean estado;

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
}
