package uiMain.funcionalidades;

import gestorAplicacion.Comprador;
import gestorAplicacion.Ciudad;
import gestorAplicacion.Tiquete;

import java.util.HashMap;
import java.util.ArrayList;

public class Recomendacion {

	public static HashMap<Ciudad, Integer> promociones = new HashMap<>();
	private static HashMap<Ciudad,Integer> visitadas = new HashMap<>();
	
	
	
	// validar historico de viajes por usuario
	
	public static String recomendarViaje(Comprador aRecomendar) {
		Ciudad recomendadisima;
		/*
		 * Se va a guardar en visitadas la cantidad de viajes por usuario, para esto se recorre la lista de historicoViaje
		 * del usuario solicitado y para posteriormente guardarlo en el valor de cada ciudad la cual es la llave de HashMap
		 */
		
		if (Comprador.getCompradores().contains(aRecomendar)) {
			for(Tiquete cadaTiquete: aRecomendar.getHistoricoViajes()) {
				if (visitadas.isEmpty()) {
					visitadas.put(cadaTiquete.getViaje().getDestino(), 1); //inicializa en 1 la Ciudad
				}
				if (visitadas.containsKey(cadaTiquete.getViaje().getDestino())) { //Suma 1 al valor de la ciudad (llave)
					visitadas.put(cadaTiquete.getViaje().getDestino(), visitadas.get(cadaTiquete.getViaje().getDestino())+1);
				}
				else {
					visitadas.put(cadaTiquete.getViaje().getDestino(), 1);
				}
			}
			Ciudad masVisitada = null;
			int visitas = 0;
			for (Ciudad cadaCiudad: visitadas.keySet()) {
				if ((promociones.containsKey(cadaCiudad)) && (visitadas.get(cadaCiudad)) > visitas) {
					masVisitada = cadaCiudad;
					visitas = visitadas.get(cadaCiudad);
				}else {
					continue;
				}
			}
			recomendadisima = masVisitada;
			
			
		}
		
		else { //Busca la ciudad con mas visitas y la devuelve como recomendación
			Ciudad masVisitada = null;
			int visitas = 0;
			for (Ciudad cadaCiudad: Ciudad.getCiudades()) {
				if((cadaCiudad.getNumVisitantes() > visitas) && promociones.containsKey(cadaCiudad)) {
					visitas = cadaCiudad.getNumVisitantes();
					masVisitada = cadaCiudad;
				}else {
					continue;
				}
			}
			recomendadisima = masVisitada;
		}
		
		String f = promociones.get(aRecomendar)+""; //El toString saca errores
		
		return "Te recomendamos " + aRecomendar.getNombre() + " que viajes a" + recomendadisima.getNombre() + 
				" con una promoción de "  + f +"%";
		
		
	}
	

}
