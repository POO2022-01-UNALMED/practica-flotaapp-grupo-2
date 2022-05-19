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

    public Comprador(int cc, String uNombre, String email, long movil) {
        super(cc, uNombre, email, movil, 0);
        this.historicoViajes =  new ArrayList<>();
    }

    public Comprador(int cc, String uNombre, String email, long movil, int billetera,  ArrayList<Tiquete> historicoViajes) {
        super(cc, uNombre, email, movil, billetera);
        this.historicoViajes = historicoViajes;
    }

    public void registrarse(){
        ArrayList<String> emails = new ArrayList<String>();
        ArrayList<Integer> ccs = new ArrayList<Integer>();
        ArrayList<Long> movils = new ArrayList<Long>();

        for(Usuario comprador : Comprador.getCompradores()){
            emails.add(comprador.email);
            ccs.add(comprador.cc);
            movils.add(comprador.movil);
        }
        if (emails.contains(this.email) || ccs.contains(this.cc) || movils.contains(this.movil) )
        {
            System.out.println("Este Usuario ya esta registrado");
        }else{
            Comprador.compradores.add(this);
        }
    }

    public void modificarNombre(String nombre){
        this.uNombre = nombre;
    }

    public void modificarEmail(String email){
        this.email = email;
    }

    public void modificarMovil(long movil){
        this.movil = movil;
    }


    public void darseDeBaja(){
        Comprador.compradores.remove(this);
    }


    public ArrayList<Tiquete> historicoViaje(Date fechaInicial, Date fechaFinal){
        ArrayList<Tiquete> viajes = new ArrayList<Tiquete>();
        for(Tiquete tiquete : Tiquete.getTiquetes()){
            System.out.println(tiquete);
            Date d = tiquete.getViaje().getFechaViaje();
            if (d.after(fechaInicial) && d.before(fechaFinal) && tiquete.getUsuario() == this){
                viajes.add(tiquete);
            }
        }
        return viajes;
    }

    public int historicoViaje(Ciudad ciudad){
        int cantidad = 0;
        for(Tiquete tiquete : Tiquete.getTiquetes()){
            if (tiquete.getViaje().getDestino().contains(ciudad)){
                cantidad += 1;
            }
        }
        return cantidad;
    }

    /*public ArrayList<Ciudad> recomendacion(){
        Map<Ciudad, Integer> masVisitados = Ciudad.getCiudades().entrySet().stream().sorted(Map.Entry.comparingByValue()).collect(Collectors.toMap(Map.Entry::getKey, Map.Entry::getValue, (e1, e2) -> e1, LinkedHashMap::new));
        return masVisitados[:5];
    }*/


    public ArrayList<Tiquete> getHistoricoViajes() {
        return historicoViajes;
    }

    public void anadirTiqueteHistoria(Tiquete tiquete) {this.historicoViajes.add(tiquete);}

    //Metodos Staticos
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