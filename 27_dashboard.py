import streamlit as st
st.title("analisis de distancias")
st.write("bienvenido al primer dashboard")

distancia = st.slider("seleccione una distancia en cm",0,50,20)
st.write("distancia seleccionada",distancia)

if distancia< 20:
    st.write("objeto cerca")
else:
    st.write("distancia segura")

import pandas as pd
datos= {
    "medicion"[1,2,3,4,5,6,7,8],
    "distancia"[15,18,22,12,30,25,10,20]
}

tabla= pd.DataFrame(datos)
st.subheader("registro de mediciones")
st.dataframe(tabla)

st.subheader("grafica de distancias")

st.line_chart(tabla, x="medicion", y="distancia")
tabla["distancia ajustada"]=tabla["distancia"]+2




















