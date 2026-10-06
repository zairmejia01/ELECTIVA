#Continuacion segunda parte 
# productos =
# [
#     {"nombre": "mouse", "precio": 50000, "cantidad": 5},
#     {"nombre": "teclado", "precio": 80000, "cantidad": 3}
#     {"nombre": "teclado", "precio": 700000, "cantidad": 2}
# ]

# with open("productos.txt","w")as archivo:
#     for producto in productos:
#         archivo.write(producto["nombre"] + "," +
#                       str(producto["precio"])+ "," +
#                       str(producto["cantidad"])+ "\n")

# linea= "teclado,80000,3"
# datos= linea.strip().split(",")
# nombre= datos[0]
# precio= int(datos[1])
# cantidad = int(datos[2])
# total= precio*cantidad
# print(total)


# with open("productos.txt","r")as archivo:
#     for linea in archivo:
#         datos=linea.sprit().split(",")
#     producto = { 
#         "nombre": datos[0]
#         "precio" :int(datos[1]),
#         "cantidad":int(datos[2])
#   }
# productos.append(producto)
# print (productos)


# NUEVOS EJEMPLOS

# with open("estudiantes.txt","w") as archivo:
#     for i in range(3):
#         nombre=input ("INGRESE EL NOMBRE DEL ESTUDIANTE")
#         edad= int (input("ingrese la edad del estudiante"))
#         archivo.write(nombre +"," + str (edad) +"\n")
# estudiantes=[]
# with open("estudiantes.txt","r")as archivo:
#     for linea in archivo:
#         datos= linea.strip().split(",")
#         estudiante = { 
#         "nombre": datos[0],
#         "edad" :int(datos[1])
#   }
#     estudiantes.append(estudiante)
# print (estudiantes)



# PROGRAMACION ORIENTADA A OBJETOS (POO)

# # pass no ejecuta nado solo nos permite pasar un bloque de codigo o ejecutarlo en este caso
# class producto:
#     pass
# mouse= producto()
# teclado=producto()
# print(type(mouse))

# __init__ se ejecuta automaticamente cuando creamos un objeto
# self representa al objeto que esta usando el metodo en ese momento
# el self no es un fo no recorre  


# class producto:
#     def __init__ (self, nombre, precio):
#      self.nombre= nombre
#      self.precio= precio
     
# mouse = producto("mouse",50000)

# class producto:
#     def __init__ (self, nombre, precio, cantidad):
#      self.nombre= nombre
#      self.precio= precio
#      self.cantidad= cantidad
# mouse = producto("mouse",50000,2)
# teclado= producto("teclado",80000,3)
# print(teclado)


class producto:
    def __init__(self,nombre,precio):
        self.nombre= nombre
        self.precio= precio

    def mostrar_precio(self):
        print(self.nombre, self.precio)

mouse = producto("mouse",50000)
mouse.mostrar_precio()










