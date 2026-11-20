import pandas as pd
datos= {
    "medicion":[1,2,3,4,5],
    "distancia":[15,18,22,12,30]
}
tabla_datos= pd.DataFrame(datos)
# print(tabla_datos)

# print(tabla_datos["distancia"])
# promedio = tabla_datos["distancia"].mean()
# print(promedio)
# dis_max= tabla_datos["distancia"].max()
# print(dis_max)
# tem_altas= tabla_datos[tabla_datos["distancia"]>= 20]
# print(tem_altas)
# tabla_datos["distancia doble"]= tabla_datos["distancia"]*2
# print(tabla_datos)


tabla_datos.to_csv("distancias.csv",index=False)