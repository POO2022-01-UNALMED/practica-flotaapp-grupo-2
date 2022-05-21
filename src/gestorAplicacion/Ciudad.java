package gestorAplicacion;

import java.io.Serializable;
import java.util.ArrayList;

public class Ciudad implements Serializable {
	private int id;
	private String nombre; //
	private String dirTerminal;
	private int numVisitantes;
	private static  ArrayList<Ciudad> ciudades = new ArrayList<>();
	static {
		ciudades = new ArrayList<Ciudad>();
	}

	public Ciudad(int id, String nombre, String dirTerminal) {
		this.id = id;
		this.nombre = nombre;
		this.dirTerminal = dirTerminal;
		this.numVisitantes = 0;
		ciudades.add(this);
	}

	public static void quitarCiudad(String ciudad) {
		if (!ciudades.isEmpty()){
			for (Ciudad c: ciudades) {
				if (c.nombre.equals(ciudad)) {
					ciudades.remove(c); //por que me saca error al intentar eliminar
				}
			}
		}else {
			return;
		}

	}
	//historico de viajes


	public void anadirVisitantes(int numVisitantes) {
		this.numVisitantes += numVisitantes;
	}

	public void eliminarVisitantes(int numVisitantes) {
		this.numVisitantes -= numVisitantes;
	}

	public static ArrayList<Ciudad> getCiudades() { return ciudades; }
}