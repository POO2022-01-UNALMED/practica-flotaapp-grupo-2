import sys
sys.path.append("../practica-flotaapp-grupo-2/Python/src")

from gestorAplicacion.Comprador import Comprador
from gestorAplicacion.Ciudad import Ciudad
from gestorAplicacion.Vehiculo import Vehiculo
from gestorAplicacion.Silla import Silla, Ubicacion
from gestorAplicacion.Viaje import Viaje
from gestorAplicacion.Conductor import Conductor, Categoria
from gestorAplicacion.Especialista import Especialidad, Especialista
from Funcionalidades.Gestionar import Gestionar
from Funcionalidades.VisualizarEstadisticas import VisualizarEstadisticas
from Funcionalidades.Asignar import Asignar

from datetime import datetime
from datetime import timedelta

# COMPRADORES
comprador1 = Comprador(1, "Mateo", "example@email.com", 3234567890)
comprador2 = Comprador(2, "Marcos", "example2@email.com", 3087654321)
comprador3 = Comprador(3, "Lucas", "example3@email.com", 3088890321)
comprador4 = Comprador(4, "Juan", "example4@email.com", 3087656654)
comprador5 = Comprador(5, "Estrella", "example5@email.com", 3087756654)

##FRECHAS
fin = datetime.now() + timedelta(days=15)
inicio = datetime.now() + timedelta(days=2)
intermedio = datetime.now() + timedelta(days=10)

# CIUDADES
Medellin =  Ciudad(1, "MEDELLIN", "calle X - 95")
Bello =  Ciudad(12, "BELLO", "calle Y - 72")
Popayan =  Ciudad(7, "POPAYAN", "calle X - 37")
Cali =  Ciudad(8, "CALI", "calle F - 13")
Monteria =  Ciudad(5, "MONTERIA", "circular 4 # 1 - 44")
Cartagena =  Ciudad(4, "CARTAGENA", "calle G - 14")
Pasto =  Ciudad(6, "PASTO", "Carrera 24 # 4 - 22")
Barranquilla =  Ciudad(9, "BARRANQUILLA", "calle siempre viva # 123")
Manizales =  Ciudad(3, "MANIZALES", "avenida 24 # 3-23")

## SILLAS
se1v1 =   Silla(7, False, Ubicacion.VENTANA)
se2v1 =   Silla(8, False, Ubicacion.PASILLO)
sp1v1 =   Silla(1, True, Ubicacion.VENTANA)
sp2v1 =   Silla(2, True, Ubicacion.PASILLO)
sp3v1 =   Silla(3, True, Ubicacion.VENTANA)
sp4v1 =   Silla(4, True, Ubicacion.PASILLO)
sp5v1 =   Silla(5, True, Ubicacion.VENTANA)
sp6v1 =   Silla(6, True, Ubicacion.PASILLO)
sillasv1 = [se1v1, se2v1, sp1v1, sp2v1, sp3v1, sp4v1, sp5v1, sp6v1]

se1v2 =   Silla(3, False, Ubicacion.VENTANA)
se2v2 =   Silla(5, False, Ubicacion.PASILLO)
se3v2 =   Silla(4, False, Ubicacion.PASILLO)
sp1v2 =   Silla(6, True, Ubicacion.VENTANA)
sp3v2 =   Silla(1, True, Ubicacion.VENTANA)
sp2v2 =   Silla(2, True, Ubicacion.PASILLO)
sillasv2 =  [se1v2, se2v2, sp1v2, sp2v2, sp3v2, se3v2]

se1v3 =   Silla(3, False, Ubicacion.VENTANA)
se2v3 =   Silla(4, False, Ubicacion.PASILLO)
sp1v3 =   Silla(1, True, Ubicacion.VENTANA)
sp2v3 =   Silla(2, True, Ubicacion.PASILLO)
sillasv3 =   [se1v3, se2v3, sp1v3, sp2v3]

#VEHICULO
v1 =   Vehiculo("AAA000", sillasv1)
v2 =   Vehiculo("ZZZ999", sillasv2)
v3 =   Vehiculo("ABC123", sillasv3)

#VIAJES
viaje2 =   Viaje(4, 40000, 10000, 15000, Monteria, Pasto, 12, v2, intermedio)
viaje3 =   Viaje(3, 35000, 12000, 18000, Medellin, Manizales, 24, v3, fin)
viaje1 =   Viaje(1, 30000, 15000, 22000, Bello, Cali, 24, v1, intermedio)
viaje4 =   Viaje(2, 30000, 11000, 17000, Medellin, Cartagena, 12, v1, fin)
viaje5 =   Viaje(10, 30000, 15000, 20000, Medellin, Barranquilla, 32, v2, inicio)
viaje6 =   Viaje(22, 30000, 11500, 13500, Medellin, Popayan, 48, v3, fin + timedelta(days=2))

# PROMOCIONES
Pasto.setPromocion(25)
Cali.setPromocion(10)
Bello.setPromocion(15)
Medellin.setPromocion(20)
Manizales.setPromocion(35)


#EMPLEADOS
mec1 =   Especialista(27, "Jose", "emailMecanico1@example.com", 3224568585, 3500, Especialidad.MECANICO)
ele1 =   Especialista(78, "Maria", "emailElectrico1@example.com", 3224567585, 4000, Especialidad.ELECTRICO)
ele2 =   Especialista(88, "Joselipa", "emailElectrico2@example.com", 3228867585, 4000, Especialidad.ELECTRICO)
ele3 =   Especialista(98, "Carlos", "emailElectrico3@example.com", 3229967585, 4000, Especialidad.ELECTRICO)
mec3 =   Especialista(32, "Pablo", "emailMecanico3@example.com", 3224538585, 3700, Especialidad.MECANICO)
si1 =   Especialista(12, "Edgar", "emailSillas1@example.com", 3224588485, 3000, Especialidad.SILLETERIA)
si2 =   Especialista(102, "Ramon", "emailSillas2@example.com", 3224599485, 3000, Especialidad.SILLETERIA)
si3 =   Especialista(120, "Angelica", "emailSillas3@example.com", 3224500485, 3000, Especialidad.SILLETERIA)

#CONDUCTORES
con1 =   Conductor(28, "Don Javie", "DonJavier@example.com", 3004569696, 4000, Categoria.B3)
con2 =   Conductor(29, "Don Hernan", "DonHernan@example.com", 3007569696, 4100, Categoria.C1)
con3 =   Conductor(30, "Dona Marta", "DonaMarta@example.com", 3004589696, 4200, Categoria.C2)


#funcionamiento de comprarTiquete
comprador1.comprarTiquete(Bello, Cali, 80000)
comprador2.comprarTiquete(Monteria, Pasto, 50000)
comprador4.comprarTiquete(Monteria, Pasto, 90000)
comprador3.comprarTiquete(Bello, Cali, 90000)
comprador3.comprarTiquete(Bello, Cali, 90000)
comprador3.comprarTiquete(Monteria, Pasto, 100000)
comprador5.comprarTiquete(Medellin, Cartagena, 100000)
comprador5.comprarTiquete(Medellin, Cartagena, 100000)
comprador5.comprarTiquete(Medellin, Barranquilla, 100000)
comprador1.comprarTiquete(Medellin, Popayan, 100000)


#funcionalidad Asignar Viaje
Asignar.asignarVehiculoConductor(con1, viaje1)
Asignar.asignarVehiculoConductor(con2, viaje3)

Asignar.asignarVehiculoEspecialista(mec1, v1)
Asignar.asignarVehiculoEspecialista(si1, v2)
Asignar.asignarVehiculoEspecialista(si2, v1)
Asignar.asignarVehiculoEspecialista(ele1, v2)



if __name__ == '__main__':
    
    VisualizarEstadisticas.visualizarEstadisticas()
    Gestionar.gestionarEspecialistas()
    
