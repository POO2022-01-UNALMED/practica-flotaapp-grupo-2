package terminal;

import java.util.ArrayList;
import java.io.Serializable;

public class Usuario implements Serializable {

    private int cc;
    private String uNombre;
    private String email;
    private int movil;
    private int cartera;
    private ArrayList<Viaje> historicoViajes;
    private static ArrayList<Usuario> usuarios;
    static {
        usuarios = new ArrayList<Usuario>();
    }

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
        Usuario.usuarios.add(this);
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

    public static ArrayList<Usuario> getUsuarios(){
        return usuarios;
    }

}
