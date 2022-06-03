package gestorAplicacion;

import java.io.Serializable;
import java.util.ArrayList;

public class Especialista extends Empleado implements Serializable {
	private Especialidad especialidad;
	private ArrayList<Vehiculo> historialVehiculosRevisados;
	private static  ArrayList<Especialista> especialistas = new ArrayList<>();

	public Especialista(){ super(0, "ESPECIALISTA NO REGISTRADO", "noemail@error.exe", 666, 0); this.especialidad = Especialidad.ADMINISTRADOR;}

	public Especialista(int cc, String uNombre, String email, long movil, int sueldo, Especialidad especialidad) {
		super(cc, uNombre, email, movil, sueldo);
		this.especialidad = especialidad;
		this.historialVehiculosRevisados = new ArrayList<Vehiculo>();
		Especialista.especialistas.add(this);
	}

	public void renunciar() {
		Especialista.desvincularEmpleado(this);
	}
	
	public static void desvincularEmpleado(Especialista empleado) {
    	Especialista.especialistas.remove(empleado);
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
	
	public  String despedir(Especialista empleado){
		System.out.println("ESPECIALISTA: " + empleado.getuNombre() +" DESPEDIDO");
		String mesage = "";
		if (this.especialidad.equals(especialidad.ADMINISTRADOR)) {
			empleado.agregarSaldo(3000); //Comision de Despido
	        Especialista.desvincularEmpleado(empleado);
	        mesage = "Se ha despedido el especialista" + empleado.getuNombre();
		}
		else {
			mesage = "Solo los ADMINISTRADORES pueden despedir empleados";
		}
		return mesage;
        
    }

    public  String despedir(Conductor empleado){
		System.out.println("CONDUCTOR: " + empleado.getuNombre() +" DESPEDIDO");
    	String mesage = "";
    	if (this.especialidad.equals(especialidad.ADMINISTRADOR)) {
			for(Viaje viaje : empleado.getHistoriaViajesRealizados()){
				viaje.setConductor(null);
			}
			empleado.agregarSaldo(3000); //comision por despido
	        Conductor.desvincularEmpleado(empleado);
	        mesage = "Se ha despedido el especialista" + empleado.getuNombre();
		}
		else {
			mesage = "Solo los ADMINISTRADORES pueden despedir empleados";
		}
    	return mesage;
    }


	// ----- G E T   A N D   S E T -----

	public void anadirVehiculoHistoria(Vehiculo vehiculo) {this.historialVehiculosRevisados.add(vehiculo);}

	public Especialidad getEspecialidad() {return especialidad;	}

	public ArrayList<Vehiculo> getHistorialVehiculosRevisados() {	return historialVehiculosRevisados;	}

	public static ArrayList<Especialista> getEspecialistas() {	return especialistas;}
}
