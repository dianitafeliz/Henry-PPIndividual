#IMPORTS
from http.client import HTTPException
import pandas as pd
import numpy as np
import json
import matplotlib.pyplot as plt
import seaborn as sns
from fastapi import FastAPI
app = FastAPI()

#df_movies = pd.read_pickle(r'C:\HENRY\PROYECTOS HENRY 11\Primer Proyecto Individual\Datasets\df_movies.pkl')
#df_credits = pd.read_parquet(r'C:\HENRY\PROYECTOS HENRY 11\Primer Proyecto Individual\Datasets\df_credits1.parquet')

# Rutas Render
df_movies = pd.read_pickle(r'Datasets\df_movies.pkl')
df_credits = pd.read_parquet(r'Datasets\df_credits1.parquet')

df_movies['release_date'] = pd.to_datetime(df_movies['release_date'], errors='coerce')

#---------------------------------FUNCIONES-------------------------------------------------

#Función 1 que calcula la cantidad de peliculas estrenadas en un mes determinado
@app.get("/peliculasMes")
def cantidad_filmaciones_mes( Mes: str ):
    Mes= Mes.lower() #Convierte el valor ingresado a minúsculas
    #asignamos un valor a cada mes en español que entre como parámetro
    meses = {
        "enero": 1, "febrero": 2, "marzo": 3, "abril":4, "mayo": 5,
        "junio":6, "julio":7, "agosto":8, "septiembre":9, 
         "octubre":10, "noviembre":11, "diciembre":12
    }
    if(Mes not in meses):#Si el mes seleccionado no está entre las opciones
        raise HTTPException(status_code=400, detail="Ingrese un mes válido en español")
              
        
    peliculas_mes = (df_movies[df_movies['release_date'].dt.month==meses[Mes]])
    return f"{len(peliculas_mes)} películas fueron estrenadas en el mes de {Mes}"
    

#--------------------------------------------------------------------------------------------------------------------------

#Función que calcula la cantidad de peliculas estrenadas en un día determinado
@app.get("/peliculasDia")
def cantidad_filmaciones_dia( Dia ):
    Dia= Dia.lower() #Convierte el valor ingresado a minúsculas#Convierte el valor ingresado a minúsculas
    #asignamos un valor a cada día en español que entre como parámetro
    Dias = {
        "lunes": "Monday", "martes": "Tuesday", "miercoles": "Wednesday", "jueves":"Thursday", "viernes": "Friday",
        "sabado":"Saturday", "domingo":"Sunday"
    }
    if(Dia not in Dias):#Si el día seleccionado no está entre las opciones
        raise HTTPException(status_code=400, detail="Ingrese un día válido en español")

    peliculas_dia = (df_movies[df_movies['release_date'].dt.day_name()==Dias[Dia]])
    return f"{len(peliculas_dia)} películas fueron estrenadas el dia de {Dia}"

print(df_credits['id'].loc[3])