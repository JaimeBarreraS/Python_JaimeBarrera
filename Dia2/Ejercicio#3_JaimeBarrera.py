import random #libreria de valores aletorios

# Mensaje de bienvenida
print("") # Imprime una línea en blanco para separar
print("ADIVINAR NUMERO SECRETO DEL 1 AL 100")
print("             ¡¡¡¡EXITOS!!!")
print("")# Imprime una línea en blanco para separar

# Generar un número aleatorio entre 1 y 100 que el jugador debe adivinar
num = random.randint(1, 100) #random.randit le indico que me genere un numero aletorio entre esos valores

# Inicializar contador de intentos y establecer el número máximo de intentos permitidos
intentos = 0  
totalIntentos = 10

# Indicar al jugador que debe adivinar el número en un máximo de 10 intentos
print("Adivina el numero en 10 intentos")

# Bucle principal del juego
while intentos < totalIntentos:
    intentos += 1  # Incrementar el contador de intentos en cada numero de intento
    print("") # Imprime una línea en blanco para separar
    print(f"Intento número: {intentos}")
    
    # Solicitar al jugador que ingrese un número para adivinar
    intento = int(input("Ingresa tu número: ")) 
    
    # Compara el número ingresado con el número secreto y da pistas
    if intento < num:# if Bloque de código si la condicion1 es True
        print("El número es mayor")
    elif intento > num:# Bloque de código si la condicion2 es True (si condicion1 es False)
        print("El número es menor")
    else:# Bloque de código si todas las condiciones anteriores son False
        # Si el número ingresado es igual al número secreto, el jugador ha adivinado correctamente
        print(f"¡Advinaste el número! Era {num}")
        break # Sale del bucle 'while' si el usuario no quiere continuar.

# Comprobar si el jugador agotó todos los intentos sin adivinar el número secreto
if intento != num:#!=sirve para comparar
# if Bloque de código si la condicion1 es True
    print("") # Imprime una línea en blanco para separar
    print(f"¡Fallaste! El número era {num}")
    print("") # Imprime una línea en blanco para separar