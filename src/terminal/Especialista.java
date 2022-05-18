package terminal;

import java.util.ArrayList;

public class Especialista extends Empleado {
	private enum Especialidad {ELECTRICO, MECANICO , SILLETERIA}
	
	private Especialista especialidad;
	private static  ArrayList<Revision> historialVehiculosRevisados = new ArrayList<>();
	private static  ArrayList<Especialista> especialistas = new ArrayList<>();
	
	public Especialista(Especialista especialidad, ArrayList<Revision> historialVehiculosRevisados, ArrayList<Especialista> especialistas) {
		this.especialidad = especialidad;
		this.historialVehiculosRevisados = historialVehiculosRevisados;
		this.especialistas = especialistas;
	}
	public void registrar() {}
		 
	
	public void modificarInformacion() {} 
	
	public String revisionVehiculo(Vehiculo) {} 
	
	public void despedir() {} 
	
	public void renunciar() {} 

}
