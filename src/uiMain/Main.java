package uiMain;

import gestorAplicacion.*;

import baseDatos.*;
import uiMain.funcionalidades.*;

import java.util.ArrayList;
import java.time.LocalDate;


public class Main {
    public static void main(String[] args) {
        Deserializador.deserializarTodo();

        // COMPRADORES
        Comprador u1 = new Comprador(1, "Usuario1", "example@email.com", 3234567890L);
        Comprador u2 = new Comprador(2, "Usuario2", "example2@email.com", 3087654321L);
        Comprador u3 = new Comprador(3, "Usuario3", "example3@email.com", 3088890321L);
        Comprador  u4 = new Comprador(4, "Usuario4", "example4@email.com", 3087656654L);

        ////FECHAS PRUEBAS

        LocalDate fin = LocalDate.now().plusDays(15);
        LocalDate inicio = LocalDate.now();
        LocalDate intermedio = LocalDate.now().plusDays(12);

        ////CIUDADES

        Ciudad Medellin = new Ciudad(1, "Medellin", "calle X - 95");
        Ciudad Bello = new Ciudad(12, "Bello", "calle Y - 72");
        Ciudad Popayan = new Ciudad(7, "Popayan", "calle X - 37");
        Ciudad Cali = new Ciudad(8, "Cali", "calle F - 13");
        Ciudad Monteria = new Ciudad(5, "Montería", "circular 4 # 1 - 44");
        Ciudad Cartagena = new Ciudad(4, "Cartagena", "calle G - 14");
        Ciudad Pasto = new Ciudad(6, "Pasto", "Carrera 24 # 4 - 22");
        Ciudad Barranquilla = new Ciudad(9, "Barranquilla", "calle siempre viva # 123");
        Ciudad Manizales = new Ciudad(3, "Manizales", "avenida 24 # 3-23");

        //////SILLAS
        Silla se1 = new Silla(7, false, Ubicacion.VENTANA);
        Silla se2 = new Silla(8, false, Ubicacion.PASILLO);
        Silla sp1 = new Silla(1, true, Ubicacion.VENTANA);
        Silla sp2 = new Silla(2, true, Ubicacion.PASILLO);
        ArrayList<Silla> sillas = new ArrayList<Silla>();
        sillas.add(se1);
        sillas.add(se2);
        sillas.add(sp1);
        sillas.add(sp2);


        //////VEHICULO
        Vehiculo v1 = new Vehiculo("AAA000", sillas);

        //VIAJES
        Viaje viaje1 = new Viaje(12, 300000, 4000, 7000, Bello, Cali, 7, v1, intermedio);


        //EMPLEADOS
        
        // PROMOCIONES
        Recomendacion.promociones.put(Cali, 10);
        Recomendacion.promociones.put(Bello, 15);
        Recomendacion.promociones.put(Popayan, 5);
        Recomendacion.promociones.put(Medellin, 20);
        Recomendacion.promociones.put(Cartagena, 25);
        
        

        ////MECANICOS
        Especialista mec1 = new Especialista(27, "Jose", "emailMecanico1@example.com", 3224568585L, 3000, Especialidad.MECANICO);
        Especialista mec2 = new Especialista(28, "Maria", "emailMecanico2@example.com", 3224567585L, 4000, Especialidad.ELECTRICO);
        Especialista mec3 = new Especialista(28, "Pablo", "emailMecanico3@example.com", 3224538585L, 3700, Especialidad.MECANICO);

        ////CONDUCTORES
        Conductor con1 = new Conductor(28, "Don Javie", "DonJavier@example.com", 3004569696L, 4000, Categoria.B3);

        //PRUEBAS


        u2.modificarNombre("Usuario2Modificado");
        u3.modificarEmail("emailModificado@example.com");
        u4.modificarMovil(3333333333L);

        //System.out.println(u2.historicoViaje(inicio, fin));

        //////funcionamiento de comprarTiquete
        //System.out.println("u1: compra el tiquete: " + u1.comprarTiquete(c2, c4, 4000));
        //System.out.println("u3: compra el tiquete: " + u2.comprarTiquete(c2, c4, 5000));
        System.out.println("u3: compra el tiquete: " + u3.comprarTiquete(c2, c4, 10000));

        //////funcionamiento de Comprador.historicoViaje => (DATE, DATE) --- (CIUDAD)
        //System.out.println(u3.historicoViaje(inicio, fin));
        //System.out.println(u1.historicoViaje(c4));

        Asignar.asignarViaje(con1, viaje1);
        Asignar.asignarVehiculo(mec1, v1);

        //System.out.println(Comprador.getCompradores());

        //Serializador.serializarTodo();
        Gestionar.gestionarViajes(3);
        AdminViaje.visualizarEstadisticas();
        Gestionar.gestionarEspecialistas();


    }
}