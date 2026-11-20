import pandas as pd
import matplotlib.pyplot as plt

tabla= pd.read_csv("distancias.csv")

# plt.plot(tabla["medicion"], tabla["distancia"])# hace una grafica de lineas
plt.bar(tabla["medicion"], tabla["distancia"])# hace una grafica de barras
plt.xlabel("medicion")
plt.ylabel("distancia")
plt.title("distancias medidas por el HC-SR04")

plt.show()