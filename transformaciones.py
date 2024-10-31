import pandas as pd
import numpy as np
import json

# Rutas de los datasets originales
ruta_credits = r'C:\HENRY\PROYECTOS HENRY 11\Movies\credits1.json'
ruta_credits_csv = r'C:\HENRY\PROYECTOS HENRY 11\Movies\movies_dataset.csv'
ruta_movies = r'C:\HENRY\PROYECTOS HENRY 11\Movies\movies2.json'

credits_lista = []
with open(ruta_credits, 'rt', encoding='utf-8') as f:
    for line_num, line in enumerate(f, 1):
        line = line.strip()
        if line:
            try:
                credits_lista.append(json.loads(line))
            except json.JSONDecodeError as e:
                print(f"Error en la línea {line_num}: {line}")
                print(f"Detalle del error: {e}")
df_credits = pd.DataFrame(credits_lista)

movies_lista = []
with open(ruta_movies, 'rt', encoding='utf-8') as f:
    for line_num, line in enumerate(f, 1):
        line = line.strip()
        if line:
            try:
                movies_lista.append(json.loads(line))
            except json.JSONDecodeError as e:
                print(f"Error en la línea {line_num}: {line}")
                print(f"Detalle del error: {e}")
df_movies = pd.DataFrame(movies_lista)

#Cambiar valores nulos en revenue por 0
df_movies['revenue'] = np.where(pd.isnull(df_movies['revenue']), 0, df_movies['revenue'])

#Cambiar valores nulos en revenue por 0
df_movies['budget'] = np.where(pd.isnull(df_movies['budget']), 0, df_movies['budget'])

df_movies['release_date'].dropna()

#-------------------DESANIDAR------------------------------------------------------

# Desanidar la columna 'Cast'
df_credits_expanded_cast = df_credits.explode('Cast')

# Normalizar la columna 'Cast'
df_credits_cast = pd.json_normalize(df_credits_expanded_cast['Cast'])

# Renombrar las columnas de 'Cast'
df_credits_cast.columns = [f"cast_{col}" for col in df_credits_cast.columns]

# Combinar los DataFrames con 'id' y 'Crew'
df_credits_cast = pd.concat([
    df_credits_expanded_cast[['id']].reset_index(drop=True),
    df_credits_cast.reset_index(drop=True)
], axis=1)

print(df_credits_cast.head(20))

#-------------------------------------------------------------------------------------------------

# Cambiamos el tipo de dato de la columna 'release_date' str a datetime
df_movies['release_date'] = pd.to_datetime(df_movies['release_date'], format='%Y-%m-%d')

# Verificamos el tipo de dato de la columna
print(type(df_movies['release_date'].loc[2]))

#Creamos la columna 'release_year', la cual se obtiene de sacar el año de la columna 'release_date'
df_movies['release_year']=df_movies['release_date'].dt.year

#Creamos columna 'return', la cual es el resultado de revenue / budget
df_movies['return']=df_movies['revenue']/df_movies['budget']

#Eliminamos algunas columnas
df_movies = df_movies.drop(columns=['video', 'imdb_id', 'adult', 'original_title', 'poster_path', 'homepage'])








print(type(df_movies['release_date'].head(2).loc[1]))
# Guardar los DataFrames
#df_movies.to_pickle('df_movies.pkl')
#df_credits.to_pickle('df_credits.pkl')
#df_movies.to_json('df_movies1.json', lines=True, orient='records')
#df_credits.to_parquet('df_credits1.parquet')