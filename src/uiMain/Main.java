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
        Deserializador.deserializarTodo();
        // COMPRADORES

        Comprador u1 = new Comprador(1, "Usuario1", "example@email.com", 3234567890L);
        Comprador u2 = new Comprador(2, "Usuario2", "example2@email.com", 3087654321L);
        Comprador u3 = new Comprador(3, "Usuario3", "example3@email.com", 3088890321L);
        Comprador u4 = new Comprador(4, "Usuario4", "example4@email.com", 3087656654L);

        ////FECHAS PRUEBAS

        LocalDate fin = LocalDate.now().plusDays(15);
        LocalDate inicio = LocalDate.now();
        LocalDate intermedio = LocalDate.now().plusDays(12);

        ////CIUDADES

        Ciudad Medellin = new Ciudad(1, "Medellin", "calle X - 95");
        Ciudad Bello = new Ciudad(12, "Bello", "calle Y - 72");
        Ciudad Popayan = new Ciudad(7, "Popayan", "calle X - 37");
        Ciudad Cali = new Ciudad(8, "Cali", "calle F - 13");
        Ciudad Monteria = new Ciudad(5, "Monter�a", "circular 4 # 1 - 44");
        Ciudad Cartagena = new Ciudad(4, "Cartagena", "calle G - 14");
        Ciudad Pasto = new Ciudad(6, "Pasto", "Carrera 24 # 4 - 22");
        Ciudad Barranquilla = new Ciudad(9, "Barranquilla", "calle siempre viva # 123");
        Ciudad Manizales = new Ciudad(3, "Manizales", "avenida 24 # 3-23");

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


        //////VEHICULO
        Vehiculo v1 = new Vehiculo("AAA000", sillasv1);
        Vehiculo v2 = new Vehiculo("ZZZ999", sillasv2);

        //VIAJES
        Viaje viaje1 = new Viaje(1, 300000, 7000, 9000, Bello, Cali, 7, v1, intermedio);
        Viaje viaje2 = new Viaje(4, 400000, 3000, 5000, Monteria, Pasto, 7, v2, intermedio);


        // PROMOCIONES
        Recomendacion.promociones.put(Cali, 10);
        Recomendacion.promociones.put(Bello, 15);
        Recomendacion.promociones.put(Popayan, 5);
        Recomendacion.promociones.put(Medellin, 20);
        Recomendacion.promociones.put(Cartagena, 25);


        //EMPLEADOS
        Especialista mec1 = new Especialista(27, "Jose", "emailMecanico1@example.com", 3224568585L, 3000, Especialidad.MECANICO);
        Especialista ele1 = new Especialista(28, "Maria", "emailMecanico2@example.com", 3224567585L, 4000, Especialidad.ELECTRICO);
        Especialista mec3 = new Especialista(28, "Pablo", "emailMecanico3@example.com", 3224538585L, 3700, Especialidad.MECANICO);

        ////CONDUCTORES
        Conductor con1 = new Conductor(28, "Don Javie", "DonJavier@example.com", 3004569696L, 4000, Categoria.B3);
        Conductor con2 = new Conductor(29, "Don Hernan", "DonHernan@example.com", 3007569696L, 4100, Categoria.C1);
        Conductor con3 = new Conductor(30, "Dona Marta", "DonaMarta@example.com", 3004589696L, 4200, Categoria.C2);


        //System.out.println(u2.historicoViaje(inicio, fin));

        //////funcionamiento de comprarTiquete
        u1.comprarTiquete(Bello, Cali, 8000);
        u2.comprarTiquete(Monteria, Pasto, 5000);
        u3.comprarTiquete(Bello, Cali, 10000);


        //////funcionalidad Asignar Viaje
        Asignar.asignarViaje(con1, viaje1);
        Asignar.asignarViaje(con2, viaje2);

        Asignar.asignarVehiculo(mec1, v1);
        Asignar.asignarVehiculo(ele1, v1);

        System.out.println(Ciudad.getCiudades());


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
                Scanner aux = new Scanner(System.in);
                int cc = aux.nextInt();
                Gestionar.gestionarViajes(cc);
                break;
            case 5:
                Comprador compradorBase = new Comprador(0, "FLOTAAPPCOMPRADOR", "FLOTA@app.com", 999);
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