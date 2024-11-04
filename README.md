# Henry-PPIndividual
Primer Proyecto Individual Henry<br>
<h4> https://henry-ppindividual.onrender.com/docs#/ </h4>
<h4>Descripción:</h4>
Este proyecto tiene como objetivo analizar los datos de una plataforma de streaming, con el fin de crear un sistema de recomendación, empezando por un ETL que nos permita obtener datos más limpios y organizados para el respectivo analisis exploratorio de los datos EDA, que nos permita descubrir el significado de los mismos.
<h4>Contenido:</h4>
1. Instalación y Requisitos <br>
2. Estructura del proyecto <br>
3. Transformación de datos <br>
4. Datos y fuentes <br>
5. Metodología <br>
6. Resultados y conclusiones <br>
7. Datos de Prueba <br>

<h4>1. Instalación y Requisitos:</h4> 
<h5>Requisitos:</h5> 
Python 3.7 o superior <br>
pandas <br>
numpy <br>
matplotlib <br>
scikit-learn <br>
json <br>
fastapi <br>
seaborn <br>
os <br>

<h5>Pasos de instalación:</h5> 
Entorno Virtual: <br>
1. Crear el entorno virtual: python -m venv ppindividual <br>
2. Activar entorno virtual: ppindividual\Scripts\activate <br>
3. Instalar dependencias del proyecto: pip install -r requirements.txt <br>
4. Ejecutar tu aplicación FastAPI utilizando el servidor de Uvicorn: uvicorn main:app --reload <br>

Render: <br>
1. Crear proyecto en https://github.com/: https://github.com/dianitafeliz/Henry-PPIndividual.git 
2. Crear una cuenta en (https://render.com/)
3. ir a dashboard y crear un nuevo servicio (+New)
4. Configurar el repositorio de github 
5. Configurar la Branch: main
6. Configurar el Build Command: pip install -r requirements.txt
7. Configurar el Start Command: uvicorn main:app --host 0.0.0.0 --port 8000
8. y Desplegar
 <br>
<h4>2. Estructura del proyecto</h4>
 <br>
1.transformacion_datos.ipynb: Es un notebook que contiene todo el desarrollo del proyecto paso a paso mediante el cual realicé las pruebas necesarias antes de llevarlo a main.py. Contiene todas las transformaciones que se le hicieron a los datos durante el desarrollo del proyecto, y todas las funciones desarrolladas y funcionales. <br>
2. transformaciones.py: Contiene únicamente las transformaciones de los datos de manera limpia y organizada. <br>
3. requirements.txt: Contiene todas las dependencias con las versiones necesarias para poder desplegar el proyecto. <br>
4. main.py: Contiene todas las funciones a desplegar con sus respectivos decoradores. <br>
5. Datasets: Contiene los datasets transformados para el despliegue. <br>
6. README.md: Documentación del Proyecto. <br>

<h4>3. Transformación de datos</h4> <br>
Con base en los datos originales y para el correcto despliegue en render, se aplicaron las transformaciones solicitadas en el ejercicio y se eliminaron columnas no requeridas para el análisis solicitado, y se borraron solo 3000 filas del dataset credits, las cuales cuentan con un retorno = a 0. (pasando de 181mb a 33mb) <br>

<h4>4. Datos y fuentes </h4> <br>
Datasets Originales: https://drive.google.com/drive/folders/1X_LdCoGTHJDbD28_dJTxaD4fVuQC9Wt5 <br>
Datasets Organizados Json: https://drive.google.com/drive/folders/1hFkjdaWb-ZDytw2Cm9c9tKFpKacq1ET8?usp=sharing <br>
Datasets usados para despliegue: https://github.com/dianitafeliz/Henry-PPIndividual/tree/main/Datasets <br>

<h4>5. Metodología</h4> <br>
Para crear el sistema de recomendaciones, hice uso de la similitid del coseno, la cual es una métrica utilizada para medir la similitud entre dos vectores en un espacio multidimensional, es decir, se utiliza para comparar la similitud entre elementos, que para este caso se hizo basado en titulos y generos de las  <br>
Libreria usada: <br>
scikit-learn <br>
funciones:  <br>
TfidfVectorizer <br>
cosine_similarity <br>

<h4>6. Resultados y conclusiones</h4> <br>
1. Se extrajeron los datos del datasets poco funcionales <br>
2. Se transformaron los datos para conseguir mejor calidad de datos <br>
3. Se cargaron los datos en nuevos datasets listos para el análisis <br>
4. Se crearon funciones con el fin de analizar diferentes comportamientos pertinentes para la toma de decisiones <br>
5. Se creó un sistema de recomendación de peliculas según el titulo y generos. <br>
6. Se logra desplegar la api en render. <br>

<h4>7. Datos de Prueba </h4> <br>
<h5>title:</h5><br>
12 Angry Men<br>
The Seventh Seal<br>
Sense and Sensibility<br>
Evil Dead II<br>
Avatar<br>
The Avengers<br>
Fight Club<br>
The Hunger Games<br>
Get Shorty<br>

<h5>Actor:</h5><br>
Johnny Depp <br>
Alfred Molina <br>
Bob Holt <br>
Frank Sinatra <br>
Robert De Niro <br>
Angelina Jolie <br>

<h5>Director: </h5><br>
Mel Brooks <br>
Gary Trousdale <br>
Steven Spielberg <br>
James Cameron <br>
Tim Burton <br>

<h5>Recomendaciones: </h5><br>
Frankenweenie <br>
Avatar <br>
Minions <br>
Casino <br>
Babe <br>
Batman <br>
