package uiMain.funcionalidades;

import gestorAplicacion.*;

public class Asignar {
    public static Tiquete asignarTiquete(Comprador comprador, Tiquete tiquete){
        tiquete.setComprador(comprador);
        comprador.anadirTiqueteHistoria(tiquete);
        return tiquete;
    }
    public Viaje asignarViaje(Conductor conductor, Viaje viaje){
        viaje.getVehiculo().setConductor(conductor);
        conductor.anadirViajeHistoria(viaje);
        return viaje;
    }
    public String asignarVehiculo(Especialista mecanico, Vehiculo vehiculo){

    }
}
