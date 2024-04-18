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
print("")


# Mostrar información de los productos disponibles
for clave in diccionario:               #este for repite sobre cada clave del diccionario
    producto = diccionario[clave]       #se obtiene el valor que tiene cada clave (nombre,precio,cantidad)
    print(f"Producto: {producto['Nombre']} - Precio: ${producto['Precio']} - Cantidad: {producto['Cantidad']}") #hago un print contatenado para mostrar nombre,precio y cantidad

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

    if opcion == 1: # Si la opción ingresada es 1 (Agregar productos al carrito)
        codigo = input("Ingrese la clave del producto: ") #le pido que ingrese la clave del producto
        if codigo in diccionario:# Si el código ingresado existe en el diccionario de productos
            producto = diccionario[codigo] # Se obtiene el diccionario anidado correspondiente al producto
            cantidad = int(input(f"Ingrese la cantidad de {producto['Nombre']}: ")) # Se solicita al usuario que ingrese la cantidad del producto, usando su nombre
            if cantidad <= producto['Cantidad']:# Si la cantidad ingresada no excede la cantidad disponible
                carrito.append((codigo, cantidad))# Se agrega una tupla con el código y la cantidad al carrito
                print("")
                print("Producto agregado al carrito.")# Se confirma que el producto se ha agregado al carrito
            else:
                print("No hay suficiente cantidad disponible.")# Si no hay suficiente cantidad disponible, se muestra este mensaje
        else:
            print("Código de producto inválido.")# Si el código ingresado no existe en el diccionario, se muestra este mensaje

    # Opción 2: Ver contenido del carrito
    elif opcion == 2:# Si la opción ingresada es 2 (ver productos al carrito)
        if carrito: # Si 'carrito' no está vacío, se ejecuta 
            print("Contenido del carrito:")
            for elemento in carrito:# repite sobre cada elemento en 'carrito'
                codigo, cantidad = elemento # realiza el codigo y la cantidad del elemento
                producto = diccionario[codigo] # Obtiene el diccionario correspondiente al código del producto
                valor = producto['Precio'] * cantidad  # Calcula el valor total del producto multiplicando el precio por la cantidad
                print(f"{producto['Nombre']}: {cantidad} unidades - Valor: ${valor}") # Imprime el nombre del producto, la cantidad y el valor total
        else:
            print("El carrito está vacío.") # Si 'carrito' está vacío, se ejecuta esta linea

    # Opción 3: Calcular valor de la compra
    elif opcion == 3:# Si la opción ingresada es 3 (calcular el valor de la compra)
        total = 0 # Inicializa la variable total en 0
        for elemento in carrito: # repite sobre cada elemento en la lista carrito
            codigo, cantidad = elemento # Desempaca la tupla en las variables codigo y cantidad
            producto = diccionario[codigo] # Obtiene el producto del diccionario usando el código como clave
            total += producto['Precio'] * cantidad # Suma al total el precio del producto multiplicado por la cantidad
        print(f"El valor total de la compra es: ${total}") # Imprime el valor total de la compra

    # Opción inválida
    else:
        print("\nOpción inválida.") # Imprime un mensaje de opción inválida

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

if carrito:# Verifica si la lista carrito contiene elementos
    print("\n GRACIAS POR ELEGIR A SUPER-VALJAI") # Imprime un mensaje de agradecimiento
    print("\n Esta es tu factura o resumen de  compra") # Imprime resumen de la factura
    print("")
    total = 0
    for elemento in carrito:# repite sobre cada elemento en la lista carrito
        codigo, cantidad = elemento # Desempaca la tupla en las variables codigo y cantidad
        producto = diccionario[codigo] # Obtiene el producto del diccionario usando el código como clave
        valor = producto['Precio'] * cantidad # Calcula el valor del producto multiplicando el precio por la cantidad
        total += valor# Suma el valor del producto al total
        print(f"{producto['Nombre']}: {cantidad} unidades - Valor: ${valor}") # Imprime el nombre del producto, la cantidad y el valor
    print("")
    print(f"Total a pagar: ${total}")# Imprime el total a pagar
else:
    print("EN EL MEMENTO NO HAZ COMPRADO NINGUN PRODUCTO")# Imprime un mensaje indicando que no se han comprado productos

print("\n¡Gracias por su compra!")
#Jaime Barrera CC.1093925253 Valentida Molina CC.1007109135