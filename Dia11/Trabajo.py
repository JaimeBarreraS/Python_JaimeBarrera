import json #Importo el modulo Json

with open('jaime.json', encoding='utf-8') as f: #abro el archivo 'jaime.json' en modo lectura, lo decodifico utilizando utf-8.  
    datos = json.load(f) #la variable datos tendra los datos del archivo 'jaime.json #as f crea un objeto de archivo llamado f que representa el archivo abierto.

goku = True #boleano llamada goku con el valor True

while goku: #se abre while mientras goku sea true
    
    Types = set(i['type'] for i in datos if 'type' in i) # creo un conjunto llamado Types y que se guarde una vez y no repetidas

    print("\nTYPES:")
    print("")
    for tipo in Types: #este for recorre sobre cada valor type en el conjunto Types e imprime cada uno de ello
        print(tipo)

    print("")
    tipo = input("Ingrese el type: ") #pido el nombre de la clave type y lo guardo en la variable tipo

    if tipo in Types:#verifico si la clave que se ingresa se encuentra en types
        print("")
        print("         MENU:") 
        print("1. Revisar ")
        print("2. Crear")
        print("3. Actualizar")
        print("4. Eliminar")
        print("5. Salir")
        print("")
        opcion = int(input("Ingrese un numero del 1 al 5: "))

        if opcion == 1:# revisa los datos
            for i in datos:#recorre en la lista datos
                if i['type'] == tipo: #se verifica si el valor de la clave type del diccionario es igual al valor de la variable tipo
                    print(f"\nDatos para el type '{tipo}':") #si la condicion se cumple le digo que me impeima los datos dentro del type
                    for clave, valor in i.items(): #este for me permite ver la informacion de de los datos con clave y valor
                        print(f"{clave}: {valor}") #imprimo clave y valor de los datos de type 

        elif opcion == 2:  # Crear nuevo dato
            Dato_N = {'type': tipo}  # Crea un nuevo diccionario Dato_N con una clave 'type' y el valor de la variable tipo
            claves_ordenadas = []  # Crea una lista 'claves_ordenadas' para almacenar las claves ordenadas

            # Obtener las claves ordenadas de un dato existente
            for i in datos:  # Recorre cada diccionario en la lista 'datos'
                if i['type'] == tipo:  # Verifica si el valor de la clave 'type' del diccionario actual coincide con el 'type' seleccionado
                    claves_ordenadas = list(i.keys())  # Convierte las claves del diccionario en una lista y la asigna a 'claves_ordenadas'
                    break  # Sale del bucle después de encontrar un dato existente

            # Solicitar valores para las claves ordenadas
            for clave in claves_ordenadas:  # Recorre cada clave en la lista 'claves_ordenadas'
                if clave != 'type':  # Verifica si la clave actual no es 'type'
                    valor = input(f"Ingrese el valor para '{clave}': ")  # Solicita al usuario el valor para la clave actual
                    if valor:  # Si el usuario ingresa un valor
                        Dato_N[clave] = valor  # Agrega la clave y el valor al nuevo diccionario Dato_N
                    else:  # Si el usuario no ingresa un valor
                        sub_claves = input(f"¿Desea agregar subclaves para '{clave}'? (si/no): ")  # Pregunta si desea agregar subclaves
                        if sub_claves.lower() == 'si':  # Si la respuesta es 'si'
                            Dato_N[clave] = {}  # Crea la clave con un diccionario vacío
                            while True:  # Bucle para agregar subclaves
                                sub_clave = input(f"Ingrese el nombre de la subclave: ")  # Solicita el nombre de la subclave
                                if not sub_clave:  # Si el usuario no ingresa nada
                                    break  # Sale del bucle de subclaves
                                sub_valor = input(f"Ingrese el valor para la subclave '{sub_clave}': ")  # Solicita el valor para la subclave
                                Dato_N[clave][sub_clave] = sub_valor  # Agrega la subclave y su valor al diccionario

            datos.append(Dato_N)  # Agrega el nuevo diccionario Dato_N a la lista datos
            print(f"Se ha creado un nuevo dato en el type '{tipo}'") 

        elif opcion == 3:  # Actualizar datos
            print(f"\nID de datos para el type '{tipo}':")  
            ids_disponibles = []  # Crea una lista 'ids_disponibles' para almacenar los ID de los datos disponibles
            for dato in datos:  # Recorre cada diccionario en la lista 'datos'
                if dato['type'] == tipo:  # Verifica si el valor de la clave 'type' del diccionario actual coincide con el 'type'
                    id_dato = dato.get('id', '')  # Obtiene el valor de la clave 'id' del diccionario actual
                    print(f"ID: {id_dato}")  # Imprime el ID del dato actual
                    ids_disponibles.append(id_dato)  # Agrega el ID del dato actual a la lista 'ids_disponibles'

            id_actualizar = input(f"\nIngrese el ID del dato que desea actualizar: ")
            # Solicita al usuario que ingrese el ID del dato que desea actualizar 

            if not id_actualizar:  # Verifica si el usuario no ingresó ningún ID 
                print("Actualización cancelada.")  # Imprime un mensaje 
            elif id_actualizar not in ids_disponibles:  # Verifica si el ID ingresado por el usuario no se encuentra en la lista 'ids_disponibles'
                print(f"No se encontró ningún dato con ID '{id_actualizar}' en el type '{tipo}'")  # Imprime un mensaje de que no se encontró el ID
            else:  # Si el ID ingresado por el usuario es valido
                for dato in datos:  # Recorre cada diccionario en la lista 'datos'
                    if dato['type'] == tipo and str(dato.get('id', '')) == id_actualizar:
                        # Verifica si el valor de la clave 'type' del diccionario actual coincide con el 'type' seleccionado
                        # y si el valor de la clave 'id' coincide con el ID ingresado por el usuario
                        for clave, valor in dato.items():  # Recorre cada par clave-valor del diccionario actual
                            if clave != 'type' and clave != 'id':  # Verifica si la clave actual no es 'type' ni 'id'
                                Valor_N = input(f"Ingrese el nuevo valor para '{clave}' (actual: {valor}): ")  # Solicita al usuario un nuevo valor para la clave actual
                                if Valor_N:  # Verifica si el usuario ingresó un nuevo valor
                                    dato[clave] = Valor_N  # Actualiza el valor de la clave en el diccionario con el nuevo valor ingresado por el usuario
                        print(f"Se han actualizado los datos del ID '{id_actualizar}' en el type '{tipo}'")  # Imprime un mensaje de que si actualizo los datos
                        break  # Sale del bucle for después de actualizar los datos

        elif opcion == 4:  # Eliminar
            print(f"\nID de datos para el type '{tipo}':")  
            ids_disponibles = []  # Creo una lista 'ids_disponibles' para almacenar los ID de los datos disponibles
            for dato in datos:  # Recorre cada diccionario en la lista 'datos'
                if dato['type'] == tipo:  # Verifica si el valor de la clave 'type' del diccionario actual coincide con el 'type' seleccionado
                    id_dato = dato.get('id', '')  # Obtiene el valor de la clave 'id' del diccionario actual
                    print(f"ID: {id_dato}")  # Imprime el ID del dato actual
                    ids_disponibles.append(id_dato)  # Agrega el ID del dato actual a la lista 'ids_disponibles'

            id_eliminar = input(f"\nIngrese el ID del dato '{tipo}' que desea eliminar: ")
            # Solicita al usuario que ingrese el ID del dato que desea eliminar

            if not id_eliminar:  # Verifica si el usuario no ingresó ningún ID 
                print("eliminación cancelada.")  # Imprime un mensaje de cancelación
            elif id_eliminar not in ids_disponibles:  # Verifica si el ID ingresado por el usuario no se encuentra en la lista 'ids_disponibles'
                print(f"No se encontró ningún dato con ID '{id_eliminar}' en el type '{tipo}'")  # Imprime un mensaje que no se encontró el ID
            else:  # Si el ID ingresado por el usuario es válido
                eliminado = False  #boleano
                D_actualizado = []  # Crea una lista vacía llamada 'D_actualizado' para almacenar los datos actualizados

                for i in datos:  # Recorre cada diccionario en la lista 'datos'
                    if i['type'] == tipo:  # Verifica si el valor de la clave 'type' del diccionario actual coincide con el 'type' seleccionado
                        if str(i.get('id', '')) == id_eliminar:  # Verifica si el valor de la clave 'id' del diccionario actual coincide con el ID ingresado por el usuario
                            eliminado = True  # Si se cumple la condición 
                        else:
                            D_actualizado.append(i)  # Si el ID no coincide, agrega el diccionario actual a la lista 'D_actualizado'

                if eliminado:  # Verifica si se eliminó un dato
                    datos[:] = D_actualizado  # Actualiza la lista 'datos' con la lista 'D_actualizado' 
                    print(f"Se ha eliminado el dato con ID '{id_eliminar}' del type '{tipo}'")  # Imprime un mensaje de la eliminación
                else:  # Si no se eliminó ningún dato
                    print(f"No se encontró ningún dato con ID '{id_eliminar}' en el type '{tipo}'")  # Imprime un mensaje que no se encontró el ID

        elif opcion == 5: #opcion 5 salir
            # Salir
            goku = False #valor de goku false para salir

        else:
            print("Opcion no valida") #si no ingresa un numero del 1 al 5 me sale este print

        # Guardar datos en el archivo JSON
        with open('barrera.json', 'w', encoding='utf-8') as f:
            json.dump(datos, f)

    else:
        print(f"El type '{tipo}' no existe")

#hecho por Jaime Barrera cc 1093925253