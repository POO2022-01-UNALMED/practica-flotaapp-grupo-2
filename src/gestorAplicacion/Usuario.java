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
    protected int billetera;

    public Usuario(){}

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

    public int consultarSaldo(){
        return this.billetera;
    }

    public double agregarSaldo(double dinero){
        if(dinero > 0){
            this.billetera += dinero;
        }else{
            System.out.println("El dinero a agregar debe ser en numeros positivos");
        }
        return this.consultarSaldo();
    }

    public String getuNombre() {  return uNombre; }

    public int getCc() {  return cc;  }
}