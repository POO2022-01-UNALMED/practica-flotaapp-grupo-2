/*
 * Clase con la funcionalidad para retornar un string con la ciudad con destino mas frecuente sobre su historial o ciudad mas visitada
 * Estructuras: ArrayList, Scanner, HashMap
 * 
 * @author: Mateo Hechavarria, Juan Pablo Pineda, Miguel Angel Fonseca, Haison Urrutia
 */




package uiMain.funcionalidades;

import gestorAplicacion.Comprador;
import gestorAplicacion.Ciudad;
import gestorAplicacion.Tiquete;
import uiMain.Main;

import java.util.HashMap;
import java.util.ArrayList;


public class Recomendacion{

	public static HashMap<Ciudad, Integer> promociones = new HashMap<>();
	private static HashMap<Ciudad,Integer> visitadas = new HashMap<>();
	
	
	
	// validar historico de viajes por usuario
	
	public static String recomendarViaje(int cc) {        
		System.out.println("----- R E C O M E N D A R   V I A J E -----" + "\n");		
		Ciudad recomendadisima = new Ciudad();
		Comprador aRecomendar = new Comprador();
		for(Comprador comprador : Comprador.getCompradores()){
			if(comprador.getCc() == cc){ aRecomendar = comprador;}
		}
		/*
		 * Se va a guardar en visitadas la cantidad de viajes por usuario, para esto se recorre la lista de historicoViaje
		 * del usuario solicitado y para posteriormente guardarlo en el valor de cada ciudad la cual es la llave de HashMap
		 */
		
		if (Comprador.getCompradores().contains(aRecomendar) && (aRecomendar.getHistoricoViajes().size() > 0)) {
			for(Tiquete cadaTiquete: aRecomendar.getHistoricoViajes()) {
				if (visitadas.isEmpty()) {
					visitadas.put(cadaTiquete.getViaje().getDestino(), 1); //inicializa en 1 la Ciudad
				}
				else if (visitadas.containsKey(cadaTiquete.getViaje().getDestino())) { //Suma 1 al valor de la ciudad (llave)
					visitadas.put(cadaTiquete.getViaje().getDestino(), visitadas.get((cadaTiquete.getViaje().getDestino())) + 1);
				}
				else {
					visitadas.put(cadaTiquete.getViaje().getDestino(), 1);
				}
			}
			
			Ciudad masVisitada = null;
			int visitas = 0;
			for (Ciudad cadaCiudad: visitadas.keySet()) {
				if ((promociones.containsKey(cadaCiudad)) && ((visitadas.get(cadaCiudad)) > visitas)) {
					masVisitada = cadaCiudad;
					visitas = visitadas.get(cadaCiudad);
				}else {
					continue;
				}
			}
			recomendadisima = masVisitada;
			
			
		}
		
		else { //Busca la ciudad con mas visitas y la devuelve como recomendacion
			Ciudad masVisitada = null;
			int visitas = 0;
			for (Ciudad cadaCiudad: Ciudad.getCiudades()) {
				if((cadaCiudad.getNumVisitantes() > visitas) && promociones.containsKey(cadaCiudad)) {
					masVisitada = cadaCiudad;
					visitas = cadaCiudad.getNumVisitantes();					
				}else {
					continue;
				}
		    }
			
			recomendadisima = masVisitada;
		}
		
		String mesage = "Te recomendamos viajar a: \n" + recomendadisima.toString();

		
		return mesage;

		
	}

	public static HashMap<Ciudad, Integer> getPromociones() {
		return promociones;
	}
}
