package uiMain;

import  terminal.*;

import baseDatos.*;


public class Main {
    public static void main(String[] args) {
        Deserializador.deserializarTodo();
        Comprador u1 = new Comprador(1, "Mateo E", "example@email.com", 3234567890L);
        u1.registrarse();

        Comprador u2 = new Comprador(2, "Pablo", "example2@email.com", 3087654321L);
        u2.registrarse();
        System.out.println(Comprador.getCompradores());

        u2.modificarInformacion("Pablito", "example3@gmail.com", 3003333333L);
        System.out.println(Comprador.getCompradores());

        Comprador u3 = new Comprador(2, "Coco", "example5@email.com", 3087679321L);
        u3.registrarse();

        System.out.println(Comprador.getCompradores());

    }
}
