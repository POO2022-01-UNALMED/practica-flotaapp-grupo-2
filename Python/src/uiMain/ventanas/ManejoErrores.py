from tkinter import messagebox

class ExceptionPopUp():
    def __init__(self, mensaje):
        self._mensaje = mensaje
        messagebox.showinfo(title = "Error en la aplicación", message = mensaje)

class ErrorAplicacion(Exception):
    def __init__(self, extra_message, message="Manejo de errores de la Aplicación: "):
        c_type = type(self)
        self.message = message + " " + extra_message
        super().__init__(self.message)
    
    def mostrarMensaje(self):
        print(self.message)


class ElecionException(ErrorAplicacion):
    def __init__(self, message="No estas eligiendo una opción"):
        super().__init__(message)

class IndexException(ErrorAplicacion):
    def __init__(self, message="El valor que escoges no esta dentro del rango"):
        super().__init__(message)

class NumericException(ErrorAplicacion):
    def __init__(self, message="Estas usando valores no numericos"):
        super().__init__(message)
    







        


