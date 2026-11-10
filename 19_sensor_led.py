from machine import Pin, time_pulse_us
from time import sleep, sleep_us  
import select

trig = Pin(18, Pin.OUT) 
echo = Pin(19, Pin.IN) 
led = Pin(23, Pin.OUT) 

led.value(0) 

while True:
    trig.value(0) 
    sleep_us(2) 
    
    trig.value(1)
    sleep_us(10) 
    trig.value(0) 
    
    tiempo = time_pulse_us(echo, 1, 30000) 

    if tiempo > 0:
        distancia = tiempo / 58 
        print(round(distancia, 1)) 
        
    if select.select([sys.stdin], [], [], 0.0)[0]: 
        mensaje = sys.stdin.readline().strip() 


        if mensaje == "ENCENDER": 
            led.value(1) 
            
        if mensaje == "APAGAR": 
            led.value(0.5) 