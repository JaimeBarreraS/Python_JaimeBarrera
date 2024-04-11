#imprime un mensaje de bienvenida y una breve descripción de la secuencia de Fibonacci.
print("")# Imprime una línea en blanco para separar
print("Bienvenidos a la Secuencia de Fibonacci")
print("")# Imprime una línea en blanco para separar
print("En matemática, la sucesión de Fibonacci es una serie infinita de números naturales que comienza con 0 y 1, y continúa sumando los dos números anteriores para obtener el siguiente número en la secuencia: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597…")
print("")# Imprime una línea en blanco para separar

# Esta función 'secuencia' calcula el término ingresado por el usuario para la secuencia de Fibonacci.
def secuencia(n):
    a = 0
    b = 1
    
    # repite 'n' veces para calcular la secuencia.
    for s in range(n):
        c = a + b
        a = b
        b = c
    
    return b

# Esta función 'jaime' es la función principal que maneja la interacción con el usuario y llama a otras funciones.
def jaime():
    while True:
            num = int(input("Ingresa un número: "))
            print("")  # Imprime una línea en blanco para separar

            # Verifica si el número ingresado es negativo.
            if num < 0:
            # if Bloque de código si la condicion1 es True
                print("Por favor ingresa un número entero positivo.")
                continue
            
            print("")  # Imprime una línea en blanco para separar

            # Imprime la secuencia de Fibonacci para loos 'num'(numero que ingreso el usuario) 
            print("Secuencia de Fibonacci para", num, "números:")
            for s in range(num):
                print(secuencia(s))

            print("")  # Imprime una línea en blanco para separar 

            # Pregunta al usuario si desea continuar o salir del programa.
            salir = input("Deseas continuar? (si/no): ").strip().lower()
            #.lower()=sirve para convertir todo en minuscula
            #.strip()=elimina los espacion en blanco
            if salir != 'si':#!=sirve para comparar
            # if Bloque de código si la condicion1 es True
                print("¡Saliendo del programa!")
                break  # Sale del bucle 'while' si el usuario no quiere continuar
# Llama a la función 'jaime' para iniciar la interacción con el usuario.
jaime()
