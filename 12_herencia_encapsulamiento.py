#HERENCIA Y ENCAPSULAMIENTO 

#Pass Permite ejecutar sin necesidad de tener codigo dentro de esa clase

# class Persona:
#     def __init__(self,nombre):
#         self.nombre = nombre
        
#     def saludar(self):
#         return f"Hola, soy{self.nombre}"

# class Estudiante(Persona):# En esta clase la clase padre debe estar en parentesis
#     estudiante1 = Estudiante("Pepito")
#     print(estudiante1.saludar())
# pass

#Persona tiene constructor y tiene el metodo saludar()
# Estudiante no agrega nada nuevo, Pero Hereda lo de la persona. 


# Para que sirve super()

#super() permite ejecutar el constructor o los metodos de la clase padre 

class Persona: # ESTA CLASE PADRE INICIALIZA NOMBRE Y EDAD 
    def __init__(self,nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
# class Estudiante(Persona): #ESTA CLASE HIJA REUTILIZA LO ANTERIOR Y AGREGA CARRERA
#     def __init__(self, nombre, edad, carrera):
#         super().__init__(nombre, edad)
#         self.carrera = carrera 
# estudiante1 = Estudiante("Pepito", "12", "Licenciatura en matematicas")     
# print(estudiante1.saludar())       
# #super() evita repetir self.nombre = nombre y self.edad = edad. 


#ATRIBUTOS HEREDADOS Y PROPIOS
# La clase hija puede conservar lo heredado y agregar informacion nueva

# class Estudiante(Persona):
#     def __init__(self, nombre, edad, carrera, nota):
#         super().__init__(nombre, edad)
#         self.carrera = carrera 
#         self.__nota = nota
# estudiante1 = Estudiante("Luis", 34, "  Lic. Tecnologia, 4.5")
# print(estudiante1.saludar)


# # HERERDAR METODOS HEREDADOS Y METODOS PROPIOS
# # Un objeto de clase hija puede usar metodos heredados y metodos definidos en la hija 

# estudiante1.presentarse()
# #Metodo heredado de Persona

# estudiante1.mostrar_nota()
# #Metodo propio de Estudiante 

# estudiante1.obtener_estado()
# # Metodo Propio de Estudiante


# class persona:
#     def presentarse(self):
#         return"soy una persona"
# class estudiante(persona):
#     def presentarse(self):
#         return "soy un estudiante"


# #ENCAPSULAMIENTO (encapsular como se accede y como se modifica el estado interno del objeto )


# class Estudiante:
#     def __init__(self, nota):
#         self.__nota = nota
#     def mostrar_nota (self):
#         return self.__nota

# _atributo y __atributo
# no son exactamete lo mismo Representan niveles diferentes de proteccion o intencion 

# class Sensor:
#     def __init__(self):
#         self.__ubicacion = "Sala"
#         self.__temperatura = 25
  #_ubicacion es interno por convencion
  #__temperatura se controla desde metodos 

  
# class Estudiante:
#     def __init__(self, nota):
#         self.__nota = nota
#     def mostrar_nota(self):
#         return self.__nota
#     def cambiar_nota(self, nueva_nota):
#         if 0<= nueva_nota <= 5:
#             self.__nota = nueva_nota
#     def obtener_estado(self):
#         if self.__nota >= 3:
#             return f"Aprobado con : {self.__nota}"
#         else:
#             return f"Reprobado con : {self.__nota}"

# estudiante1= Estudiante(4.5)
# print(estudiante1. mostrar_nota())

# estudiante1.cambiar_nota(3.8)
# print(estudiante1.mostrar_nota())

# estudiante1.cambiar_nota(7)
# print(estudiante1.mostrar_nota())

# print(estudiante1.obtener_estado())

# ##############################


# Dos objetos, estados diferentes
# Ambos objetos son estudiante pero cada uno conserva su informacion


# estudiante1 = Estudiante("Luis", 34, "lic. tecnologia", 4.5)
# estudiante2 = Estudiante("pedro", 25, "lic. tecnologia", 2.8)

# print(estudiante1.obtener_estado())
# print(estudiante2.obtener_estado())

# class Cuenta:
#     def __init__(self, titular,saldo):
#         self.titular= titular
#         self.__saldo = saldo
#     def cosultar_saldo(self):
#         return self.__saldo
#     def depositar(self,cantidad):
#         if cantidad > 0:
#             self.__saldo += cantidad

##########################

#ACTIVIDAD construye el sistema persona -> Estudiante y prueba dos objetos

class Persona:
    def __init__(self, nombre,edad):
        self.nombre= nombre
        self.edad= edad
    def presentarse(self):
        return f"BIENVENIDO: , {self.nombre},{self.edad}"
class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera, nota):
        super().__init__(nombre, edad)
        self.carrera=carrera
        self.__nota=nota
        
    def mostrar_nota(self):
        return self.__nota
    
    def cambiar_nota(self, nueva_nota):
        if 0<=nueva_nota<=5:
            self.__nota=nueva_nota
    
    def obtener_estado(self):
        if self.__nota>=3:
           return f"Aprobado con: {self.__nota}"
        else:
            return f"Reprobado con: {self.__nota}"
        
estudiante1=Estudiante("juan", 22,"Lic. Tecnologia", 4.5)
estudiante2=Estudiante("Pedro", 25, "Lic. Tecnologia",1.5)

print(estudiante1.mostrar_nota())
print(estudiante1.obtener_estado())
estudiante1.cambiar_nota(6)
print(estudiante1.obtener_estado())
print(estudiante2.mostrar_nota())
print(estudiante2.obtener_estado())









