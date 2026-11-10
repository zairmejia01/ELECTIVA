import serial 
from time import sleep

puerto = serial.Serial("COM10", 115200, timeout=3) 
sleep(3) # Pausa el programa por 3 segundos para dar tiempo a que se establezca la conexion con el ESP32.

puerto.reset_input_buffer() 
while True:
    dato = puerto.readline().decode().strip() 
    
    if dato: 
        distancia = float(dato) 
        print("Distancia recibida: ", distancia, "cm") # Muestra la distancia recibida en la consola de Python