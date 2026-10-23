# equipos= []
# with open("equipos.txt", "w") as archivo:
#     for i in range(4):
#         print(f"\nRegistro del equipo {i+1} ")
#         nombre = input("Ingrese el nombre del equipo: ")
#         cantidad = input("Ingrese la cantidad disponible: ")
#         valor_unitario = input("Ingrese el valor unitario: ")
#         archivo.write(f"{nombre},{cantidad}, {valor_unitario} \n")
# total_equipos = 0

# print("\n calculando el valor de los equipos ")

# with open("equipos.txt", "r") as archivo:
#     for linea in archivo:
#         datos = linea.strip().split(",")
#         nombre = datos[0]
#         cantidad = int(datos[1])
#         valor_unitario = float(datos[2])
#         valor_total = cantidad * valor_unitario
#         print(f"{nombre}: Su valor total es de: {valor_total}")
#         total_equipos += valor_total
#         equipo = {
#             "nombre": nombre,
#             "cantidad": cantidad,
#             "valor_unitario": valor_unitario,
#             "valor_total": valor_total
#         }
#         equipos.append(equipo)

# print("\n--- Equipos con un valor total superior a $2.000.000 ---")
# for equipo in equipos:
#     if equipo["valor_total"] > 2000000:
#         print(f"- {equipo['nombre']}: valor total de: {equipo['valor_total']}")
# print(f"\n el valor total de todos los equipos registrados es: {total_equipos}")


class Dispositivo:
    def __init__(self, nombre, marca, precio):
        self.nombre = nombre
        self.marca = marca
        self.precio =precio
    def mostrar_informacion(self):
        return f"Dispositivo: {self.nombre} Marca: {self.marca} Precio: {self.precio}"
   
    def calcular_descuento(self, porcentaje):
        descuento = self.precio * porcentaje
        return self.precio - descuento

class Computador(Dispositivo):
    def __init__(self, nombre, marca, precio, memoria_ram, estado):
        super().__init__(nombre, marca, precio)
        self.memoria_ram = int(memoria_ram)
        if estado == "Disponible" or estado == "Prestado":
            self.__estado = estado
        else:
            self.__estado = "Disponible"
    def cambiar_estado(self, nuevo_estado):
        if nuevo_estado == "Disponible" or nuevo_estado == "Prestado":
            self.__estado = nuevo_estado
            print(f"El Estado a cambiado a: '{nuevo_estado}")
        else:
            print(f"Error: El estado: '{nuevo_estado}' no es válido. Solo acepta 'Disponible' o 'Prestado'.")
    def consultar_estado(self):
        return self.__estado
        
    def mostrar_informacion_computador(self):
        info_basica = self.mostrar_informacion()
        return f"{info_basica} RAM: {self.memoria_ram}GB Estado: {self.__estado}"
        
    def verificar_ram(self):
        if self.memoria_ram >= 16:
            return "El equipo posee 16 GB de memoria RAM o más."
        else:
            return "El equipo posee menos de 16 GB de memoria RAM."


# PRUEBAS
print("\n--- Creación de objetos ---")
compu1 = Computador("Portatil", "Lenovo", 3500000, 16, "Disponible")
compu2 = Computador("PC Escritorio", "HP", 1800000, 8, "Prestado")

print(compu1.mostrar_informacion_computador())
print(compu1.verificar_ram())
print(compu2.mostrar_informacion_computador())
print(compu2.verificar_ram())

print("\n Cambio de estado correcto")
compu1.cambiar_estado("Prestado")
print(f"El nuevo estado del {compu1.nombre} es: {compu1.consultar_estado()}")

print("\nIntento de cambio de estado incorrecto")
compu2.cambiar_estado("En reparación")
print(f"El estado actual del {compu2.nombre} se mantiene como: {compu2.consultar_estado()}")

print("\n Su descuento es de : ")
descuento_aplicado = 0.10
precio_final = compu1.calcular_descuento(descuento_aplicado)
print(f"El precio del {compu1.nombre} aplicando un descuento del 10% es de: {precio_final}")