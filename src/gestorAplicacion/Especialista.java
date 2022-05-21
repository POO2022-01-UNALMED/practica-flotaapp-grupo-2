package gestorAplicacion;

import java.io.Serializable;
import java.util.ArrayList;

public class Especialista extends Empleado implements Serializable {
	private Especialidad especialidad;
	private static  ArrayList<Vehiculo> historialVehiculosRevisados = new ArrayList<Vehiculo>();
	private static  ArrayList<Especialista> especialistas = new ArrayList<>();
	
	public Especialista(int cc, String uNombre, String email, long movil, Especialidad especialidad) {
		super(cc, uNombre, email, movil);
		this.especialidad = especialidad;
		this.historialVehiculosRevisados = new ArrayList<Vehiculo>();
	}
	public void registrar() {}
		 
	
	public void modificarInformacion() {} 
	
	public String revisionVehiculo(Vehiculo vehiculo) {
		String mesage = "El vehiculo " + vehiculo.getPlaca() + " esta en buenas condiciones";
		int random_int = (int)Math.floor(Math.random()*(100000));
		if (random_int == 13){
			mesage = "Al vehiculo " + vehiculo.getPlaca() + " se le necesitan hacer reparaciones";
		}
		return mesage;
	}

	public void anadirVehiculoHistoria(Vehiculo vehiculo) {this.historialVehiculosRevisados.add(vehiculo);}

	public Especialidad getEspecialidad() {return especialidad;	}

	public void despedir() {}
	
	public void renunciar() {} 

}
