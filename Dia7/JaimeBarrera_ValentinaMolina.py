#--------------------------
#PYTHON - DICCIONARIOS
#---------------------------
# Definir un diccionario de productos
diccionario = {
    "P1": {                    #clave P1 que muestra el producto con el nombre, precio y cantidad
        'Nombre': "Yuca",
        'Precio': 1500,
        'Cantidad': 20
    },
    "P2": {                    #clave P2 que muestra el producto con el nombre, precio y cantidad
        'Nombre': "papa",
        'Precio': 1200,
        'Cantidad': 10
    },
    "P3": {                    #clave P2 que muestra el producto con el nombre, precio y cantidad
        'Nombre': "manzana",
        'Precio': 2000,
        'Cantidad': 12
    }
}

# Imprimir mensaje de bienvenida

print("\n¡¡BIENVENIDOS A SUPER-VALJAI!!")


# Mostrar información de los productos disponibles
for clave in diccionario:               #este for repite sobre cada clave del diccionario
    producto = diccionario[clave]       #se obtiene el valor que tiene cada clave (nombre,precio,cantidad)
    print(f"\nProducto: {producto['Nombre']} - Precio: ${producto['Precio']} - Cantidad: {producto['Cantidad']}") #hago un print contatenado para mostrar nombre,precio y cantidad

# Mostrar la clave de cada producto
print("\nCLAVES DE PRODUCTOS")
print("P1=yuca")        #P1
print("P2=papa")        #P2
print("P3=manzana")     #P2

# Mostrar el menú de opciones
print("")
print("1. Agregar productos al carrito")  #agregar
print("2. Ver contenido del carrito")     #ver
print("3. Calcular valor de la compra")   #calcular
print("4. Salir del programa")
print("")

# Solicitar al usuario que ingrese una opción
opcion = int(input("Ingrese una opción: ")) #le pido que me escriba un numero del 1 al 4
print("")

# Inicializar el carrito como una lista vacía
carrito = []

# Bucle principal del programa
while opcion != 4: #creo un while que si es diferente a 4 me haga las otras opciones

    # Opción 1: Agregar productos al carrito
    if opcion == 1: #si opcion es igual a 1 
        codigo = input("Ingrese la clave del producto: ") #le pido que ingrese la clave del producto
        if codigo in diccionario:
            producto = diccionario[codigo]
            cantidad = int(input(f"Ingrese la cantidad de {producto['Nombre']}: "))
            if cantidad <= producto['Cantidad']:
                carrito.append((codigo, cantidad))
                print("")
                print("Producto agregado al carrito.")
            else:
                print("No hay suficiente cantidad disponible.")
        else:
            print("Código de producto inválido.")

    # Opción 2: Ver contenido del carrito
    elif opcion == 2:
        if carrito:
            print("Contenido del carrito:")
            for item in carrito:
                codigo, cantidad = item
                producto = diccionario[codigo]
                valor = producto['Precio'] * cantidad
                print(f"{producto['Nombre']}: {cantidad} unidades - Valor: ${valor}")
        else:
            print("El carrito está vacío.")

    # Opción 3: Calcular valor de la compra
    elif opcion == 3:
        total = 0
        for item in carrito:
            codigo, cantidad = item
            producto = diccionario[codigo]
            total += producto['Precio'] * cantidad
        print(f"El valor total de la compra es: ${total}")

    # Opción inválida
    else:
        print("\nOpción inválida.")

    # Mostrar el menú de opciones nuevamente
    print("\nESTAS EN EL MENU PRINCIPAL")
    print("\n1. Agregar productos al carrito")
    print("2. Ver contenido del carrito")
    print("3. Calcular valor de la compra")
    print("4. Salir del programa")

    # Solicitar al usuario que ingrese una nueva opción
    opcion = int(input("\nIngrese una opción: "))
    print("")

# Mensaje de despedida

print("\n GRACIAS POR ELEGIR A SUPER-VALJAI")
print("\n Esta es tu factura o resumen de  compra")
print("")

if opcion == 4:
        if carrito:
            print("LOS PRODUCTOS DE TU COMPRA SON: ")
            for item in carrito:
                codigo, cantidad = item
                producto = diccionario[codigo]
                valor = producto['Precio'] * cantidad
                print(f"{producto['Nombre']}: {cantidad} unidades - Valor: ${valor}")
        else:
            print("EN EL MEMENTO NO HAZ COMPRADO NINGUN PRODUCTO")
        
        if opcion == 4:
            total = 0
        for item in carrito:
            codigo, cantidad = item
            producto = diccionario[codigo]
            total += producto['Precio'] * cantidad
        print(f"El valor total de tu compra es: ${total}")

print("\n¡Gracias por su compra!")
#Jaime Barrera CC.1093925253 Valentida Molina CC.1007109135