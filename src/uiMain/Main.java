package uiMain;

import gestorAplicacion.*;

import baseDatos.*;
import uiMain.funcionalidades.*;

import java.util.ArrayList;
import java.util.Date;


public class Main {
    public static void main(String[] args) {
        Deserializador.deserializarTodo();

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

        ////FECHAS PRUEBAS

        Date fin = new Date(2022,1,1);
        Date inicio = new Date(2020,3,12);
        Date intermedio = new Date(2020,7,14);
        Date fechaCompra = new Date(2020,6,22);

        System.out.println(u2.historicoViaje(inicio, fin));

        ////CIUDADES

        Ciudad c1 = new Ciudad(1,"Medellin", "calle X - 95");
        Ciudad c2 = new Ciudad(2,"Bello", "calle Y - 72");
        Ciudad c3 = new Ciudad(7,"Popayan", "calle X - 37");
        Ciudad c4 = new Ciudad(8,"Cali", "calle F - 13");

        System.out.println(c1.getId());
        System.out.println(c2.getId());
        System.out.println(c3.getId());
        System.out.println(c4.getId());


        //////SILLAS
        Silla sp1 = new Silla(1, true , Ubicacion.VENTANA);
        Silla sp2 = new Silla(2, true , Ubicacion.PASILLO);
        Silla se1 = new Silla(7, false , Ubicacion.VENTANA);
        Silla se2 = new Silla(8, false , Ubicacion.PASILLO);
        ArrayList<Silla> sillas = new ArrayList<Silla>();
        sillas.add(sp1);
        sillas.add(sp2);
        sillas.add(se1);
        sillas.add(se2);

        //////VEHICULO
        Vehiculo v1 = new Vehiculo("AAA000", sillas);

        //VIAJES
        Viaje viaje1 = new Viaje(12,300000, 4000, 7000, c2,c4, v1 ,intermedio);

        //TIQUETES

        //////funcionamiento de asignarTiquete
        System.out.println(Asignar.asignarTiquete(u2, viaje1, 4000).getSillaTiquete());
        System.out.println(Asignar.asignarTiquete(u2, viaje1, 5000).getSillaTiquete());
        System.out.println(Asignar.asignarTiquete(u3, viaje1, 10000).getSillaTiquete());

        System.out.println(u2.getHistoricoViajes());


        //////funcionamiento de Comprador.historicoViaje => (DATE, DATE) --- (CIUDAD)
        System.out.println(u2.historicoViaje(inicio, fin));
        System.out.println(u2.historicoViaje(c4));


        //EMPLEADOS
        ////MECANICOS
        Especialista mec1 = new Especialista(27, "Jose", "emailMecanico@example.com", 3224568585L, Especialidad.MECANICO);

        ////CONDUCTORES
        Conductor con1 = new Conductor(28, "Don Javie", "DonJavier@example.com", 3004569696L, Categoria.B3);

        System.out.println(Asignar.asignarViaje(con1, viaje1));
        System.out.println(Asignar.asignarVehiculo(mec1, v1));

        System.out.println(Comprador.getCompradores());
        Serializador.serializarTodo();


        System.out.println(Comprador.getCompradores());

        AdminTiquete.visualizarEstadisticas();
    }
}