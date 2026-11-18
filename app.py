
import streamlit as st
import pandas as pd
import joblib

# Configuración de la página
st.set_page_config(
    page_title="BikeDemand AI",
    page_icon="🚲",
    layout="centered"
)

# Cargar el modelo entrenado
modelo = joblib.load("models/bike_demand_tree.joblib")

# Título
st.title("🚲 BikeDemand AI")
st.subheader("Predicción de demanda de alquiler de bicicletas")

st.write(
    "Ingresa las condiciones de una hora para estimar "
    "cuántas bicicletas podrían alquilarse."
)

st.info(
    "Esta aplicación utiliza un modelo de Árboles de Decisión "
    "entrenado con datos históricos de alquiler de bicicletas."
)

# Datos de entrada
st.header("Condiciones de la predicción")

col1, col2 = st.columns(2)

with col1:
    season = st.selectbox(
        "Temporada",
        [1, 2, 3, 4],
        format_func=lambda x: {
            1: "Primavera",
            2: "Verano",
            3: "Otoño",
            4: "Invierno"
        }[x]
    )

    year = st.selectbox("Año", [0, 1],
                        format_func=lambda x: 2011 if x == 0 else 2012)

    month = st.selectbox("Mes", list(range(1, 13)))

    hour = st.slider("Hora del día", 0, 23, 8)

    holiday = st.selectbox("¿Es día festivo?", [0, 1],
                           format_func=lambda x: "No" if x == 0 else "Sí")

    weekday = st.selectbox("Día de la semana", list(range(7)),
                           format_func=lambda x: [
                               "Domingo", "Lunes", "Martes",
                               "Miércoles", "Jueves", "Viernes",
                               "Sábado"
                           ][x])

with col2:
    workingday = st.selectbox(
        "¿Es día laboral?",
        [0, 1],
        format_func=lambda x: "No" if x == 0 else "Sí"
    )

    weathersit = st.selectbox(
        "Condición climática",
        [1, 2, 3, 4],
        format_func=lambda x: {
            1: "Despejado o parcialmente nublado",
            2: "Niebla o nublado",
            3: "Lluvia o nieve ligera",
            4: "Lluvia o nieve intensa"
        }[x]
    )

    temp = st.slider("Temperatura (escala normalizada)", 0.0, 1.0, 0.5)

    atemp = st.slider("Sensación térmica (escala normalizada)", 0.0, 1.0, 0.5)

    hum = st.slider("Humedad (escala normalizada)", 0.0, 1.0, 0.5)

    windspeed = st.slider("Velocidad del viento (escala normalizada)", 0.0, 1.0, 0.2)

# Realizar predicción
if st.button("Predecir demanda", type="primary"):

    datos = pd.DataFrame([{
        "season": season,
        "yr": year,
        "mnth": month,
        "hr": hour,
        "holiday": holiday,
        "weekday": weekday,
        "workingday": workingday,
        "weathersit": weathersit,
        "temp": temp,
        "atemp": atemp,
        "hum": hum,
        "windspeed": windspeed
    }])

    prediccion = modelo.predict(datos)[0]

    st.success(
        f"Demanda estimada: {max(0, round(prediccion))} bicicletas"
    )

    st.caption(
        "Esta cifra es una estimación del modelo y no garantiza "
        "la cantidad real de alquileres."
    )
