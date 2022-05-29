package gestorAplicacion;

import baseDatos.Deserializador;
import baseDatos.Serializador;

import java.util.ArrayList;
import java.io.Serializable;

import java.util.HashMap;
import java.util.Map;
import java.util.Date;
import java.util.stream.Collectors;
import java.util.LinkedHashMap;

public class Comprador extends Usuario implements Serializable{

    private ArrayList<Tiquete> historicoViajes;
    private static ArrayList<Comprador> compradores;
    static {
        compradores = new ArrayList<Comprador>();
    }

    //CONSTRUCTOR
    public Comprador(int cc, String uNombre, String email, long movil) {
        super(cc, uNombre, email, movil, 0);
        this.historicoViajes =  new ArrayList<>();
        Comprador.compradores.add(this);
    }


    public void darseDeBaja(){
        Comprador.compradores.remove(this);
    }


    public ArrayList<Tiquete> historicoViaje(Date fechaInicial, Date fechaFinal){
        ArrayList<Tiquete> viajes = new ArrayList<Tiquete>();
        for(Tiquete tiquete : this.getHistoricoViajes()){
            Date d = tiquete.getViaje().getFechaViaje();
            if (d.after(fechaInicial) && d.before(fechaFinal)){
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


    //Metodos Auxiliares
    @Override
    public String toString() {
        return "Usuario{" +
                "cc=" + cc +
                ", uNombre='" + uNombre + '\'' +
                ", email='" + email + '\'' +
                ", movil=" + movil +
                ", billetera=" + billetera +
                ", historicoViajes=" + historicoViajes +
                '}';
    }
}