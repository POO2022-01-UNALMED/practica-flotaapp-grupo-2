package gestorAplicacion;

import java.util.ArrayList;

public class Especialista extends Empleado {
	private enum Especialidad {ELECTRICO, MECANICO , SILLETERIA}
	
	private Especialista especialidad;
	private static  ArrayList<String> historialVehiculosRevisados = new ArrayList<String>();
	private static  ArrayList<Especialista> especialistas = new ArrayList<>();
	
	public Especialista(int cc, String uNombre, String email, long movil, Especialista especialidad, ArrayList<String> historialVehiculosRevisados, ArrayList<Especialista> especialistas) {
		super(cc, uNombre, email, movil);
		this.especialidad = especialidad;
		this.historialVehiculosRevisados = historialVehiculosRevisados;
		this.especialistas = especialistas;
	}
	public void registrar() {}
		 
	
	public void modificarInformacion() {} 
	
	//public String revisionVehiculo() {}
	
	public void despedir() {} 
	
	public void renunciar() {} 

}
