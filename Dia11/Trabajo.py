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

        elif opcion == 2:  # Crear nuevo dato
            Dato_N = {'type': tipo}  # Crea un nuevo diccionario Dato_N con una clave 'type' y el valor de la variable tipo
            for i in datos:  # Itera sobre la lista datos
                if i['type'] == tipo:  # Si el valor de la clave 'type' coincide con el tipo seleccionado
                    for clave in i.keys():  # repite sobre todas las claves del diccionario
                        if clave != 'type':  # Si la clave actual es diferente de 'type'
                            valor = input(f"Ingrese el valor para '{clave}': ")  # Solicita al usuario el valor para esa clave
                            if valor:  # Si el usuario ingresa un valor
                                Dato_N[clave] = valor  # Agrega la clave y el valor al nuevo diccionario Dato_N
                            else:  # Si el usuario no ingresa un valor
                                sub_claves = input(f"¿Desea agregar subclaves para '{clave}'? (si/no): ")  # Pregunta si desea agregar subclaves
                                if sub_claves.lower() == 'si':  # Si la respuesta es si
                                    Dato_N[clave] = {}  # Inicializa la clave con un diccionario vacío
                                    while True:  # Bucle para agregar subclaves
                                        sub_clave = input(f"Ingrese el nombre de la subclave: ")
                                        if not sub_clave:  # Si el usuario no ingresa nada 
                                            break  # Sale del bucle de subclaves
                                        sub_valor = input(f"Ingrese el valor para la subclave '{sub_clave}': ")
                                        Dato_N[clave][sub_clave] = sub_valor  # Agrega la subclave y su valor al diccionario 
            datos.append(Dato_N)  # Agrega el nuevo diccionario Dato_N a la lista datos
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

        elif opcion == 4:  # Eliminar
            id_eliminar = input(f"Ingrese el ID del dato '{tipo}': ")  # Solicita al usuario el ID del dato a eliminar

            eliminado = False  #boleano
            D_actualizado = []  # Lista para almacenar los datos actualizados

            for i in datos:  # Itera sobre la lista de datos
                if i['type'] == tipo:  # Si el valor de la clave 'type' coincide con el tipo seleccionado
                    if str(i.get('id', '')) == id_eliminar:  # Si el valor de la clave 'id' coincide con el ID ingresado
                        eliminado = True  # cierro el boleano y dice que se elimino un dato
                    else:
                        D_actualizado.append(i)  # Agrega el dato a la lista actualizada si no coincide con el ID

            if eliminado:
                datos[:] = D_actualizado  # Actualiza la lista de datos original con la lista actualizada
                print(f"Se ha eliminado el dato con ID '{id_eliminar}' del type '{tipo}'")
            else:
                print(f"No se encontró ningún dato con ID '{id_eliminar}' en el type '{tipo}'")

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