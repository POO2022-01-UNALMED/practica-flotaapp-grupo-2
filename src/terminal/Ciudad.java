package terminal;

import java.util.ArrayList;
import java.io.Serializable;
import java.util.Date;

//public class Ciudad implements Serializable {
public class Ciudad {
    private int id;
    private String nombre; //
    private String dirTerminal;
    private int numVisitantes;
    private static  ArrayList<Ciudad> ciudades = new ArrayList<>();
    
    
    public Ciudad(int id, String nombre, String dirTerminal) { 
    	this.id = id;
    	this.nombre = nombre;
    	this.setDirTerminal(dirTerminal);
    	ciudades.add(this); 
    }
    
    public static void quitarCiudad(String ciudad) {
    	if (!ciudades.isEmpty()){
    		for (Ciudad c: ciudades) {
        		if (c.nombre.equals(ciudad)) {
        			ciudades.remove(c); //No corre en una clase afuera, analizar método
        		}
        	}
    		
    	}else {
    		return;
    	}

    }
    
    
    public static void agregarCiudad(Ciudad nuevaCiudad) {
    	
    	if(ciudades.isEmpty()) {
    		ciudades.add(nuevaCiudad);
    		return;
    	}
    	for (Ciudad c: ciudades) {
    		if (ciudades.contains(nuevaCiudad)){
    			return;
    		} else {
    			ciudades.add(nuevaCiudad);
    			return;
    		}
    	}
    }
    
    // hV es la cidad con su respectivo historico de viajes
    //Lo mejor sería implementar un toString para retornar toda la ciudad y es mejor que sea un método de clase?
    public static String historicoViajes(String nomCiudad) {
    	String hV = "";
    	
    	if (!ciudades.isEmpty()) {
    		for(Ciudad c: ciudades) {
    			if (c.nombre.equals(nomCiudad)) {
    				hV = "La ciudad " + c.nombre + "a tenido " + c.numVisitantes; //Numero de visitantes es de tipo String mirar que compile
    			}else {
    				hV = "La ciudad " +  nomCiudad + " no existe dentro de nuestra base de datos";
    			}
    		}
    		
    	}else {
    		hV = "La ciudad " + nomCiudad + "no existe";	
    	}
		return hV;
    } 
    
    public String historicoViajes() {  // Método sobrecargado para llamarse desde una instancia
    	
    	String hV = "";
    	if (!ciudades.isEmpty()) {
    		for(Ciudad c: ciudades) {
    			if (c.nombre.equals(this.nombre)) {
    				hV = "La ciudad " + c.nombre + "a tenido " + c.numVisitantes;
    			}else {
    				hV = "La ciudad " +  this.nombre + " no existe dentro de nuestra base de datos";
    			}
    		}
    		
    	}else {
    		hV = "La ciudad " + this.nombre + "no existe";	
    	}
		return hV;
    }
    

	public String getDirTerminal() {
		return dirTerminal;
	}

	public void setDirTerminal(String dirTerminal) {
		this.dirTerminal = dirTerminal;
	}  
	
	public  boolean ciudadExiste() { 
		if(ciudades.contains(this)) {
			return true;
		}else {
			return false;
		}
	}
	
	
	public static ArrayList<Ciudad> getCiudad(){
		return ciudades;
	}
	
	/*
	public static boolean getCiudad(Ciudad existente) {
		if(ciudades.contains(existente)) {
			return true;
		}
		else {
			return false;
		}
	}*/
}
