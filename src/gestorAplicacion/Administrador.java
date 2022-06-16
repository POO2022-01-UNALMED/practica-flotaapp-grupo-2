package gestorAplicacion;

import java.util.ArrayList;

public class Administrador extends Empleado{
    private static ArrayList<Administrador> administradores = new ArrayList<>();

    public Administrador(int cc, String uNombre, String email, long movil, int sueldo) {
        super(cc, uNombre, email, movil, sueldo);
        Administrador.administradores.add(this);
    }

    // ----- Sobrecargo metodo Despedir - Dependiendo el tipo de Empleado

    public static void despedir(Especialista empleado){
        empleado.agregarSaldo(3000); //Comision de Despido
        Especialista.desvincularEmpleado(empleado);
    }

    public static void despedir(Conductor empleado){
        empleado.agregarSaldo(3000); //Comision de Despido
        Conductor.desvincularEmpleado(empleado);
    }

    public static void despedir(Administrador empleado){
        empleado.agregarSaldo(3000); //Comision de Despido
        Administrador.desvincularEmpleado(empleado);
    }
    
    

    public void renunciar() {
        Administrador.desvincularEmpleado(this);
    }
    
    public static void desvincularEmpleado(Administrador empleado) {
    	Administrador.administradores.remove(empleado);
    }
}