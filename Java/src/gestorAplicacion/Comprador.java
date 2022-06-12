/*
 * Clase con las funciones de Comprador  necesarias para almacenar la información del comprador y generar funciones 
 * Estructuras: ArrayList y sus funciones, herencia
 * 
 * @author: Mateo Hechavarria, Juan Pablo Pineda, Miguel Angel Fonseca, Haison Urrutia
 */



package gestorAplicacion;

import baseDatos.Deserializador;
import baseDatos.Serializador;
import uiMain.funcionalidades.Asignar;

import java.time.LocalDate;
import java.util.ArrayList;
import java.io.Serializable;

import java.util.HashMap;
import java.util.Map;
import java.util.Date;
import java.util.stream.Collectors;
import java.util.LinkedHashMap;

public class Comprador extends Usuario implements Serializable{
	
	private static final long serialVersionUID = 2L;

    private ArrayList<Tiquete> historicoViajes;
    private static ArrayList<Comprador> compradores;
    static {
        compradores = new ArrayList<Comprador>();
    }

    //CONSTRUCTOR
    public Comprador(){super(0, "USUARIO NO EXISTENTE", "usuarioInexistente@error.exe" , 666);this.historicoViajes =  new ArrayList<>();}

    public Comprador(int cc, String uNombre, String email, long movil) {
        super(cc, uNombre, email, movil, 0);
        this.historicoViajes =  new ArrayList<>();
        Comprador.compradores.add(this);
    }


    public void darseDeBaja(){
        Comprador.compradores.remove(this);
    }

    public Tiquete comprarTiquete(Ciudad salida, Ciudad destino, int presupuesto){
        Tiquete tiqueteFinal;
        for(Viaje viaje: Viaje.getViajes()){
            if(viaje.getDestino() == destino && viaje.getOrigen() == salida){
                tiqueteFinal = viaje.tiqueteDisponible(presupuesto);
                if( tiqueteFinal.getViaje() != new Tiquete().getViaje()){
                    return  Asignar.asignarTiquete(this, tiqueteFinal);
                }
            }
        }
        return new Tiquete();
    }


    public ArrayList<Tiquete> historicoViaje(LocalDate fechaInicial, LocalDate fechaFinal){
        ArrayList<Tiquete> viajes = new ArrayList<Tiquete>();
        for(Tiquete tiquete : this.getHistoricoViajes()){
            LocalDate d = tiquete.getViaje().getFechaViaje();
            if (d.isAfter(fechaInicial) && d.isBefore(fechaFinal)){
                viajes.add(tiquete);
            }
        }
        return viajes;
    }

    public int historicoViaje(Ciudad ciudad){
        int cantidad = 0;
        for(Tiquete tiquete : this.getHistoricoViajes()){
            if (tiquete.getViaje().getDestino()== ciudad){
                cantidad += 1;
            }
        }
        return cantidad;
    }

    // ----- G E T   A N D   S E T -----

    public ArrayList<Tiquete> getHistoricoViajes() {
        return historicoViajes;
    }

    public void anadirTiqueteHistoria(Tiquete tiquete) {this.historicoViajes.add(tiquete);}

    public void eliminarTiqueteHistoria(Tiquete tiquete) {this.historicoViajes.remove(tiquete);}

    public void modificarNombre(String nombre){
        this.uNombre = nombre;
    }

    public void modificarEmail(String email){
        this.email = email;
    }

    public void modificarMovil(long movil){
        this.movil = movil;
    }

    public static ArrayList<Comprador> getCompradores(){
        return compradores;
    }

    @Override
    public String toString() {
        return "Comprador{" +
                "cc :" + cc +
                ", Nombre : " + uNombre +
                ", email : " + email  +
                ", movil :" + movil +
                '}';
    }
}