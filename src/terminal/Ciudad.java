package terminal;

import java.util.ArrayList;

public class Ciudad {
    private int id;
    private String nombre; //
    private String dirTerminal;
    private int numVisitantes;
    private static  ArrayList<Ciudad> ciudades = new ArrayList<>();
    
    
    public Ciudad(int id, String nombre, String dirTerminal) { 
    	this.id = id;
    	this.nombre = nombre;
    	this.numVisitantes = numVisitantes;
    	ciudades.add(this); 
    }
    
    public static void quitarCiudad(String ciudad) {
    	if (!ciudades.isEmpty()){
    		for (Ciudad c: ciudades) {
        		if (c.nombre.equals(ciudad)) {
        			ciudades.remove(c); 
        		}
        	}
    	}else {
    		return;
    	}

    }
    //historico de viajes 
    
    
}
