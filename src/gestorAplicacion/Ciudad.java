/*
 * Clase con las funciones de Ciudad necesarias para hacer CRUD en ciudades
 * Estructuras: ArrayList y sus funciones
 * 
 * @author: Mateo Hechavarria, Juan Pablo Pineda, Miguel Angel Fonseca, Haison Urrutia
 */




package gestorAplicacion;

import java.io.Serializable;

import java.util.ArrayList;

public class Ciudad implements Serializable {
	private int id;
    private String nombre; 
    private String dirTerminal;
    private int numVisitantes;
    private static  ArrayList<Ciudad> ciudades;
	static {
		ciudades = new ArrayList<Ciudad>();
	}
    
    /*
     * Desde el constructor se valida para agregar una nueva ciudad que no exista previamente y cuando esto pase no
     * se crea la instancia
     */
	public Ciudad(){}

    public Ciudad(int id, String nombre, String dirTerminal) { 
    	this.id = id;
    	this.nombre = nombre;
    	this.setDirTerminal(dirTerminal);
    	ciudades.add(this); 
    }
    
    public static void quitarCiudad(String ciudad) {
    	if (!ciudades.isEmpty()) {
			for (Ciudad c : ciudades) {
				if (c.nombre.equals(ciudad)) {
					ciudades.remove(c); //No corre en una clase afuera, analizar m�todo
				}
			}
		}
	}

    // hV es la cidad con su respectivo historico de viajes
    //Lo mejor ser�a implementar un toString para retornar toda la ciudad y es mejor que sea un m�todo de clase?
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
    
    public String historicoViajes() {  
    	
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

	public void setId(int id) {	this.id = id;}

	public void anadirVisitantes(int numVisitantes) {
		this.numVisitantes += numVisitantes;
	}

	public int getId() {
		return id;
	}


	public String getNombre() {
		return nombre;
	}


	public void setNombre(String nombre) {
		this.nombre = nombre;
	}


	public int getNumVisitantes() {
		return numVisitantes;
	}

	public static ArrayList<Ciudad> getCiudades(){ return ciudades;	}

	@Override
	public String toString() {
		return "Ciudad: "+nombre +
				" id: "+ id +
				" - Direccion Terminal: "+dirTerminal;
				
				
	}
}
