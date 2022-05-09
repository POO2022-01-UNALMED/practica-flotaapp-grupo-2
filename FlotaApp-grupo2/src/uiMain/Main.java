package uiMain;

import  terminal.*;


public class Main {
    public static void main(String[] args) {
        Usuario u1 = new Usuario();
        System.out.println(u1);
        u1.registrarse(1, "Mateo E", "example@email.com", 1234567890);
        System.out.println(u1);

        //Test Metodos Silla
        Silla s1 = new Silla();
        //System.out.println(s1.getEstado());
        s1.ocuparSilla();
        //System.out.println(s1.getEstado());
        s1.liberarSilla();
        //System.out.println(s1.getEstado());

        //Test Metodos Usuario
        System.out.println(u1.consultarSaldo());
        u1.agregarSaldo(1000);
        System.out.println(u1.consultarSaldo());
        u1.agregarSaldo(-1000);
        System.out.println(u1.consultarSaldo());
    }
}
