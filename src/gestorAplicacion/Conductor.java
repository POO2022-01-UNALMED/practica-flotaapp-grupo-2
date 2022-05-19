package gestorAplicacion;

import java.util.ArrayList;

public class Conductor extends Empleado {

    private Viaje historiaViajesRealizados;
    private Categoria categoria;
    private static ArrayList<Conductor> conductores = new ArrayList<>();
    static {
        conductores = new ArrayList<Conductor>();
    }

    public Conductor(int cc, String uNombre, String email, long movil) {
        super(cc, uNombre, email, movil);
    }

    public void registrarse() {}

    public void modificarinformacion() {}

    //public Conductor aumenarCategoria(String Categoria) {}

    public void despedir() {}

    public void renunciar() {}

}