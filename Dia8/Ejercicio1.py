SUBSCRIPTION_PRICE = 50

class PYTimesUser:
    def __init__(self, nombre, subscription_price=SUBSCRIPTION_PRICE):
        self.nombre = nombre
        self.subscription_price = subscription_price
        self.suscripciones = []
        self.cantidad = 0

    def agregar_suscripcion(self, año):

        self.suscripciones.append(año)

    def suscribirse(self, año):

        if self.cantidad >= self.subscription_price:
            self.cantidad -= self.subscription_price
            self.agregar_suscripcion(año)
        else:
            print(f"No hay suficiente dinero ({self.cantidad}) para suscribirse en {año}.")

    def depositar(self, monto):
       
        self.cantidad += monto

    def comprar_suscripcion_regalo(self, otro_usuario, año):
       
        if self.cantidad >= otro_usuario.subscription_price:
            self.cantidad -= otro_usuario.subscription_price
            otro_usuario.agregar_suscripcion(año)
            print(f"{self.nombre} compró una suscripción de regalo para {otro_usuario.nombre} para {año}")
        else:
            print(f"No hay suficiente dinero({self.cantidad}) para comprar una suscripción de regalo para {otro_usuario.nombre}.")

    def obtener_precio_suscripcion(self):
        
        return self.subscription_price

    def obtener_nombre(self):
        
        return self.nombre
    
nombre = input("Ingresa tu nombre: ") # Solicitar al usuario el nombre y crear un objeto PYTimesUser
usu = PYTimesUser(nombre)

monto = int(input(f"Hola {usu.obtener_nombre()}, ingresa el dinero: "))# guarda dinero en la cuenta del usuario
usu.depositar(monto)

año = int(input("Ingresa el año al que deseas suscribirte: "))# Suscribirse a un año
usu.suscribirse(año)

nombre_otro = input("Ingresa el nombre al que deseas regalarle una suscripción: ")# Crear otro nombre para comprar una suscripción de regalo
otro_usuario = PYTimesUser(nombre_otro)

año_regalo = int(input(f"Ingresa el año para la suscripción de regalo de {otro_usuario.obtener_nombre()}: ")) # Comprar una suscripción de regalo
usu.comprar_suscripcion_regalo(otro_usuario, año_regalo)

print(f"Tu suscripcion, {usu.obtener_nombre()}: {usu.suscripciones}")# Imprime la suscripcion

print(f"Suscripcion de {otro_usuario.obtener_nombre()}: {otro_usuario.suscripciones}")# Imprime la suscripciones de regalo

#Hecho por Jaime Barrera cc 1093925253