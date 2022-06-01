package gestorAplicacion;

import java.io.Serializable;
import java.util.ArrayList;
import java.util.Scanner;

public class Conductor extends Empleado implements Serializable {

    private Categoria categoria;
    private ArrayList<Viaje> historiaViajesRealizados;
    private static ArrayList<Conductor> conductores = new ArrayList<>();
    

    public Conductor(int cc, String uNombre, String email, long movil,int salario, Categoria categoria) {

        super(cc, uNombre, email, movil, salario);
        this.categoria = categoria;
        this.historiaViajesRealizados = new ArrayList<Viaje>();
        Conductor.conductores.add(this);
    }

    public void anadirViajeHistoria(Viaje viaje) {this.historiaViajesRealizados.add(viaje);}

    // ----- M E T O D O S -----

    public Conductor modificarCategoria(Categoria categoria) {
        System.out.println("[1] B3 , [2] C1 , [3] C2, [4]");
        Scanner aux = new Scanner(System.in);
        int categoriaModificada = aux.nextInt();
        switch (categoriaModificada){
            case 1:
                this.setCategoria(Categoria.B3);
            case 2:
                this.setCategoria(Categoria.C1);
            case 3:
                this.setCategoria(Categoria.C2);
            case 4:
                this.setCategoria(Categoria.C3);
        }
        return this;
    }

    //bonoSueldo() : void
    @Override
    public void bonoSueldo() {
    	sueldo += sueldo*0.15; //bono del 15% por ligadura dinámica
    	Conductor superConductor = null;
    	for (Conductor cadaConductor: Conductor.conductores) {
    		if (superConductor.equals(cadaConductor)) {
    			superConductor = cadaConductor;
    		}
    		else if (cadaConductor.historiaViajesRealizados.size() > superConductor.historiaViajesRealizados.size()) {
    			superConductor = cadaConductor;
    		}else {
    			continue;
    		}
    		if (superConductor.equals(null)) {
    			return;
    		}else {
    			this.sueldo += sueldo*0.15; //bono del 15% al mejor conductor
    		}
    	}
    }

    public void renunciar() {
        Conductor.desvincularEmpleado(this);
    }
    
    public static void desvincularEmpleado(Conductor empleado) {
    	Conductor.conductores.remove(empleado);
    }

    // ----- G E T   A N D   S E T -----

    public void setCategoria(Categoria categoria) {
        this.categoria = categoria;
    }

    public static ArrayList<Conductor> getConductores() {      return conductores;   }

    public ArrayList<Viaje> getHistoriaViajesRealizados() {
        return historiaViajesRealizados;
    }
}