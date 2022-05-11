package terminal;

import baseDatos.Serializador;

import java.util.ArrayList;
import java.io.Serializable;

public class Usuario implements Serializable {

    private int cc;
    private String uNombre;
    private String email;
    private long movil;
    private int cartera;
    private ArrayList<Viaje> historicoViajes;
    private static ArrayList<Usuario> usuarios;
    static {
        usuarios = new ArrayList<Usuario>();
    }

    public void Usuario(int cc, String uNombre, String email, long movil){
        this.cc = cc;
        this.uNombre = uNombre;
        this.email = email;
        this.movil = movil;
        this.cartera = 0;
        this.historicoViajes = new ArrayList<>();
    }

    public void Usuario(int cc, String uNombre, String email, long movil, int cartera, ArrayList<Viaje> historicoViajes){
        this.cc = cc;
        this.uNombre = uNombre;
        this.email = email;
        this.movil = movil;
        this.cartera = cartera;
        this.historicoViajes = historicoViajes;
    }

    public void registrarse(){
        ArrayList<String> emails = new ArrayList<String>();
        ArrayList<Integer> ccs = new ArrayList<Integer>();
        ArrayList<Long> movils = new ArrayList<Long>();

        for(Usuario usuario : Usuario.getUsuarios()){
            emails.add(usuario.email);
            ccs.add(usuario.cc);
            movils.add(usuario.movil);
        }
        if (emails.contains(this.email) || ccs.contains(this.cc) || movils.contains(this.movil) )
        {
            System.out.println("Este Usuario ya esta registrado");
        }else{
            System.out.println("Usuario-" + this.cc + " guardado con exito");
            Usuario.usuarios.add(this);
            Serializador.serializarTodo();
        }
    }

    public void modificarInformacion(String uNombre, String email, long movil){
        Usuario aux = new Usuario();
        aux.Usuario(this.cc, uNombre, email, movil, this.cartera, this.historicoViajes);
        this.darseDeBaja();
        aux.registrarse();
    }


    public void darseDeBaja(){
        Usuario.usuarios.remove(this);
        Serializador.serializarTodo();
    }

    public int consultarSaldo(){
        return this.cartera;
    }

    public int agregarSaldo(int dinero){
        if(dinero > 0){
            this.cartera += dinero;
        }else{
            System.out.println("El dinero a agregar debe ser en numeros positivos");
        }
        return this.consultarSaldo();
    }

    public static ArrayList<Usuario> getUsuarios(){
        return usuarios;
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


}
