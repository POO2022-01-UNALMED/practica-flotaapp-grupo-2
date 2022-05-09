package terminal;

import java.util.ArrayList;

public class Usuario {

    private int cc;
    private String uNombre;
    private String email;
    private int movil;
    private int cartera;
    private ArrayList<Usuario> historicoViajes;

    public int consultarSaldo(){
        return this.cartera;
    }

    public void agregarSaldo(int dinero){
        if(dinero > 0){
            this.cartera += dinero;
        }else{
            System.out.println("El dinero a agregar debe ser en numeros positivos");
        }
    }

}
