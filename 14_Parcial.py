# with open("producto.txt", "w") as archivo:
#     for i in range(3):
#         print(f"\nRegistro del producto {i+1}")
#         nombre = input("Ingrese el nombre del producto: ")
#         cantidad = input("Ingrese la cantidad: ")
#         precio_unitario = input("Ingrese el precio unitario: ")        
#         archivo.write(f"{nombre},{cantidad},{precio_unitario}\n")
# total_general = 0

# print("\nValores Totales")
# with open("producto.txt", "r") as archivo:
#     for linea in archivo:
#         datos = linea.strip().split(",")
#         nombre = datos[0]
#         cantidad = int(datos[1])
#         precio_unitario = float(datos[2])
#         valor_total = cantidad * precio_unitario
#         print(f" {nombre}: Valor total = ${valor_total:,.2f}")
#         total_general += valor_total
# print(f"\nEl valor total de todos los productos registrados es: ${total_general:,.2f}")

class Dispositivo:
    def __init__(self, nombre, marca, precio):
        self.nombre = nombre
        self.marca = marca
        self.precio = precio
        
    def mostrar_informacion(self):
        return f"Dispositivo: {self.nombre} | Marca: {self.marca} | Precio: ${self.precio}"
   
    def calcular_descuento(self, porcentaje):
        descuento = self.precio * porcentaje
        return self.precio - descuento

class Sensor(Dispositivo):
    def __init__(self, nombre, marca, precio, tipo, unidad, estado):
        super().__init__(nombre, marca, precio)
        self.tipo = tipo
        self.unidad = unidad
        
        if estado == "activo" or estado == "inactivo":
            self.__estado = estado
        else:
            self.__estado = "inactivo"
            
    def consultar_estado(self):
        return self.__estado
        
    def cambiar_estado(self, nuevo_estado):
        if nuevo_estado == "activo" or nuevo_estado == "inactivo":
            self.__estado = nuevo_estado
            print(f"El estado ha cambiado a: '{self.__estado}")
        else:
            print(f"Error: El estado '{nuevo_estado}' no es válido. Solo acepta 'activo' o 'inactivo'.[cite: 5]")
    def mostrar_informacion_sensor(self):
        info_basica = self.mostrar_informacion()
        return f"{info_basica}Tipo: {self.tipo}Unidad: {self.unidad}Estado: {self.__estado}"
        
    def comprobar_limite(self, lectura, limite):
        if lectura > limite:
            print(f"La lectura de {lectura}{self.unidad} SUPERA el límite de {limite}{self.unidad}.")
            return True
        else:
            print(f"La lectura de {lectura}{self.unidad} está dentro del límite de {limite}{self.unidad}.")
            return False

# PRUEBAS
print("\nCreación de objetos e información")
sensor1 = Sensor("sensor de temperatura", "Rubianos", 8000, "activo")
sensor2 = Sensor("Sensor de proximidad", "Sejel", 12000, "inactivo")

print(sensor1.mostrar_informacion_sensor())
print(sensor2.mostrar_informacion_sensor())

print("\nCambio de estado correcto")
sensor1.cambiar_estado("inactivo")
print(f"El nuevo estado del {sensor1.nombre} es: {sensor1.consultar_estado()}")

print("\nIntento de cambio de estado incorrecto")
sensor2.cambiar_estado("dañado")
print(f"El estado actual del {sensor2.nombre} se mantiene como: {sensor2.consultar_estado()}")

print("\nAplicar descuento")
descuento_aplicado = 0.15 
precio_final = sensor2.calcular_descuento(descuento_aplicado)
print(f"El precio del {sensor2.nombre} aplicando un descuento del 15% es de:{precio_final}")

print("\nComprobacion de limites")
sensor1.comprobar_limite(35, 40) 
sensor2.comprobar_limite(120, 150) 
