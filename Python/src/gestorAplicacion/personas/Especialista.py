import random
import time
from enum import Enum
from gestorAplicacion.personas.Empleado import Empleado
from gestorAplicacion.personas.Conductor import Conductor
from gestorAplicacion.viajes.Vehiculo import Vehiculo

class Especialidad(Enum):

    ELECTRICO = "ELECTRICO"

    MECANICO = "MECANICO"

    SILLETERIA = "SILLETERIA"

    ADMINISTRADOR = "ADMINISTRADOR" 

class Especialista(Empleado):

    __especialistas = []

    def __init__(self, cc = 0, uNombre = "ESPECIALISTA NO REGISTRADO", email = "", movil = 666, billetera = 0, especialidad : Especialidad = Especialidad.ADMINISTRADOR, historialVehiculosRevisados = None): #Se está casteando bien los enumeradores?
        super().__init__(cc, uNombre, email, movil, billetera)
        self._historialiVehiculosRevisados = historialVehiculosRevisados
        self._especialidad = especialidad
        if uNombre != "ESPECIALISTA NO REGISTRADO":
            Especialista.__especialistas.append(self)

    def renunciar(self):
        Especialista.__especialistas.remove(self)
        
    @classmethod
    def desvincularEmpleado(cls, especialistaC):
        cls.__especialistas.remove(especialistaC)
     
    ## ---- M E T O D O S ---- ##

    def revisionVehiculo(self, vehiculoE : Vehiculo):
        print(f"El vehiculo {vehiculoE.getPlaca()} esta siendo revisado...")
        time.sleep(5)
        random_int = random.randint(1, 10)
        if (random_int == 7):
            print(f"EL VEHICULO NECESITA REPARACIONES")
        else:
            print("EL VEHICULO ESTA EN PERFECTO ESTADO")

    def despedir(self, empleadoE: Empleado = None):
        mesage = ""
        if (self.getEspecialidad() == Especialidad.ADMINISTRADOR):
                if empleadoE in Especialista.getEspecialistas():                  
                    mesage = "Especialista " + empleadoE.getuNombre() + " despedido."
                    empleadoE._billetera += 3000
                    Especialista.desvincularEmpleado(empleadoE)
                elif empleadoE in Conductor.getConductores():
                    mesage = "Conductor " + empleadoE.getuNombre() + " despedido"
                    empleadoE._billetera += 3000
                    Conductor.desvincularConductor(empleadoE)
                else:
                    mesage = "El empleado " + empleadoE.getuNombre() + " no está en nuestra base de datos"
        else:
            mesage = "Solo los ADMINISTRADORES pueden despedir usuarios"
        
        return mesage     
    
    ## G E T   A N D  S E T ##

    def getuNombre(self):
        return super().getuNombre()

    def getEspecialidad(self):
        return self._especialidad
    
    def getHistoricoVehiculosRevisados(self):
        return self._historialiVehiculosRevisados
    
    @classmethod
    def getEspecialistas(cls):
        return cls.__especialistas
    
    @classmethod
    def setEspecialistas(cls, especialistas):
        cls.__especialistas = especialistas

    def anadirVehiculoHistoria(self, vehiculoE: Vehiculo):
        if self.getHistoricoVehiculosRevisados() == None:
            self._historialiVehiculosRevisados = [vehiculoE]
        else:
            self._historialiVehiculosRevisados.append(vehiculoE)

    def __str__(self) : 
        return "Nombre: {} - Sueldo: {} - Especialidad: {}".format(self._uNombre, self._sueldo, self._especialidad) 
