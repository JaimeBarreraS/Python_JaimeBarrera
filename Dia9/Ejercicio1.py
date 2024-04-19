vegeta=[]
cuanto=int(input("ingrese la cantidad de productos: "))

for i in range(cuanto):
    print("")
    nombre=str(input("Ingrese el nombre del producto: "))
    precio=int(input("Ingrese el precio del producto: "))
    cantidad=int(input("Ingresa la cantidad del producto: "))
    vegeta.append((nombre,precio,cantidad))
    print("")
    print("¡¡Producto agregado al carrito!!")

contador = 0
for i in vegeta:
    print("")
    print("Producto #",contador +1)
    print("-----------------------")
    print("Nombre:",i[0])
    print("Precio:",i[1])
    print("Cantidad:",i[2])
    contador = contador + 1
