entrada = input("") 
# Solicita al usuario que ingrese números separados por espacios y los almacena en la variable 'entrada' como una cadena de texto

lista = tuple(sorted(set(map(int, entrada.split()))))
# Realiza las siguientes operaciones para convertir la entrada en una tupla ordenada de números únicos:
# 1. entrada.split() divide la cadena 'entrada' en una lista, usando los espacios en blanco como separadores
# 2. map(int, entrada.split()) aplica la función int convirtiéndolas en números enteros
# 3. set(map(int, entrada.split())) crea un conjunto a partir de la lista de números enteros, eliminando así los elementos duplicados
# 4. sorted(set(map(int, entrada.split()))) ordena los elementos del conjunto en orden ascendente
# 5. tuple(sorted(set(map(int, entrada.split())))) convierte la lista ordenada de números únicos en una tupla
# El resultado final se almacena en la variable 'lista'

print(lista) # Imprime el contenido de la variable 'lista', que es una tupla ordenada de números únicos ingresados por el usuario