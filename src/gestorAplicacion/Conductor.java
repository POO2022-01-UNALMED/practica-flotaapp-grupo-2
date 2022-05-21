package gestorAplicacion;

import java.util.ArrayList;

public class Conductor extends Empleado {

    private ArrayList<Viaje> historiaViajesRealizados;
    private Categoria categoria;
    private static ArrayList<Conductor> conductores = new ArrayList<>();
    static {
        conductores = new ArrayList<Conductor>();
    }

    public Conductor(int cc, String uNombre, String email, long movil, Categoria categoria) {

        super(cc, uNombre, email, movil);
        this.categoria = categoria;
        this.historiaViajesRealizados = new ArrayList<Viaje>();
    }

    public void registrarse() {}

    public void modificarinformacion() {}

    public void anadirViajeHistoria(Viaje viaje) {this.historiaViajesRealizados.add(viaje);}

    //public Conductor aumenarCategoria(String Categoria) {}

    public void despedir() {}

    public void renunciar() {}

}