package uiMain;

import  terminal.*;

import baseDatos.*;


public class Main {
    public static void main(String[] args) {
        Deserializador.deserializarTodo();
        Usuario u1 = new Usuario();
        u1.Usuario(1, "Mateo E", "example@email.com", 3234567890L);
        u1.registrarse();

        Usuario u2 = new Usuario();
        u2.Usuario(2, "Pablo", "example2@email.com", 3087654321L);
        u2.registrarse();
        System.out.println(Usuario.getUsuarios());

        u2.modificarInformacion("Pablito", "example3@gmail.com", 3003333333L);
        System.out.println(Usuario.getUsuarios());

        Usuario u3 = new Usuario();
        u3.Usuario(2, "Coco", "example5@email.com", 3087679321L);
        u3.registrarse();

        System.out.println(Usuario.getUsuarios());

    }
}
