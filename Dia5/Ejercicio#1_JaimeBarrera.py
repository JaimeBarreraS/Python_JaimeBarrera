def contador_pares(n, k): #Función que cuenta el número de pares de enteros distintos (ai, aj) en la lista n que ai + aj es divisible por k.
    jaime = len(n)  # Longitud de la lista n
    contador = 0  # Contador para llevar la cuenta de los pares válidos
    pares = set()  # Conjunto para almacenar pares únicos, .set() es para crear un conjunto vacio
    pares_validos = []  # Lista para almacenar los pares válidos

    # Bucle para repetir sobre todos los pares posibles
    for i in range(jaime):
        for j in range(i+1, jaime):
            # Verificar si la suma del par es divisible por k
            if (n[i] + n[j]) % k == 0:
                p = tuple(sorted((n[i], n[j])))  # Crear una tupla ordenada con el par
                #tuple es para crear un tipo de datos que representa una secuencia ordenada de elementos que no se pueden modificar ejemplo (1,2)
                #sorted sirve para ordenar de menor a mayor, una lista, una tupla o cadena en este caso la tupla ejemplo (1,2)(1,3)(1,4)
                if p not in pares:  # Verificar si el par no ha sido contado antes
                    pares.add(p)  # Agregar el par al conjunto de pares únicos .add agregar elementos a un conjunto
                    pares_validos.append(p)  # Agregar el par a la lista de pares válidos .appernd agregar elementos a una lista
                    contador += 1  # Incrementar el contador de pares válidos

    return contador, pares_validos  # Devolver la tupla con el contador y la lista de pares válidos

# Entrada del usuario
entrada = input("N: ") #obtengo el valor de la lista de numeros 
n = [int(num) for num in entrada]  # Convertir la entrada a una lista de enteros
k = int(input("K: "))  # Obtener el valor de k

# Llamar a la función contador_pares y almacenar los resultados
resultado, pares_validos = contador_pares(n, k)

# Imprimir los resultados
print("")
print(f"Case 1: {resultado}")  # Imprimir el número de pares válidos
print("")
print("pares:")  # lista de pares válidos
for p in pares_validos:
    print(p)  # Imprimir cada par válido

# hecho por Jaime Barrera Sandoval cc 1.093.925.253 #camper