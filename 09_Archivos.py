#archivos con notas.txt se pueden abrir mañana , leer etc..
# "r"
# read
# leer
# el archivo debe existir 
# "w"
# write
# escribir 
# crea o reemplaza
# "a"
# append
# agregar
# conserva y suma al final 

# archivo=open("saludo.txt")
# contenido= archivo.read()
# print(contenido)
# archivo.close()

# with open("saludo.txt", "r") as archivo: # cierra el archivo al salir de su identacion 
#     texto= archivo.read()
# print(texto)


# with open("datos.txt", "w")as archivo: # este crea y sobreescribe archivos
#     archivo.write("ana")
# with open("datos.txt", "r") as archivo:
#     texto= archivo.read()
# print(texto)


#para agregar uso "a" append

# with open("registro.txt", "w")as archivo:
#     archivo.write("ana\n")
# with open("registro.txt","a")as archivo:
#     archivo.write("luis\n")
#     archivo.write("carlos\n") # el \ es para el salto de linea 
# with open("registro.txt", "r") as archivo:
#     leer=archivo.read()
# print(leer)

# with open("registro.txt", "r") as archivo:
#     for linea in archivo:
#         print(linea.strip()) #elimina saltos de linea y espacios
# print("final")



# with open("edades.txt", "w")as archivo:
#     archivo.write("20\n")
#     archivo.write("25\n")
#     archivo.write("30\n")
# with open("edades.txt", "r") as archivo:
#     for linea in archivo:
#         edad= int(linea.strip())
#         print(edad + 5)
# print("final")


#read() lee todo como un solo string 
#readline() lee una linea cada vez
#readlines() devuelve una lista de lineas

# with open("registro.txt","r")as archivo:
#     datos= archivo.readlines()
# print(datos[1].strip())


# productos=["mouse","teclado","monitor"]
# with open("productos.txt","w")as archivo:
#     for producto in productos:
#         archivo.write(producto+"\n")

#write lines() no agrega saltos de linea por si solo

# nombres=["ana\n","luis\n","carlos\n"] # se escribe de esta manera para que lo imprima verticalmente

# with open("nombres.txt","w")as archivo:
#     archivo.writelines(nombres)


# productos=[
#     {"nombre": "mouse", "precio": 50000, "cantidad": 5},
#     {"nombre": "teclado", "precio": 80000, "cantidad": 3}
# ]

# with open("productos.txt","w")as archivo:
#     for producto in productos:
#         archivo.write(producto["nombre"] + "," +
#                       str(producto["precio"])+ "," +
#                       str(producto["cantidad"])+ "\n")


#split() divide un texto segun un separador


# linea= "teclado,80000,3"
# datos= linea.strip().split(",")
# nombre= datos[0]
# precio= int(datos[1])
# cantidad = int(datos[2])
# total= precio*cantidad
# print(total)
