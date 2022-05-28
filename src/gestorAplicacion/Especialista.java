package gestorAplicacion;

import java.io.Serializable;
import java.util.ArrayList;

public class Especialista extends Empleado implements Serializable {
	private Especialidad especialidad;
	private static  ArrayList<Vehiculo> historialVehiculosRevisados = new ArrayList<Vehiculo>();
	private static  ArrayList<Especialista> especialistas = new ArrayList<>();
	static {
		especialistas = new ArrayList<Especialista>();
	}
	
	public Especialista(int cc, String uNombre, String email, long movil, int sueldo, Especialidad especialidad) {
		super(cc, uNombre, email, movil, sueldo);
		this.especialidad = especialidad;
		this.historialVehiculosRevisados = new ArrayList<Vehiculo>();
		Especialista.especialistas.add(this);
	}

	public void renunciar() {
		Especialista.especialistas.remove(this);
	}

	// ----- M E T O D O S -----

	public String revisionVehiculo(Vehiculo vehiculo) {
		String mesage = "El vehiculo " + vehiculo.getPlaca() + " esta en buenas condiciones";
		int random_int = (int)Math.floor(Math.random()*(100000));
		if (random_int == 13){
			mesage = "Al vehiculo " + vehiculo.getPlaca() + " se le necesitan hacer reparaciones";
		}
		return mesage;
	}

	// ----- G E T   A N D   S E T -----

	public void anadirVehiculoHistoria(Vehiculo vehiculo) {this.historialVehiculosRevisados.add(vehiculo);}

	public Especialidad getEspecialidad() {return especialidad;	}

}
