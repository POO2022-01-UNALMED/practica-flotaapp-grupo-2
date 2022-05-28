package gestorAplicacion;

import java.io.Serializable;

import java.util.ArrayList;

public class Ciudad implements Serializable {
//public class Ciudad{
	private final int id;
    private String nombre; //
    private String dirTerminal;
    private int numVisitantes;
    private static  ArrayList<Ciudad> ciudades = new ArrayList<>();
    
    /*
     * Desde el constructor se valida para agregar una nueva ciudad que no exista previamente y cuando esto pase no
     * se crea la instancia
     */
    
    public Ciudad(int id, String nombre, String dirTerminal) { 
    	this.id = id;
    	this.setNombre(nombre);
    	this.dirTerminal = dirTerminal;
    	
    	if(ciudades.isEmpty()) {
    		ciudades.add(this);
    	}else {
    		for (Ciudad c: ciudades) {
        		if (c.id == this.id){  // compara el identificador de la ciudad que es la llave
        			break;
        		} else {
        			ciudades.add(this);
        		}
        	}
        }
    }
    	
    public static void quitarCiudad(int idCiudad) {
    	if (!ciudades.isEmpty()){
    		for (Ciudad c: ciudades) {
        		if (c.id == idCiudad) {
        			ciudades.remove(c); 
        		}else {
        			return;
        		}
        	}
    		
    	}else {
    		return;
    	}

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


	public void setNumVisitantes(int numVisitantes) {
		this.numVisitantes = numVisitantes;
	}
	

	public static ArrayList<Ciudad> getCiudades(){return ciudades;	}
	
	/*
	public static boolean getCiudad(Ciudad existente) {
		if(ciudades.contains(existente)) {
			return true;
		}
		else {
			return false;
		}
	}*/

	@Override
	public String toString() {
		return nombre;
	}

}
