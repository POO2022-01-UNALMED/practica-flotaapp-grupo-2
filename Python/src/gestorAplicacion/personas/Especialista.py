import random
import time
from enum import Enum
from gestorAplicacion.personas.Empleado import Empleado
from gestorAplicacion.personas.Conductor import Conductor
from gestorAplicacion.viajes.Vehiculo import Vehiculo

class Especialidad(Enum):
    """
    Especialidad: Enum
        - Este enum lmacena las distintas categorias de los Empleados
    """

    ELECTRICO = "ELECTRICO"

    MECANICO = "MECANICO"

    SILLETERIA = "SILLETERIA"

    ADMINISTRADOR = "ADMINISTRADOR" 

class Especialista(Empleado):
    """
    Especialista contiene informacion de: 
        - ID : int
        - Nombre : String
        - email : String
        - movil : int
        - billetera : int
        - especialidad : Especialidad
        - historialVehiculosRevisados : list(Vehiculos)
        
    Especilista hereda de Empleado que a su vez hereda de Usuario. Su objetivo es referenciar Empleados 
    con distintas Especialidades e implementar metodos para cada una de estas
        
    """

    __especialistas = []

    def __init__(self, cc = 0, uNombre = "ESPECIALISTA NO REGISTRADO", email = "", movil = 666, billetera = 0, especialidad : Especialidad = Especialidad.ADMINISTRADOR, historialVehiculosRevisados = None): 
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
        time.sleep(5)                                 # Pausa la ejecusion 5 segundos para simular reision del vehiculo
        random_int = random.randint(1, 10)            # Selecciona 1 de cada 10 vehiculos para revision
        if (random_int == 7):
            print(f"EL VEHICULO NECESITA REPARACIONES")
        else:
            print("EL VEHICULO ESTA EN PERFECTO ESTADO")

    def despedir(self, empleadoE: Empleado = None):
        mesage = ""
        if (self.getEspecialidad() == Especialidad.ADMINISTRADOR):
                if empleadoE in Especialista.getEspecialistas():                  
                    mesage = "Especialista " + empleadoE.getuNombre() + " despedido."
                    empleadoE._billetera += 3000         # Brinda una liquidacion de 3000 al despedirse el eEmpleado
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
        if self._historialiVehiculosRevisados == None:
            return []
        return self._historialiVehiculosRevisados
    
    @classmethod
    def getEspecialistas(cls):
        return cls.__especialistas
    
    @classmethod
    def setEspecialistas(cls, especialistas):
        cls.__especialistas = especialistas
    
    def getCc(self):
        return self._cc

    def anadirVehiculoHistoria(self, vehiculoE: Vehiculo):
        if self._historialiVehiculosRevisados == None:
            self._historialiVehiculosRevisados = [vehiculoE]
        else:
            self._historialiVehiculosRevisados.append(vehiculoE)

    def __str__(self) : 
        return " CC: ({}) - Nombre: {} - Sueldo: {} - Especialidad: {}".format(self.getCc(),self._uNombre, self._sueldo, self._especialidad) 

