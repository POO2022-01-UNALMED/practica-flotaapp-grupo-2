from tkinter import messagebox

class ExceptionPopUp():
    def __init__(self, mensaje):
        self._mensaje = mensaje
        messagebox.showinfo(title = "Error en la aplicación", message = mensaje)

class ErrorAplicacion(Exception):
    def __init__(self, extra_message="", message="Manejo de errores de la Aplicación: "):
        c_type = type(self)
        self.message = message + " " + extra_message
        super().__init__(self.message)

class FieldException(ErrorAplicacion):
    def __init__(self, message):
        super().__init__(extra_message=message)


class LengthException(FieldException):
    def __init__(self, message="La longitud de la cadena no es suficiente"):
        super().__init__(message)


class ViewException(ErrorAplicacion):
    def __init__(self, message):
        super().__init__(extra_message=message)

class ClientIncorrectoException(ViewException):
    def __init__(self, message="Esta usado un id del cliente incorrecto"):
        super().__init__(message)


class NumericException(FieldException):
    def __init__(self, message="Esta usando valores no numericos"):
        super().__init__(message)

class EmptyException(FieldException):
    def __init__(self, message="Campo vacio"):
        super().__init__(message)



        


