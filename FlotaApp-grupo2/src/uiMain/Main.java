package uiMain;

import  terminal.*;


public class Main {
    public static void main(String[] args) {
        Usuario u1 = new Usuario();
        System.out.println(u1);

        Silla s1 = new Silla();
        System.out.println(s1.getEstado());
        s1.ocuparSilla();
        System.out.println(s1.getEstado());
        s1.liberarSilla();
        System.out.println(s1.getEstado());
    }
}
