/*
 * Clase con las funciones e información de la clase abstacta Empelado necesarias para forzar la implementación del método renunciar
 * Estructuras: Clases y métodos abstractos y herencia
 * 
 * @author: Mateo Hechavarria, Juan Pablo Pineda, Miguel Angel Fonseca, Haison Urrutia
 */


package gestorAplicacion;

public abstract class Empleado extends Usuario {

	protected int sueldo;
	
	public Empleado(int cc, String uNombre, String email, long movil, int sueldo) {

		super(cc, uNombre , email, movil);
		this.sueldo = sueldo;
	}
	
	public abstract void renunciar();
	
	public void bonoSueldo() {
		sueldo += sueldo*0.1; //Se brinda un bono del 10% a cada empleado
	}

}
