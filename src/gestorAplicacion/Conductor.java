package gestorAplicacion;

import java.io.Serializable;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class Conductor extends Empleado implements Serializable {

    private Categoria categoria;
    private ArrayList<Viaje> historiaViajesRealizados;
    private static ArrayList<Conductor> conductores = new ArrayList<>();
    static {
        conductores = new ArrayList<Conductor>();
    }

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

    public static void  bonoSueldo() {
    	ArrayList<Integer> listaDeViajes = new ArrayList<>();
    	for(Conductor allConductores: Conductor.getConductores()) {
    		listaDeViajes.add( allConductores.historiaViajesRealizados.size() );
    		//Agrega el numero de viajes de cada conductor
    	}
    	int posicionConductorBono = listaDeViajes.indexOf(Collections.max(listaDeViajes));
    	//Da la posicion del mayor numero de viajes entre los conductores
    	
    	Conductor conductorMasViajes = Conductor.getConductores().get(posicionConductorBono);
    	//Da la posicion del conductor con mas viajes
    	
    	int porcentajeBono = (int) (conductorMasViajes.sueldo * 0.10);
    	
    	int totalBono = conductorMasViajes.sueldo + porcentajeBono;
    	
    	conductorMasViajes.sueldo = totalBono; //Actualiza el sueldo del conductor
    	
    	
    }

    // ----- G E T   A N D   S E T -----

    public void setCategoria(Categoria categoria) {
        this.categoria = categoria;
    }

    public static ArrayList<Conductor> getConductores() {
        return conductores;
    }

    public ArrayList<Viaje> getHistoriaViajesRealizados() {      return historiaViajesRealizados;   }

    @Override
    public void renunciar() {
    }
}