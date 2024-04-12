

def cantidadBilletes(cantidad, billetes, resultado):
    if cantidad > 0 and len(billetes) > 0:
        maximoBilletes = max(billetes)
        if cantidad - maximoBilletes >= 0:
            if "billete" + str(maximoBilletes) not in resultado:
                resultado["billete" + str(maximoBilletes)] = 1
            else:
                resultado["billete" + str(maximoBilletes)] += 1
            cantidad = cantidad - maximoBilletes
        else:
            billetes.remove(maximoBilletes)
        return cantidadBilletes(cantidad, billetes, resultado)
    else:
        return resultado

cant = int(input("Ingresa el numero: "))
billetes = [1, 5, 10]

# Llama a la función y muestra el resultado
resultado_final = cantidadBilletes(cant, billetes, {})
print(resultado_final)
# hecho por Jaime_Barrera cc:  1.093.925.253