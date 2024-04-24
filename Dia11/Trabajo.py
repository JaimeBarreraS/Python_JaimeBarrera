import json #Importo el modulo Json

with open('jaime.json', encoding='utf-8') as f: #abro el archivo 'jaime.json' en modo lectura, lo decodifico utilizando utf-8.  
    datos = json.load(f) #la variable datos tendra los datos del archivo 'jaime.json #as f crea un objeto de archivo llamado f que representa el archivo abierto.

goku = True #boleano llamada goku con el valor True

while goku: #se abre while mientras goku sea true
    
    Types = set(i['type'] for i in datos if 'type' in i) # creo un conjunto llamado Types y que se guarde una vez y no repetidas

    print("\nTYPES:")
    print("")
    for tipo in Types: #este for repite sobre cada valor type en el conjunto Types e imprime cada uno de ello
        print(tipo)

    print("")
    tipo = input("Ingrese el type: ") #pido el nombre de la clave type y lo guardo en la variable tipo

    if tipo in Types:#verifico si la clave que se ingresa se encuentra en types
        print("")
        print("         MENU:") 
        print("1. Revisar")
        print("2. Crear")
        print("3. Actualizar")
        print("4. Eliminar")
        print("5. Salir")
        print("")
        opcion = int(input("Ingrese un numero del 1 al 5: "))

        if opcion == 1:# revisa los datos
            for i in datos:#se repite en la lista datos
                if i['type'] == tipo: #se verifica si el valor de la clave type del diccionario es igual al valor de la variable tipo
                    print(f"\nDatos para el type '{tipo}':") #si la condicion se cumple le digo que me impeima los datos dentro del type
                    for clave, valor in i.items(): #este for me permite ver la informacion de de los datos con clave y valor
                        print(f"{clave}: {valor}") #imprimo clave y valor de los datos de type 

        elif opcion == 2:# Crear nuevo dato 
            Dato_N = {'type': tipo} #creo un nuevo diccionario  Dato_N con una clave 'type' el valor es de la variable tipo (que ingreso arriba)
            for i in datos:#se repite en la lista datos
                if i['type'] == tipo:#se verifica si el valor de la clave type del diccionario es igual al valor de la variable tipo
                    for clave in i.keys():#se repite sobre todas las claves del diccionario utilizando i.keys()
                        if clave != 'type':# verifica si la clave actual es diferente de la cadena 'type'
                            valor = input(f"Ingrese el valor para '{clave}': ") #se ingrese un valor para las demas claves
                            Dato_N[clave] = valor #se agrega la clave y su valor al nuevo diccionario Dato_N
            datos.append(Dato_N)#se agrega Dato_N a la lista datos
            print(f"Se ha creado un nuevo dato en el type '{tipo}'")
            

        elif opcion == 3: # Actualizar datos 
            for i in datos:#se repite en la lista datos
                if i['type'] == tipo:##se verifica si el valor de la clave type del diccionario es igual al valor de la variable tipo
                    for clave, valor in i.items():#este for me permite ver la informacion de de los datos con clave y valor
                        if clave != 'type':# verifica si la clave actual es diferente de la cadena 'type'
                            Valor_N = input(f"Ingrese el nuevo valor para '{clave}' (actual: {valor}): ") # se ingresa el nuevo valor para la clave actual
                            if Valor_N:#Verifica si el usuario ingresa un nuevo valor 
                                i[clave] = Valor_N #se agrega el nuevo valor a la clave
            print(f"Se han actualizado los datos del type '{tipo}'")

        elif opcion == 4:# Eliminar 
            D_actualizado = [i for i in datos if i['type'] != tipo] # Crea una nueva lista D_actualizado que contiene todos los diccionarios de la lista 'type' no coincide con el valor de la variable tipo
            if len(datos) == len(D_actualizado):#Compara la longitud de las listas datos y D_actualizado Si son iguales significa que no se eliminó ningún elemento
                print(f"No se encontraron datos para el type '{tipo}'") #imprime la informacion de type
            else:#Si la longitud de las listas datos y D_actualizado es diferente significa que se eliminaron algunos elementos
                datos[:] = D_actualizado #le da a la lista D_actualizado a la lista datos, reemplazando los elementos de datos por la nueva lista sin los elementos eliminados.
                print(f"Se han eliminado los datos del type '{tipo}'") #Imprime un mensaje que seelimino

        elif opcion == 5: #opcion 5 salir
            # Salir
            goku = False #valor de goku false para salir

        else:
            print("Opcion no valida") #si no ingresa un numero del 1 al 5 me sale este print

        # Guardar datos en el archivo JSON
        with open('jaime.json', 'w', encoding='utf-8') as f:
            json.dump(datos, f)

    else:
        print(f"El type '{tipo}' no existe")

#hecho por Jaime Barrera cc 1093925253