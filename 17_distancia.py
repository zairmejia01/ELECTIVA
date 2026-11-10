# from machine import Pin, time_pulse_us
# from time import sleep, sleep_us

# trig= Pin(18,Pin.OUT )
# echo = Pin(19,Pin.IN)

# while True:
#     trig.value(0)
#     sleep_us(2)

#     trig.value(1)
#     sleep_us(10)
#     trig.value(0)

#     tiempo= time_pulse_us(echo,1, 30000)
#     if tiempo > 0:
#         distancia= tiempo/58
#         print(round(distancia,1))
#     else:
#         print("sin medicion valida")
#     sleep(1)