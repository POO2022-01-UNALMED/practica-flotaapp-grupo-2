package terminal;

import baseDatos.Serializador;

import java.util.ArrayList;
import java.util.Date;
import java.io.Serializable;


public class Usuario implements Serializable {

    public int cc;
    public String uNombre;
    public String email;
    public long movil;
    public int billetera;

    public Usuario(int cc, String uNombre, String email, long movil) {
        this.cc = cc;
        this.uNombre = uNombre;
        this.email = email;
        this.movil = movil;
        this.billetera = 0;
    }

    public Usuario(int cc, String uNombre, String email, long movil, int billetera) {
        this.cc = cc;
        this.uNombre = uNombre;
        this.email = email;
        this.movil = movil;
        this.billetera = billetera;
    }

    public void registrarse(){}
    public void  modificarInformacion(){}

    public void  darseDeBaja(){}

    public int consultarSaldo(){
        return this.billetera;
    }

    public int agregarSaldo(int dinero){
        if(dinero > 0){
            this.billetera += dinero;
        }else{
            System.out.println("El dinero a agregar debe ser en numeros positivos");
        }
        return this.consultarSaldo();
    }

}