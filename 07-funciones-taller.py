# def saludar (): # Define 
#     print("Hola")
# saludar() # Ejecuta 

# def presentar(nombre, edad):
#     print("Nombre:", nombre)
#     print("Edad:", edad)
# presentar("Laura", 22)

# return devuelve

# def sumar(a,b):
#     print(a+b)
# resultado=sumar(5,3)
# print(resultado)

# def sumar(a,b):
#     return(a+b)
# resultado=sumar(5,3)
# print(resultado)

# por que return es tan util : porque el resultaod se puede resutilizar 
# def multiplicar (a,b):
#     return a*b
# resultado= multiplicar (4,5)+10
# print(resultado)

# def calcular_promedio(notas):
#     suma=0
#     for nota in notas:
#         suma += nota
#     return suma/ len(notas)
# notas_ana=[4.0,3.5,5.0]
# promedio=calcular_promedio(notas_ana)
# print(round(promedio,2))

# def calcular():
#     resultado= 20
#     print (resultado)
# calcular()
# print(resultado)

# nombre = "Laura"

# def saludar():
#     print(nombre)
# saludar()

# contador=10
# def aumentar():
#     contador=contador +1
#     print(contador)
# aumentar()

# def aumentar (numero):
#     return numero +1
# contador=10
# contador= aumentar (contador)
# print(contador)

#INTEGRADOR:FUNCION + DICCIONARIO

# def calcular_total(precio,cantidad):
#     return precio*cantidad
# producto={
#     "nombre":"teclado",
#     "precio": 80000,
#     "cantidad": 3
# }
# producto["total"]= calcular_total(
#     producto["precio"],
#     producto["cantidad"]
# )
# print(producto)

#CORREGIR CODIGO
#PUNTOS
# def sumar_puntos():
#     puntos=puntos + 10 
#     print(puntos)
# sumar_puntos()

#codigo CORREGIDO

# puntos=5
# def sumar_puntos(puntos_actuales):
#     return puntos +10
# puntos= sumar_puntos(puntos)
# print(puntos)

#TALLER de clase
def calcular_promedio(notas):
    return sum(notas) / len(notas)
estudiantes=[
    {"nombre":"ana","notas":[4.0,3.5,5.0]},
    {"nombre":"luis","notas":[2.5,3.0,2.8]},
    {"nombre":"carlos","notas":[4.5,4.0,4.8]}
]

for estudiante in estudiantes:
    promedio = calcular_promedio(estudiante["notas"])
    promedio_redondeado = round(promedio, 2)
    estudiante["promedio"] = promedio_redondeado
    if promedio_redondeado >= 3.0:
        estudiante["estado"] = "Aprobado"
    else:
        estudiante["estado"] = "Reprobado"
# print("luis")
# print(estudiantes[1])

print("RESULTADOS FINALES")
for estudiante in estudiantes:
    print(estudiante)

