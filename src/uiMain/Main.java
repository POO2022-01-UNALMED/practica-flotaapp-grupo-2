package uiMain;

import gestorAplicacion.*;

import baseDatos.*;
import uiMain.funcionalidades.*;

import java.util.ArrayList;
import java.time.LocalDate;
import java.util.Scanner;


public class Main {
    private static boolean running = true;
    private static int election = -1;

    public static void main(String[] args) {
        //Deserializador.deserializarTodo();
        // COMPRADORES

        Comprador u1 = new Comprador(1, "Mateo", "example@email.com", 3234567890L);
        Comprador u2 = new Comprador(2, "Marcos", "example2@email.com", 3087654321L);
        Comprador u3 = new Comprador(3, "Lucas", "example3@email.com", 3088890321L);
        Comprador u4 = new Comprador(4, "Juan", "example4@email.com", 3087656654L);
        Comprador u5 = new Comprador(5, "Estrella", "example5@email.com", 3087756654L);

        ////FECHAS PRUEBAS

        LocalDate fin = LocalDate.now().plusDays(15);
        LocalDate inicio = LocalDate.now().plusDays(2);
        LocalDate intermedio = LocalDate.now().plusDays(12);

        ////CIUDADES

        Ciudad Medellin = new Ciudad(1, "MEDELLIN", "calle X - 95");
        Ciudad Bello = new Ciudad(12, "BELLO", "calle Y - 72");
        Ciudad Popayan = new Ciudad(7, "POPAYAN", "calle X - 37");
        Ciudad Cali = new Ciudad(8, "CALI", "calle F - 13");
        Ciudad Monteria = new Ciudad(5, "MONTERIA", "circular 4 # 1 - 44");
        Ciudad Cartagena = new Ciudad(4, "CARTAGENA", "calle G - 14");
        Ciudad Pasto = new Ciudad(6, "PASTO", "Carrera 24 # 4 - 22");
        Ciudad Barranquilla = new Ciudad(9, "BARRANQUILLA", "calle siempre viva # 123");
        Ciudad Manizales = new Ciudad(3, "MANIZALES", "avenida 24 # 3-23");

        //////SILLAS
        Silla se1v1 = new Silla(7, false, Ubicacion.VENTANA);
        Silla se2v1 = new Silla(8, false, Ubicacion.PASILLO);
        Silla sp1v1 = new Silla(1, true, Ubicacion.VENTANA);
        Silla sp2v1 = new Silla(2, true, Ubicacion.PASILLO);
        Silla sp3v1 = new Silla(3, true, Ubicacion.VENTANA);
        Silla sp4v1 = new Silla(4, true, Ubicacion.PASILLO);
        Silla sp5v1 = new Silla(5, true, Ubicacion.VENTANA);
        Silla sp6v1 = new Silla(6, true, Ubicacion.PASILLO);
        ArrayList<Silla> sillasv1 = new ArrayList<Silla>();
        sillasv1.add(se1v1);
        sillasv1.add(se2v1);
        sillasv1.add(sp1v1);
        sillasv1.add(sp2v1);
        sillasv1.add(sp3v1);
        sillasv1.add(sp4v1);
        sillasv1.add(sp5v1);
        sillasv1.add(sp6v1);

        Silla se1v2 = new Silla(3, false, Ubicacion.VENTANA);
        Silla se2v2 = new Silla(4, false, Ubicacion.PASILLO);
        Silla sp1v2 = new Silla(1, true, Ubicacion.VENTANA);
        Silla sp2v2 = new Silla(2, true, Ubicacion.PASILLO);
        ArrayList<Silla> sillasv2 = new ArrayList<Silla>();
        sillasv2.add(se1v2);
        sillasv2.add(se2v2);
        sillasv2.add(sp1v2);
        sillasv2.add(sp2v2);


        Silla se1v3 = new Silla(3, false, Ubicacion.VENTANA);
        Silla se2v3 = new Silla(4, false, Ubicacion.PASILLO);
        Silla sp1v3 = new Silla(1, true, Ubicacion.VENTANA);
        Silla sp2v3 = new Silla(2, true, Ubicacion.PASILLO);
        ArrayList<Silla> sillasv3 = new ArrayList<Silla>();
        sillasv3.add(se1v3);
        sillasv3.add(se2v3);
        sillasv3.add(sp1v3);
        sillasv3.add(sp2v3);


        //////VEHICULO
        Vehiculo v1 = new Vehiculo("AAA000", sillasv1);
        Vehiculo v2 = new Vehiculo("ZZZ999", sillasv2);
        Vehiculo v3 = new Vehiculo("ABC123", sillasv3);

        //VIAJES
        Viaje viaje2 = new Viaje(4, 400000, 3000, 5000, Monteria, Pasto, 7, v2, intermedio);
        Viaje viaje3 = new Viaje(3, 350000, 5000, 7500, Medellin, Manizales, 7, v3, fin);
        Viaje viaje1 = new Viaje(1, 300000, 7000, 9000, Bello, Cali, 7, v1, intermedio);
        Viaje viaje4 = new Viaje(2, 300000, 3000, 7000, Medellin, Cartagena, 7, v1, fin);

        // PROMOCIONES
        Recomendacion.promociones.put(Pasto, 25);
        Recomendacion.promociones.put(Cali, 10);
        Recomendacion.promociones.put(Bello, 15);
        Recomendacion.promociones.put(Medellin, 20);
        Recomendacion.promociones.put(Manizales, 35);


        //EMPLEADOS
        Especialista mec1 = new Especialista(27, "Jose", "emailMecanico1@example.com", 3224568585L, 3500, Especialidad.MECANICO);
        Especialista ele1 = new Especialista(78, "Maria", "emailElectrico1@example.com", 3224567585L, 4000, Especialidad.ELECTRICO);
        Especialista ele2 = new Especialista(88, "Maria", "emailElectrico2@example.com", 3228867585L, 4000, Especialidad.ELECTRICO);
        Especialista ele3 = new Especialista(98, "Maria", "emailElectrico3@example.com", 3229967585L, 4000, Especialidad.ELECTRICO);
        Especialista mec3 = new Especialista(32, "Pablo", "emailMecanico3@example.com", 3224538585L, 3700, Especialidad.MECANICO);
        Especialista si1 = new Especialista(12, "Edgar", "emailSillas1@example.com", 3224588485L, 3000, Especialidad.SILLETERIA);
        Especialista si2 = new Especialista(102, "Edgar", "emailSillas2@example.com", 3224599485L, 3000, Especialidad.SILLETERIA);
        Especialista si3 = new Especialista(120, "Edgar", "emailSillas3@example.com", 3224500485L, 3000, Especialidad.SILLETERIA);

        ////CONDUCTORES
        Conductor con1 = new Conductor(28, "Don Javie", "DonJavier@example.com", 3004569696L, 4000, Categoria.B3);
        Conductor con2 = new Conductor(29, "Don Hernan", "DonHernan@example.com", 3007569696L, 4100, Categoria.C1);
        Conductor con3 = new Conductor(30, "Dona Marta", "DonaMarta@example.com", 3004589696L, 4200, Categoria.C2);


        //System.out.println(u2.historicoViaje(inicio, fin));



        //////funcionamiento de comprarTiquete
        u1.comprarTiquete(Bello, Cali, 8000);
        u2.comprarTiquete(Monteria, Pasto, 5000);
        u4.comprarTiquete(Monteria, Pasto, 9000);
        u3.comprarTiquete(Bello, Cali, 9000);
        u3.comprarTiquete(Monteria, Pasto, 10000);
        u5.comprarTiquete(Medellin, Cartagena, 10000);


        //////funcionalidad Asignar Viaje
        Asignar.asignarVehiculo(con1, viaje1);
        Asignar.asignarVehiculo(con2, viaje3);

        Asignar.asignarVehiculo(mec1, v1);
        Asignar.asignarVehiculo(ele1, v1);

        //System.out.println(Ciudad.getCiudades());


        Scanner in = new Scanner(System.in);
        showLogo();
        System.out.println("\n".repeat(2));

        while(running) {
            showMenu();
            while(election < 0 || election > 7) {
                try {
                    election = in.nextInt();
                    if (election < 0 || election > 7) {
                        System.out.println("Opcion invalida..., probemos otra vez");
                        System.out.println("Recuerda, elije una de las opciones [1] [2] [3] [4] [5] [6]");
                    }
                } catch (Exception InputMismatchException) {
                    // TODO: handle exception
                    System.out.println("No te entiendo..., probemos otra vez");
                    System.out.println("Recuerda, elije una de las opciones [1] [2] [3] [4] [5] [6]");
                }
            }
            System.out.println("");
            executeFunctionality(election, in);
            election = -1;
        }
        in.close();

    }

    public static void showLogo() {
        System.out.println(
                  "                                 ______      __            ______        _________    ________                    ________        ______      ______     \n"
                + "                          __    /_____/\\    /_/\\          /_____/\\      /________/\\  /_______/\\                 /_______/\\      /_____/\\    /_____/\\    \n"
                + " .-----------------------'  |   \\::::_\\/_   \\:\\ \\         \\:::_ \\ \\     \\__.::.__\\/  \\::: _  \\ \\      _______   \\::: _  \\ \\     \\:::_ \\ \\   \\:::_ \\ \\   \n"
                + "/| _ .---. .---. .---. .---.|    \\:\\/___/\\   \\:\\ \\         \\:\\ \\ \\ \\       \\::\\ \\     \\::(_)  \\ \\    /______/\\   \\::(_)  \\ \\     \\:(_) \\ \\   \\:(_) \\ \\  \n"
                + "|j||||___| |___| |___| |___||     \\:::._\\/    \\:\\ \\____     \\:\\ \\ \\ \\       \\::\\ \\     \\:: __  \\ \\   \\__::::\\/    \\:: __  \\ \\     \\: ___\\/    \\: ___\\/  \n"
                + "|=|||=======================|      \\:\\ \\       \\:\\/___/\\     \\:\\_\\ \\ \\       \\::\\ \\     \\:.\\ \\  \\ \\                \\:.\\ \\  \\ \\     \\ \\ \\       \\ \\ \\    \n"
                + "[_|j||(O)\\__________|(O)\\___]       \\_\\/        \\_____\\/      \\_____\\/        \\__\\/      \\__\\/\\__\\/                 \\__\\/\\__\\/      \\_\\/        \\_\\/    ");


    }

    public static void showMenu() {
        System.out.println(" ");
        System.out.println("----- M E N U -----");

        System.out.println("[1] Visualizar Estadisticas");
        System.out.println("[2] Gestionar Conductores");
        System.out.println("[3] Gestionar Especialistas");
        System.out.println("[4] Gestionar Viaje - (cc) ");
        System.out.println("[5] Compra de Tiquete");
        System.out.println("[6] Recomendacion");
        System.out.println("[7] Salir\n");

    }

    public static void executeFunctionality(int election, Scanner in) {
        switch (election) {
            case 1:
                AdminViaje.visualizarEstadisticas();
                break;
            case 2:
                System.out.println("GESTIONAR CONDUCTORES");
                Gestionar.gestionarConductores();
                break;
            case 3:
                Gestionar.gestionarEspecialistas();
                break;
            case 4:
                System.out.println("Gestionar Viaje - CC: ");
                Scanner ccGV = new Scanner(System.in);
                int ccCG = ccGV.nextInt();
                Gestionar.gestionarViajes(ccCG);
                break;
            case 5:
                AdminViaje.comprarTiqueteTerminal();
                break;
            case 6:
                System.out.println("Recomendar Viaje - CC: ");
                Scanner aux1 = new Scanner(System.in);
                int cc1 = aux1.nextInt();
                System.out.println(Recomendacion.recomendarViaje(cc1));
                break;
            case 7:
                running = false;
                break;
        }
    }
}