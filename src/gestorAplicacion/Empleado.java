/*
 * Clase con las funciones e informaci�n de la clase abstacta Empelado necesarias para forzar la implementaci�n del m�todo renunciar
 * Estructuras: Clases y m�todos abstractos y herencia
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
