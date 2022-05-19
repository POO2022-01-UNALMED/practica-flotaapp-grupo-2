package uiMain.funcionalidades;

import gestorAplicacion.*;

public class Asignar {
    public static Tiquete asignarTiquete(Comprador comprador, Tiquete tiquete){
        tiquete.setComprador(comprador);
        comprador.anadirTiqueteHistoria(tiquete);
        return tiquete;
    }
    //public Viaje asignarViaje(Conductor conductor, Ciudad ciudad){ }
    //public String asignarTiquete(Especialista mecanico, Vehiculo vehiculo){ }
}
