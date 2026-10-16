# class producto:
#     def __init__(self,nombre,cantidad):
#         self.nombre= nombre
#         self.cantidad= cantidad 
#     def agregar_stock(self, unidades):
#         self.cantidad += unidades

# celular= producto("celular", 2)
# zapatos= producto("zapatos", 1)
# medias= producto("medias", 4)
# chaquetas= producto("chaquetas", 3)
# celular.agregar_stock(4)
# zapatos.agregar_stock(4)
# medias.agregar_stock(4)
# chaquetas.agregar_stock(4)
# print(celular.cantidad,zapatos.cantidad,medias.cantidad,chaquetas.cantidad)


#ATRIBUTOS VS PARAMETROS DE METODO " NO TODOO DATO USADO  POR UN METODO DEBE GRUARDARSE COMO UN PARAMETRO"

# class producto:
#     def __init__(self,nombre,precio):
#         self.nombre= nombre
#         self.precio= precio
#     def agregar_stock(self, unidades):
#         self.precio += unidades
#     def calcular_total(self, cantidad):
#         return self.precio * cantidad

# celular= producto("celular", 20000)
# teclado= producto("teclado", 35000)
# mouse= producto("mouse", 5000)
# monitor= producto("monitor", 23000)
# mouse.calcular_total(5)
# print(mouse.calcular_total(7))


#######
#DICCIONARIO VS OBJETO

# producto={
#     "nombre":"mouse"
#     "precio": 50000
# }
# print(producto["precio"])


# class producto:
#     def __init__(self,nombre,precio,cantidad):  # lo que esta dentro de los parantesis son los parametros 
#         self.nombre= nombre # self.cantidad self.precio self.nombre estos son atributos
#         self.precio= precio
#         self.cantidad= cantidad
#     def mostrar_datos(self): # todos los def son metodos
#         return f"{self.nombre}-{self.precio}-{self.cantidad}"
#     def calcular_total(self):
#         return self.precio * self.cantidad
# # AHORA VAMOS A CREAR LOS OBJETOS 
# celular=producto("celular",10000, 3 )
# teclado=producto("teclado",80000, 2 )
# monitor=producto("monitor",700000, 1 )

# print(celular.mostrar_datos())
# print(celular.calcular_total())


class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    def retirar(self,cantidad):
        if cantidad > 0 and cantidad <= self.saldo:
            self.saldo -= cantidad
        elif cantidad > self.saldo:
            print("SALDO INSUFICIENTE , DIGITE OTRO VALOR")
        else:
            print("EL VALOR DEBE SER POSITIVA ")
    def consultar_saldo(self):
        return self.saldo
    def mostrar_datos(self):
        return f"Titular: {self.titular} - Saldo actual: ${self.saldo}"
    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
        else:
            print("El depósito debe ser un valor positivo.")
            
cuenta1 = CuentaBancaria("Carlos", 100000)
cuenta2 = CuentaBancaria("Ana", 50000)
cuenta1.depositar(50000)
cuenta1.retirar(30000)
cuenta2.retirar(60000)
print(cuenta1.mostrar_datos())
print(cuenta2.mostrar_datos())




















































