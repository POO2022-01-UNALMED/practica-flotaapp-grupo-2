package terminal;

import java.util.ArrayList;

public class Usuario {

    private int cc;
    private String uNombre;
    private String email;
    private int movil;
    private int cartera;
    private ArrayList<Usuario> historicoViajes;

    @Override
    public String toString() {
        return "Usuario{" +
                "cc=" + cc +
                ", uNombre='" + uNombre + '\'' +
                ", email='" + email + '\'' +
                ", movil=" + movil +
                ", cartera=" + cartera +
                ", historicoViajes=" + historicoViajes +
                '}';
    }

    public void registrarse(int cc, String uNombre, String email, int movil){
        this.cc = cc;
        this.uNombre = uNombre;
        this.email = email;
        this.movil = movil;
        this.cartera = 0;
        this.historicoViajes = new ArrayList<>();
    }

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
