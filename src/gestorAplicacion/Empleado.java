
package gestorAplicacion;

public abstract class Empleado extends Usuario {

	protected int sueldo;
	
	public Empleado(int cc, String uNombre, String email, long movil, int sueldo) {

		super(cc, uNombre , email, movil);
		this.sueldo = sueldo;
	}
	
	public abstract void renunciar();

}
