/*
 * Clase con las funciones de Usuario  necesarias almacenar la información de usuario y ser super clase de especialista, Comprador y Conductor
 * Estructuras: funciones
 * 
 * @author: Mateo Hechavarria, Juan Pablo Pineda, Miguel Angel Fonseca, Haison Urrutia
 */



package gestorAplicacion;

import baseDatos.Serializador;

import java.util.ArrayList;
import java.util.Date;
import java.io.Serializable;


public abstract class Usuario implements Serializable {

    protected int cc;
    protected String uNombre;
    protected String email;
    protected long movil;
    protected double billetera;
    private static final long serialVersionUID = 8L;

    public Usuario(int cc, String uNombre, String email, long movil) {
        this(cc,uNombre,email,movil,0);
    }

    public Usuario(int cc, String uNombre, String email, long movil, int billetera) {
        this.cc = cc;
        this.uNombre = uNombre;
        this.email = email;
        this.movil = movil;
        this.billetera = billetera;
    }

    public double consultarSaldo(){
        return this.billetera;
    }

    public void agregarSaldo(double dinero){
    	this.billetera += dinero;
    }

    public String getuNombre() {    return uNombre;   }

    public int getCc() {       return cc;   }


}