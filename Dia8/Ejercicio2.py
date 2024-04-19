frutas = [('banana', 0.45, 6), ('jackfruit', 4.55, 2), ('kiwi', 0.15, 23)]

mayusculas = [i[0].upper() for i in frutas] #le digo que la posicion 0 de la tupla me la vuelva mayuscula y que hago los mismo para todas las tuplas
print(mayusculas) #se hace el print a lista donde guardador los nombre en mayucula

baratas = [ nombre for nombre, precio, cantidad in frutas if precio < 0.50] #se crea una lista con las frutas que sean menor a 0.50
print(baratas)  #se hace el print a lista donde se guardaron las frutas

cantidad = max(frutas, key=lambda fruta: fruta[2]) #se max junto con una función lambda para traer la tupla que contiene la fruta con mayor cantidad
print(cantidad)  #print a la lista cantidad                #La clave de la función lambda es el (2=tercero) de cada tupla

frutas.sort (key=lambda fruta: fruta[1] * fruta[2],reverse=True) #ordena la lista frutas en orden descendente según el valor de (precio * cantidad)
print(frutas)  #print a la lista frutas ordenadas          #La clave de la función lambda es el (1=tercero)*(2=tercero) de cada tupla

#Hecho por Jaime Barrera cc 1093925253