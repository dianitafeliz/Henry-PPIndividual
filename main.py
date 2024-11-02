#IMPORTS
from http.client import HTTPException
import pandas as pd
import numpy as np
import json
import matplotlib.pyplot as plt
import seaborn as sns
from fastapi import FastAPI
from fastapi import FastAPI, HTTPException
app = FastAPI()
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os

#df_movies = pd.read_pickle(r'C:\HENRY\PROYECTOS HENRY 11\Primer Proyecto Individual\Datasets\df_movies.pkl')
#df_credits = pd.read_parquet(r'C:\HENRY\PROYECTOS HENRY 11\Primer Proyecto Individual\Datasets\df_credits1.parquet')

#df_credits_pkl = pd.read_pickle(r'C:\HENRY\PROYECTOS HENRY 11\Primer Proyecto Individual\Datasets\newCredits.pkl')

# Rutas Render------------------------------------------------------------------------------------
current_directory = os.path.dirname(__file__)

# Construir las rutas completas a los archivos
df_movies_path = os.path.join(current_directory, 'Datasets', 'df_movies.pkl')
df_credits_path = os.path.join(current_directory, 'Datasets', 'newCredits1.pkl')
#-------------------------------------------------------------------------------------------------

# Cargar los archivos para Render
df_movies = pd.read_pickle(df_movies_path)
df_credits = pd.read_pickle(df_credits_path)

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

#Función 2 que calcula la cantidad de peliculas estrenadas en un día determinado
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
    return f"{len(peliculas_dia)} películas fueron estrenadas el dia {Dia}"


#--------------------------------------------------------------------------------------------------------------------------

#Función 3 Se ingresa el título de una filmación esperando como respuesta el título, 
# el año de estreno y el score

@app.get("/peliculasScore")
def score_titulo(titulo_de_la_filmación):
    titulo_de_la_filmación = titulo_de_la_filmación.lower()
    # Convertir los títulos del DataFrame a minúsculas para la comparación
    df_movies['title_lower'] = df_movies['title'].str.lower()
    # Filtrar las filas donde el título coincida con el título de la filmación
    coincidencias = df_movies[df_movies['title_lower'] == titulo_de_la_filmación]

    # Si hay coincidencias, devuelve el título, el año de lanzamiento, y la puntuación
    if not coincidencias.empty:
        titulo = coincidencias['title'].values[0]
        año = int(coincidencias['release_year'].values[0])
        puntuacion = float(coincidencias['vote_average'].values[0] / coincidencias['popularity'].values[0])
        # Aplicamos la función round para redondear solo a 2 decimales
        puntuacion = round(puntuacion, 2)
        #return titulo, año, puntuacion
        return f" La película {titulo} fue estrenada en el año {año} con un score de {puntuacion} "
    else:
        return "No se encontró la filmación"

# Ejemplo de uso
#resultado = score_titulo("Sense and Sensibility")
#print(resultado)

#--------------------------------------------------------------------------------------------------------------------------

#Función 4 Se ingresa el título de una filmación esperando como respuesta el título,
#  la cantidad de votos y el valor promedio de las votaciones. La misma variable deberá 
# de contar con al menos 2000 valoraciones

@app.get("/peliculasVotaciones")
def votos_titulo(titulo_de_la_filmación):
    titulo_de_la_filmación = titulo_de_la_filmación.lower()
    # Convertir los títulos del DataFrame a minúsculas para la comparación
    df_movies['title_lower'] = df_movies['title'].str.lower()
    # Filtrar las filas donde el título coincida con el título de la filmación
    coincidencias = df_movies[df_movies['title_lower'] == titulo_de_la_filmación]
    
    if not coincidencias.empty:
        votos = coincidencias.iloc[0]['vote_count']
        promedio = coincidencias.iloc[0]['vote_average']
        if votos >= 2000:
            return f"La película {coincidencias.iloc[0]['title']} fue estrenada en el año {int(coincidencias.iloc[0]['release_year'])}. La misma cuenta con un total de {votos} valoraciones, con un promedio de {promedio}"
    return "No se encontraron coincidencias o la película no tiene suficientes valoraciones."

#print(votos_titulo('Get Shorty'))

#--------------------------------------------------------------------------------------------------------------------------

#Función 5 Se ingresa el nombre de un actor que se encuentre dentro de un dataset
# debiendo devolver el éxito del mismo medido a través del retorno. Además, la cantidad 
# de películas que en las que ha participado y el promedio de retorno


@app.get("/ActorRetorno")
def get_actor(nombre_actor: str):
    nombre_actor = nombre_actor.lower().strip()
    
    # Filtrar las filas donde el nombre coincida con el nombre_actor y manejar None
    coincidencias = df_credits[df_credits['Cast'].apply(lambda Cast: Cast is not None and any(member['name'].lower() == nombre_actor for member in Cast))]
    #print(coincidencias)
    
    # Verificar que haya coincidencias
    if coincidencias.empty:
        return {"actor": nombre_actor, "cantidad_filmes": 0, "total_return": 0.1, "avg_return": 0.1}
        
    # Obtener los IDs únicos y contar la cantidad de películas
    cant_films = len(coincidencias['id'].unique())
    
    # Verificar que la columna 'return' exista
    if 'return' not in df_movies.columns:
        return {"actor": nombre_actor, "cantidad_filmes": cant_films, "total_return": 0.0, "avg_return": 0.0}
    
    # Seleccionar las películas del actor
    actor_movies = df_movies[df_movies['id'].isin(coincidencias['id'])].copy()
    
    # Manejar los valores NaN e infinitos en la columna 'return'
    actor_movies['return'] = actor_movies['return'].replace([np.inf, -np.inf], np.nan)
    actor_movies['return'] = actor_movies['return'].fillna(0)
          
    # Calcular el retorno total y el promedio de retorno
    total_return = float(round(actor_movies['return'].sum(), 2))
    avg_return = float(round(actor_movies['popularity'].sum() / cant_films if cant_films > 0 else 0.0, 2))
    
    return {"actor": nombre_actor, "cantidad_filmes": cant_films, "total_return": total_return, "avg_return": avg_return}


# Prueba la función
print(get_actor('Johnny Depp'))
#print(get_actor('Alfred Molina'))




#--------------------------------------------------------------------------------------------------------------------------
#Función 6
@app.get("/DirectorRetorno")
def get_director(nombre_director):
    nombre_director = nombre_director.lower()

    # Asegurarse de que los valores en la columna 'directors' son cadenas y manejamos adecuadamente listas y arreglos
    def process_directors(directors):
        if isinstance(directors, list):
            return ', '.join(d.lower() for d in directors)
        elif isinstance(directors, np.ndarray):
            return ', '.join(directors).lower()
        else:
            return directors.lower()

    df_credits['directors'] = df_credits['directors'].apply(process_directors)

    # Filtrar las filas donde el nombre del director coincide con nombre_director
    coincidencias = df_credits[df_credits['directors'].str.contains(nombre_director)]

    # Verificar que haya coincidencias
    if coincidencias.empty:
        return {"director": nombre_director, "cantidad_filmes": 0, "total_return": 0.0, "avg_return": 0.0}

    # Comparación de películas
    peliculas = df_movies[df_movies['id'].isin(coincidencias['id'])].copy()

    # Manejar los valores NaN en la columna 'return' antes de sumar
    peliculas['return'] = peliculas['return'].replace([np.inf, -np.inf], np.nan)
    peliculas['return'] = peliculas['return'].fillna(0)

    # Calcular el nivel de retorno
    total_return = round(peliculas['return'].sum(), 2)

    return {
        "director": nombre_director,
        "cantidad_filmes": len(peliculas),
        "total_return": total_return,
        "avg_return": total_return / len(peliculas) if len(peliculas) > 0 else 0.0,
        "peliculas": peliculas[['title', 'release_year', 'revenue', 'budget', 'return']].to_dict(orient='records')
    }

# Prueba la función
print(get_director('Gary Trousdale'))

#--------------------------------------------------------------------------------------------------------------------------
# Similitud del coseno usando titulo y genero
#Función 7
@app.get("/Recomendadas")
def recommend_movies(movie_title: str, num_recommendations: int = 5):
    title_col = 'title'
    genre_col = 'genres'
    
    # Unir título y géneros en un texto
    def process_genres(genres):
        if isinstance(genres, str):  # Si es una cadena, intenta convertirla a lista de diccionarios
            try:
                genres = json.loads(genres.replace("'", "\""))
            except json.JSONDecodeError:
                return ""
        # Une los nombres de los géneros si es una lista de diccionarios
        return ' '.join([genre['name'] for genre in genres if isinstance(genre, dict) and 'name' in genre])
    
    # Aplicar la función de procesamiento a la columna 'genres'
    df_movies['combined_features'] = df_movies[title_col] + ' ' + df_movies[genre_col].apply(process_genres)
    
    # Vectorizar las características combinadas
    vectorizer = TfidfVectorizer(stop_words='english')
    combined_matrix = vectorizer.fit_transform(df_movies['combined_features'])
    
    # Verificar que la película existe en el DataFrame
    if movie_title not in df_movies[title_col].values:
        raise HTTPException(status_code=404, detail=f"Movie '{movie_title}' not found")
    
    # Encontrar el índice de la película objetivo
    target_index = df_movies[df_movies[title_col] == movie_title].index[0]
    
    # Calcular la similitud del coseno
    cosine_similarities = cosine_similarity(combined_matrix[target_index], combined_matrix).flatten()
    
    # Obtener índices de películas similares en orden descendente
    similar_indices = cosine_similarities.argsort()[::-1][1:num_recommendations + 1]
    
    # Crear un DataFrame con las recomendaciones y los puntajes de similitud
    recommendations = pd.DataFrame({
        'title': df_movies.iloc[similar_indices][title_col].values,
        'similarity_score': cosine_similarities[similar_indices]
    }).sort_values(by='similarity_score', ascending=False)
    
    return recommendations.to_dict(orient='records')

# Prueba la función
#recomendaciones = recommend_movies('From Dusk Till Dawn')
#print(recomendaciones)
