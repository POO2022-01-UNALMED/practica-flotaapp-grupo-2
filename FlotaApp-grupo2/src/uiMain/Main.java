package uiMain;

import  terminal.*;

import baseDatos.*;


public class Main {
    public static void main(String[] args) {
        Deserializador.deserializarTodo();
        Usuario u1 = new Usuario();
        //System.out.println(u1);
        u1.registrarse(1, "Mateo E", "example@email.com", 1234567890);
        //System.out.println(u1);

        Usuario u2 = new Usuario();
        //System.out.println(u2);
        u2.registrarse(2, "Pablo", "example2@email.com", 2087654321);
        //System.out.println(u2);
        System.out.println(Usuario.getUsuarios());
        Usuario.eliminarUsuario(u2.toString());

        //Test Metodos Silla
        Silla s1 = new Silla();
        //System.out.println(s1.getEstado());
        s1.ocuparSilla();
        //System.out.println(s1.getEstado());
        s1.liberarSilla();
        //System.out.println(s1.getEstado());

        //Test Metodos Usuario
        //System.out.println(u1.consultarSaldo());
        u1.agregarSaldo(1000);
        //System.out.println(u1.consultarSaldo());
        u1.agregarSaldo(-1000);
        //System.out.println(u1.consultarSaldo());


    }
}
