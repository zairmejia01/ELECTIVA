import serial 
from time import sleep 
puerto = serial.Serial("COM10", 115200, timeout=3) 

sleep(3) 
puerto.reset_input_buffer() 

while True:
    dato = puerto.readline().decode().strip() 
    
    try: 
        distancia = float(dato) 
        print("Distancia: ", distancia, " cm") 
        
        if distancia < 10: 
            puerto.write(b'ENCENDER\n') 
        else: 
            puerto.write(b'APAGAR\n') 
    except ValueError: # Si ocurre un error al convertir el dato a float (por ejemplo, si el dato no es un numero valido)
        pass 