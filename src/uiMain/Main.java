package uiMain;

import  gestorAplicacion.*;

import baseDatos.*;

import java.util.ArrayList;
import java.util.Date;


public class Main {
    public static void main(String[] args) {
        //Deserializador.deserializarTodo();

        // COMPRADORES
        Comprador u1 = new Comprador(1, "Usuario1", "example@email.com", 3234567890L);
        u1.registrarse();

        Comprador u2 = new Comprador(2, "Usuario2", "example2@email.com", 3087654321L);
        u2.registrarse();

        Comprador uError = new Comprador(2, "Error", "example2@email.com", 3087654321L);
        uError.registrarse();

        Comprador u3 = new Comprador(3, "Usuario3", "example3@email.com", 3088890321L);
        u3.registrarse();

        Comprador u4 = new Comprador(4, "Usuario4", "example4@email.com", 3087656654L);
        u4.registrarse();


        u1.darseDeBaja();
        u2.modificarNombre("Usuario2Modificado");
        u3.modificarEmail("emailModificado@example.com");
        u4.modificarMovil(3333333333L);

        Serializador.serializarTodo();

        ////FECHAS PRUEBAS

        Date fin = new Date(2022,1,1);
        Date inicio = new Date(2020,3,12);
        Date intermedio = new Date(2020,7,14);
        Date fechaCompra = new Date(2020,6,22);

        System.out.println(u2.historicoViaje(inicio, fin));

        ////CIUDADES

        Ciudad c1 = new Ciudad(1,"Medellin", "calle X - 95");
        Ciudad c2 = new Ciudad(2,"Bello", "calle Y - 72");
        Ciudad c3 = new Ciudad(3,"Popayan", "calle X - 37");
        Ciudad c4 = new Ciudad(4,"Cali", "calle F - 13");
        ArrayList<Ciudad> destinos = new ArrayList<>();
        destinos.add(c1);
        destinos.add(c4);

        //VIAJES
        Viaje v1 = new Viaje(1112, 300000, c2,destinos,intermedio, true, true);

        //TIQUETES
        Tiquete t1 = new Tiquete(1,u2,v1,4000,fechaCompra);

        //////funcionamiento de Comprador.historicoViaje => (DATE, DATE) --- (CIUDAD)
        System.out.println(u2.historicoViaje(inicio, fin));
        System.out.println(u2.historicoViaje(c4));


        //EMPLEADOS


        ////CONDUCTORES


        //////SILLAS

        System.out.println(Comprador.getCompradores());
        Serializador.serializarTodo();
    }
}