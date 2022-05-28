package gestorAplicacion;

import java.io.Serializable;
import java.util.ArrayList;

public class Vehiculo implements Serializable {
    private String placa;
    private Conductor conductor;
    private ArrayList<Silla> sillas;

    public Vehiculo(String placa, ArrayList<Silla> sillas){
        this.placa = placa;
        this.setSillas(sillas);
    }

    public String getPlaca() {   
    	return placa;
    	}

    public Conductor getConductor() { 
    	return conductor;  
    	}

    public void setConductor(Conductor conductor) {
        this.conductor = conductor;
    }

	public ArrayList<Silla> getSillas() {
		return sillas;
	}

	public void setSillas(ArrayList<Silla> sillas) {
		this.sillas = sillas;
	}

    //public Silla selecionarSilla() {}

}