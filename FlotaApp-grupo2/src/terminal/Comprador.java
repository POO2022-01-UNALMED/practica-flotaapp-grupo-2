package terminal;

import baseDatos.Serializador;

import java.util.ArrayList;
import java.io.Serializable;

import java.util.HashMap;
import java.util.Map;
import java.util.stream.Collectors;
import java.util.LinkedHashMap;

public class Comprador extends Usuario implements Serializable{
    private ArrayList<Viaje> historicoViajes;
    private static ArrayList<Usuario> compradores;
    static {
        compradores = new ArrayList<Usuario>();
    }

    public Comprador(int cc, String uNombre, String email, long movil) {
        super(cc, uNombre, email, movil);
        this.historicoViajes =  new ArrayList<>();
    }

    public Comprador(int cc, String uNombre, String email, long movil, int billetera,  ArrayList<Viaje> historicoViajes) {
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
            System.out.println("Usuario-" + this.cc + " guardado con exito");
            Comprador.compradores.add(this);
            Serializador.serializarTodo();
        }
    }

    public void modificarInformacion(String uNombre, String email, long movil){
        Comprador aux = new Comprador(this.cc, uNombre, email, movil, this.billetera, this.historicoViajes);
        this.darseDeBaja();
        aux.registrarse();
    }


    public void darseDeBaja(){
        Comprador.compradores.remove(this);
        Serializador.serializarTodo();
    }




    /*public ArrayList<Tiquete> historicoViaje(Date fechaInicial, Date fechaFinal){
        ArrayList<Tiquete> viajes = new ArrayList<Tiquete>();
        for(tiquete : Tiquete.getTiquete()){
            Date d = tiquete.viaje.getFechaViaje();
            if (d.after(fechaInicial) && d.before(fechaFinal)){
                viajes.add(tiquete);
            }
        }
        return viajes;
    }*/

    /*public int historicoViaje(Ciudad ciudad){
        int cantidad = 0;
        for(tiquete : Tiquete.getTiquete()){
            if (tiquete.viaje.getCiudad() == ciudad){
                cantidad += 1;
            }
        }
        return cantidad;
    }*/

    /*public ArrayList<Ciudad> recomendacion(){
        Map<Ciudad, Integer> masVisitados = Ciudad.getCiudades().entrySet().stream().sorted(Map.Entry.comparingByValue()).collect(Collectors.toMap(Map.Entry::getKey, Map.Entry::getValue, (e1, e2) -> e1, LinkedHashMap::new));
        return masVisitados[:5];
    }*/



    //Metodos Staticos
    public static ArrayList<Usuario> getCompradores(){
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
