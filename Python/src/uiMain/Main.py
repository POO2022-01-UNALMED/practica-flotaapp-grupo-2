from gestorAplicacion.Comprador import Comprador
from gestorAplicacion.Silla import Silla

# COMPRADORES
comprador1 = Comprador(1, "Mateo", "example@email.com", 3234567890)
comprador2 = Comprador(2, "Marcos", "example2@email.com", 3087654321)
comprador3 = Comprador(3, "Lucas", "example3@email.com", 3088890321)
comprador4 = Comprador(4, "Juan", "example4@email.com", 3087656654)
comprador5 = Comprador(5, "Estrella", "example5@email.com", 3087756654)


print(comprador1, comprador1.getHistocioViaje())
print(comprador2, comprador2.getHistocioViaje())
print(comprador3, comprador3.getHistocioViaje())
print(comprador4, comprador4.getHistocioViaje())
print(comprador5, comprador5.getHistocioViaje())
