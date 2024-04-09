#EJERCICIO 2

print("")
print("Buenas mi primer Trabajo")
print("")

#INGRESA POR TECLADO LA INFORMACION ////////////////////////

print("Ingresa tu nombre:")
ingresar=input()
print("")

#CONVERTIR VARIABLES/////////////////////////////////////////

#texto a numero

print("Texto a Numero")
Texto="Jaime Barrera"
print(Texto)
print(type(Texto))
print("")


print("Texto a Numero")
print("Jaime Barrera a 24")
Texto=24
print(Texto)
print(type(Texto))
print("")

#Numero a decimal

print("Numero a Decimal")
print(Texto)
print(type(Texto))
print("")
print("Numero a Decimal")
print("24 a 1.234")
Texto=1.234
print(Texto)
print(type(Texto))
print("")

#BUCLES FOR Y WHILE///////////////////////////////////////////////

#Bucle for

print("Bucle for")
for i in range (4):
    print(i,"Soy camper")
print("")

#Bucle while
print("Bucle while")
n = 1
while n <= 5:
    print(n)
    n = n + 1
print("")

#FUNCIONES////////////////////////////////////////////////////////////

#Funcion simple

print("Funcion Simple")
print("----------------")
def camper():
    print("Hola Camper!")
    print("Bienvenido a Campusland")

camper() #llamo la funcion
print("")

#Funcion parametros y argumentos
print("Funcion parametros y argumentos")
print("----------------")
def camper(nombre,apellido):
    print(f"Hola Camper, {nombre} {apellido}")
    print("Bienvenido a Campusland")

camper("Jaime","Barrera") #llamo la funcion
print("")

#Funcion argumentos opcionales
print("Funcion argumentos opcionales")
print("----------------")
def camper(nombre,apellido="Sandoval"):
    print(f"Hola Camper, {nombre} {apellido}")
    print("Bienvenido a Campusland")

camper("Jaime",) #llamo la funcion
print("")

#Funcion argumentos nombrados
print("Funcion argumentos nombrados")
print("----------------")
def camper(nombre,apellido="Sandoval"):
    print(f"Hola Camper, {nombre} {apellido}")
    print("Bienvenido a Campusland")
    
camper(apellido="Barrera",nombre="Jaime") #llamo la funcion
print("")


# Desarrollado por Jaime Barrera - C.C 1.093.925.253