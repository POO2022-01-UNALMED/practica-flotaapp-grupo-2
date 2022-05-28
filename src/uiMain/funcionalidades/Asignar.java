package uiMain.funcionalidades;

import gestorAplicacion.*;

import java.io.Serializable;
import java.util.ArrayList;

public class Asignar implements Serializable {
    public static Tiquete asignarTiquete(Comprador comprador, Viaje viaje, int presupuesto){
        for(Tiquete tiquete : viaje.getAllTiquetes()){
            if(tiquete.getValor() <= presupuesto && tiquete.getSillaTiquete().getEstado() == false) {
                tiquete.setComprador(comprador);
                tiquete.getSillaTiquete().setEstado(true);
                comprador.anadirTiqueteHistoria(tiquete);
                viaje.getDestino().anadirVisitantes(1);
                return tiquete;
            }
        }
        return new Tiquete();
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
