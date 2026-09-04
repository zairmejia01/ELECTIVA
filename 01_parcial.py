# PUNTO 1
# edad=int (input("ingrese su edad "))
# if edad>=18:
#     print("mayor de edad")
# else:
#     print("menor de edad")
#(EL PROBLEMA ES QUE LA VARIABLE QUE SE ESTA SOLICITANDO LE HACIA FALTA COLOCAR "INT" PARA QUE LO LEYERA COMO NUMERO Y NO SOLAMENTE COMO STR)


#1B

# nota=float(input("ingrese la nota"))
# if nota>=4.5:
#     print("desempeño superior")
# elif nota>=3.0:
#     print("aprobado")
# else:
#     print("no aprobado")
#(LA SOLUCION QUE NECESITA ES SOLAMENTE CAMBIAR EL SEGUNDO "elif" PARA QUE CUANDO NO SE CUPLA EL PRIMER "if" SALTE DIRECTAMENTE AL OTRO )

#PUNTO 2
nota= float(input("digite su nota por favor "))
if nota<0 or nota>5:
   print("Nota no valida")
elif nota<3:
   print("no aprobado")
elif nota<4:
   print(" desempeño basico")
elif nota<4.6:
   print("Desempeño Alto")
else :
   print("desempeño superoir")