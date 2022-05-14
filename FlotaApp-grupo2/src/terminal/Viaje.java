package terminal;
import java.util.Date;
import java.util.ArrayList;

public class Viaje {
	
	private Ciudad origen;
    private int id;
    private static  ArrayList<Ciudad> destino = new ArrayList<>();
    private AdminTiquete tiquete;
    private Date fechaViaje;
    private Vehiculo vehiculo; 
    private boolean escala;
    private boolean disponibilidad;
}
