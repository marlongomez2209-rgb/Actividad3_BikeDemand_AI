
# BikeDemand AI – Predicción de demanda de alquiler de bicicletas

## Descripción del proyecto

BikeDemand AI es un proyecto de Machine Learning que busca predecir la cantidad de bicicletas que pueden alquilarse durante una hora determinada, utilizando información histórica relacionada con la fecha, la hora y las condiciones climáticas.

El proyecto está orientado a apoyar a los encargados de negocios de alquiler de bicicletas en la planificación de sus recursos.

## Objetivo general

Desarrollar un modelo de aprendizaje automático basado en árboles de decisión que permita estimar la demanda horaria de alquiler de bicicletas a partir de variables temporales y climáticas.

## Conjunto de datos

Se utilizó el Bike Sharing Dataset, obtenido del repositorio UCI Machine Learning Repository.

- Registros: 17.379.
- Archivo utilizado: hour.csv.
- Ubicación de los datos: Washington D. C.
- Periodo: 2011–2012.

Fuente: https://archive.ics.uci.edu/dataset/275/bike+sharing+dataset

## Algoritmo utilizado

- Algoritmo: Árboles de decisión (Decision Tree).
- Tipo de aprendizaje: Supervisado.
- Tipo de problema: Regresión.
- Biblioteca: Scikit-learn.

## Resultados de evaluación

El modelo fue evaluado utilizando un conjunto de prueba equivalente al 20 % de los datos.

| Métrica | Resultado |
|---|---:|
| MAE | 45.25 |
| RMSE | 72.14 |
| R² | 0.8356 |

El modelo explica aproximadamente el 83.56 % de la variabilidad de la demanda en los datos de prueba.

## Estructura del proyecto

- `app.py`: código de la aplicación web.
- `models/`: carpeta que contiene el modelo entrenado.
- `requirements.txt`: bibliotecas necesarias para ejecutar la aplicación.
- `README.md`: documentación del proyecto.
- `notebooks/`: espacio destinado al cuaderno de entrenamiento.

## Tecnologías utilizadas

- Python
- Google Colab
- Pandas
- Scikit-learn
- Joblib
- Streamlit
- GitHub

## Estado del proyecto

Primera versión del modelo entrenada, evaluada y serializada. La aplicación web se encuentra en preparación para su despliegue.

