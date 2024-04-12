#Este código crea un programa interactivo que permite al usuario verificar si un número dado es primo.
#Utiliza un bucle while con una variable booleana (goku) para controlar el flujo del programa y mostrar un menú de opciones al usuario
#Dependiendo de la opción seleccionada, el programa realiza diferentes acciones
#como verificar si un número es primo, detener el programa o mostrar información adicional sobre números primos y el autor
#La variable goku se utiliza para controlar cuándo el programa debe detenerse al cambiar su valor a False.

def primo(num):                   # se crea La función primo(num) para Verificar si un número es primo
    if num < 2:                   # Si el número es menor que 2, no es primo
        return False              #la función retorna False, ya que los números menores que 2 no son  primos
    for i in range(2, num):       # recorre todos los números desde 2 hasta num
        if num % i == 0:          #Aqui el operador % calcula el residuo de la división de num por i. Si el residuo es cero, significa que num no es un número primo.
            return False          #la función retorna False, indicando que num no es primo.
    return True                   #Si ningún número en el rango divide a num sin dejar residuo, la función retorna True, indicando que num es primo.

goku = True                                             # Se inicializa la variable booleana goku como True
while goku:                                             #Contenido del bucle
    print("")                                           #Creo un menu interactivo
    print("         ¡¡Bienvenido!!")                    #Con varias opciones numeradas
    print("Verifica si un número dado es primo")
    print("")
    print("             MENU")
    print("")
    print("1. Verificar si un número es primo")         #Verificar 
    print("2. Detener el programa")                     #detener
    print("3. Obtener información adicional")           #Informacion adicional
    print("")
    
    opcion = input("Elija una opcion (1, 2, 3): ")      #Solicito que el usuario ingrese un numero y que lo almacene en la variable opcion
    
    if opcion == '1':                                   #Verifico si un numero es primo
        num = int(input("Ingrese un número entero positivo: "))#usuario ingresa un numero para verificar si es primo
        if primo(num):                                  #llamo la funcion primo(num) para verificar
            print("")
            print(f"{num} es un número primo.")         #si es primo me muestra este print
        else:
            print("")
            print(f"{num} no es un número primo.")      #Si no es primo me muestra este print
    elif opcion == '2':                                 #Detener el programa
        print("")
        print("Gracias por utilizar el programa de números primos.")
        goku = False                                    #el programa se detiene al cambiar el valor de goku a false(se cierra el bucle while)
    elif opcion == '3':                                 #Obtener informacio adicional
        print("")                                       
        print("Un número primo es aquel que es divisible solo por 1 y por sí mismo.")#Informacion adicional sobre los numeros primos
        print("Autor: Jaime_Barrera_Sandoval cc 1093925253 #Camper")#Informacion sobre el autor
    else:                                               #Opcion invalida
        print("")
        print("Opción inválida. Elija una opcion (1, 2, 3): ")#Si la opcion es invalida se muestre este print hasta que sea valida

#================================================================================================================================

#la función crear para generar contraseñas seguras 
#con diferentes configuraciones de longitud y tipos de caracteres 
#el programa principal interactúa con el usuario a través de un menú de opciones
#(Generar nueva contraseña o Salir del programa) 
#La variable vegueta se utiliza como un booleano para controlar el bucle while y terminar cuando elige salir
#La combinación de la función crear y el bucle while proporciona una forma interactiva de generar contraseñas según las condiciones


import random                  # Importación de la biblioteca random para generación de números aleatorios
import string                  # Importación de la biblioteca string para trabajar con cadenas de caracteres
    #Esta función crear toma varios parámetros para generar una contraseña aleatoria con diferentes configuraciones
def crear(longitud, mayusculas=True, minusculas=True, numeros=True, simbolos=True):
    c= ''            # Inicialización de la variable caracteres como una cadena vacía y almacena los caracteres
    # Añadir caracteres según las opciones seleccionadas por el usuario
    if mayusculas:                            
        c += string.ascii_uppercase  # Agregar letras mayúsculas (A-Z)
    if minusculas:                            
        c += string.ascii_lowercase  # Agregar letras minúsculas (a-z)
    if numeros:                               
        c += string.digits           # Agregar dígitos numéricos (0-9)
    if simbolos:
        c += string.punctuation      # Agregar símbolos especiales (e.g., !@#$%^&*(){}[])
    # Generar una contraseña seleccionando caracteres aleatorios de la cadena 'caracteres'
    contrasena = ''.join(random.choice(c) for s in range(longitud))
    return contrasena                         # Retornar la contraseña generada

vegueta = True                                # Se inicializa la variable booleana vegueta como True
while vegueta:                                #Contenido del bucle
        print("")                             #Creo un menu interactivo
        print("        ¡¡Bienvenido!!")       #con opciones numeradas
        print("Este programa te permitirá generar contraseñas")
        print(" seguras con diferentes configuraciones.")
        print("")
        print("             MENÚ")
        print("")
        print("1. Generar nueva contraseña")  #Generar
        print("2. Salir del programa")        #Salir
        print("")
        
        opcion = input("Seleccione una opción (1, 2): ")     #Solicito que el usuario ingrese un numero y que lo almacene en la variable opcion
        
        if opcion == '1':                                    # Generar una nueva contraseña
            print("")
            longitud = int(input("Ingrese la longitud de la contraseña deseada: "))          # Le solcicita al usuario agregar un numero para determinar la longitud      
            mayusculas = input("¿Incluir mayúsculas? (Si/No): ").strip().lower() in ['si']   # línea de código solicita al usuario que responda "Si" o "No" para determinar si se deben incluir 
            minusculas = input("¿Incluir minúsculas? (Si/No): ").strip().lower() in ['si']   # línea de código solicita al usuario que responda "Si" o "No" para determinar si se deben inclui
            numeros = input("¿Incluir números? (Si/No): ").strip().lower() in ['si']         # línea de código solicita al usuario que responda "Si" o "No" para determinar si se deben inclui
            simbolos = input("¿Incluir símbolos? (Si/No): ").strip().lower() in ['si']       # línea de código solicita al usuario que responda "Si" o "No" para determinar si se deben inclui

            # Llamar a la función crear para generar la contraseña con las opciones seleccionadas
            generada = crear(longitud, mayusculas, minusculas, numeros, simbolos)
            print(f"Contraseña generada: {generada}")         # Mostrar la contraseña generada
        elif opcion == '2':                                   #Salir del programa
            print("Gracias por usar el Generador de Contraseñas Seguras")
            vegueta = False                                   # Cambiar vegueta a False para salir del bucle while
        else:                                                 # Opción inválida
            print("Opción no válida. Seleccione una opción (1, 2): ")#Si la opcion es invalida se muestre este print hasta que sea valida
