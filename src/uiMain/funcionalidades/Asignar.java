/*
 * Clase que permite asignar un tiquete a un Comprador, un vehiculo a un especialista 
 * Estructuras: ArrayList
 * 
 * @author: Mateo Hechavarria, Juan Pablo Pineda, Miguel Angel Fonseca, Haison Urrutia
 */



package uiMain.funcionalidades;

import gestorAplicacion.*;

import java.io.Serializable;
import java.time.LocalDate;
import java.util.ArrayList;

public class Asignar implements Serializable {
    public static Tiquete asignarTiquete(Comprador comprador, Tiquete tiquete){
        tiquete.setComprador(comprador);
        tiquete.setFechaCompra(LocalDate.now());
        tiquete.setEstado(true);
        comprador.anadirTiqueteHistoria(tiquete);
        tiquete.getViaje().getDestino().anadirVisitantes(1);
        return tiquete;
    }
    public static Viaje asignarVehiculo(Conductor conductor, Viaje viaje){
        viaje.setConductor(conductor);
        conductor.anadirViajeHistoria(viaje);
        return viaje;
    }
    public static String asignarVehiculo(Especialista mecanico, Vehiculo vehiculo){
        mecanico.anadirVehiculoHistoria(vehiculo);
        return mecanico.revisionVehiculo(vehiculo);
    }
}
