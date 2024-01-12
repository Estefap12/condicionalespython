#Perro negro

nombreCliente=input("¿Cual es su nombre? ")
paisCliente=input("¿Cual es su pais de origen? ")
cantidadPersonas=int(input("¿Cuantas personas van a reservar? "))
añoNacimientoCliente=int(input("¿En que año nacio? "))

#Calcular la edad del cliente
añoActual=2024
edadCliente=añoActual-añoNacimientoCliente

#CLASIFICAR, PREGUNTAR, DECIDIR
if edadCliente >= 18:
    print("Usted es mayor de edad")
else:
    print("Usted es menor de edad")