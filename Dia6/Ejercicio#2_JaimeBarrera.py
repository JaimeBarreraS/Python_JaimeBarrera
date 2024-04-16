def twoSum(nums, target):#Función que encuentra los índices de dos números en la lista nums que suman el valor target.
    lista = {} #diccionario llamado lista
    
    # repite sobre la lista nums
    for i, num in enumerate(nums):
        complemento = target - num # Calcular el complemento del número actual
        if complemento in lista: # Verificar si el complemento está presente en el diccionario
            return [lista[complemento], i] # Si el complemento está presente, devolver los índices de los dos números
        lista[num] = i # Agregar el número actual y su índice al diccionario
    return [] # Si no se encuentra una solución, devolver una lista vacía

# Función para ingresar la lista de enteros y el target
def entrada():
    entrada = input().split() #obtengo el valor de la lista de numeros con espacios
    nums = [int(num) for num in entrada[:-1]]# Convertir la entrada a una lista de enteros
    target = int(entrada[-1])# Obtener el valor de target
    return nums, target #retorno

# Pedir al usuario que ingrese la lista de números y el valor de target
nums, target = entrada()

# Llamar a la función twoSum
result = twoSum(nums, target)

# Imprimir el resultado
if result:
    print(f"{result}")

# hecho por Jaime Barrera Sandoval cc 1.093.925.253 #camper