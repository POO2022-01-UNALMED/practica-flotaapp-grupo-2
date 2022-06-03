package baseDatos;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectOutputStream;
import java.util.HashMap;
import java.util.List;

import gestorAplicacion.*;
import uiMain.funcionalidades.Recomendacion;

/**
 * Se utiliza para serializar todos los objetos creados durante la ejecucion
 * del proyecto
 * @author Erik Gonzalez
 * @author Felipe Miranda
 */
public class Serializador {
    /**
     * Serializamos una lista por el nombre de la clase
     *
     * @param <E>       el generico se usa para poder agredar las clases que se
     *                  crearon
     * @param lista     Una lista de objetos
     * @param className El nombre de la clase que queremos usar como nombre del
     *                  archivo
     */
    public static <E> void serializar(List<E> lista, String className) {
        FileOutputStream fileOut;

        try {
            String path = System.getProperty("user.dir") + "/src/baseDatos/temp/" + className + ".txt";
            // se crea un fileoutputstream para saber donde serializar los archivos
            fileOut = new FileOutputStream(path);
            // Se crea un objeto output stream para poder escribir en el archivo
            ObjectOutputStream out = new ObjectOutputStream(fileOut);
            // Guardamos la lista de objetos
            out.writeObject(lista);
            out.close();
            fileOut.close();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
    }

    public static <E, V> void serializar(HashMap<E, Integer> dicc, String className) {
        FileOutputStream fileOut;

        try {
            String path = System.getProperty("user.dir") + "/src/baseDatos/temp/" + className + ".txt";
            // Se crea un fileoutputstream para saber donde serializar los archivos
            fileOut = new FileOutputStream(path);
            // Se crea un objeto output stream para poder escribir en el archivo
            ObjectOutputStream out = new ObjectOutputStream(fileOut);
            // Guardamos la lista de objetos
            out.writeObject(dicc);
            out.close();
            fileOut.close();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
    }

    /**
     * Serializamos todas las clases que necesitamos
     */
    public static void serializarTodo() {

        Serializador.serializar(Comprador.getCompradores(), "compradores");
        Serializador.serializar(Ciudad.getCiudades(), "ciudades");
        Serializador.serializar(Viaje.getViajes(), "viajes");
        Serializador.serializar(Especialista.getEspecialistas(), "especilistas");
        Serializador.serializar(Conductor.getConductores(), "conductores");
        Serializador.serializar(Vehiculo.getVehiculos(), "vehiculos");
        Serializador.serializar(Tiquete.getTiquetes(), "tiquetes");
        Serializador.serializar(Silla.getSillas(), "sillas");
        Serializador.serializar(Recomendacion.getPromociones(), "promociones");
    }
}