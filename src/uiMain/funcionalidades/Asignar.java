package uiMain.funcionalidades;

import gestorAplicacion.*;

import java.io.Serializable;

public class Asignar implements Serializable {
    public static Tiquete asignarTiquete(Comprador comprador, Tiquete tiquete){
        tiquete.setComprador(comprador);
        comprador.anadirTiqueteHistoria(tiquete);
        return tiquete;
    }
    public static Viaje asignarViaje(Conductor conductor, Viaje viaje){
        viaje.getVehiculo().setConductor(conductor);
        conductor.anadirViajeHistoria(viaje);
        return viaje;
    }
    public static String asignarVehiculo(Especialista mecanico, Vehiculo vehiculo){
        mecanico.anadirVehiculoHistoria(vehiculo);
        return mecanico.revisionVehiculo(vehiculo);
    }
}
