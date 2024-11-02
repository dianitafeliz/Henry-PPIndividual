# Henry-PPIndividual
Primer Proyecto Individual Henry
<h4>Descripción:</h4>
Este proyecto tiene como objetivo analizar los datos de una plataforma de extreaming, con el fin de crear un sistema de recomendación, empezando por un ETL que nos permita obtener datos más limpios y organizados para el respectivo analisis exploratorio de los datos EDA, que nos permita descubrir el significado de los mismos.
<h4>Contenido:</h4>
1. Instalación y Requisitos
2. Estructura del proyecto
3. Transformación de datos
4. Datos y fuentes
5. Metodología
6. Resultados y conclusiones.

<h4>1. Instalación y Requisitos:</h4>
Python 3.7 o superior
pandas
numpy
matplotlib
scikit-learn
json
fastapi
seaborn
os

<h4>Pasos de instalación:</h4>
Entorno Virtual:
1. Crear el entorno virtual: python -m venv ppindividual
2. Activar entorno virtual: ppindividual\Scripts\activate
3. Instalar dependencias del proyecto: pip install -r requirements.txt
4. Ejecutar tu aplicación FastAPI utilizando el servidor de Uvicorn: uvicorn main:app --reload

Render:
1. Crear proyecto en https://github.com/: https://github.com/dianitafeliz/Henry-PPIndividual.git
2. Crear una cuenta en (https://render.com/)
3. ir a dashboar y crear un nuevo servicio (+New)
4. Configurar el repositorio de github 
5. Configurar la Branch: main
6. Configurar el Build Command: pip install -r requirements.txt
7. Configurar el Start Command: uvicorn main:app --host 0.0.0.0 --port 8000
8. y Desplegar

<h4>2. Estructura del proyecto</h4>

1.transformacion_datos.ipynb: Es un notebook que contiene todo el desarrollo del proyecto paso a paso mediante el cual realicé las pruebas necesarias antes de llevarlo a main.py. Contiene todas las transformaciones que se le hicieron a los datos durante el desarrollo del proyecto, y todas las funciones desarrolladas y funcionales.
2. transformaciones.py: Contiene unicamente las transformaciones de los datos de manera limpia y organizada.
3. requirements.txt: Contiene todas las dependencias con las versiones necesarias para poder desplegar el proyecto.
4. main.py: Contiene todas las funciones a desplegar con sus respectivos decoradores.
5. Datasets: Contiene los datasets transformados para el despliegue.
6. README.md: Documentación del Proyecto.

<h4>3. Transformación de datos</h4>
Con base en los datos originales y para el correcto despliegue en render, se aplicaron las transformaciones solicitadas en el ejercicio y se eliminaron columnas no requeridas para el análisis solicitado, y se borraron solo 3000 filas del dataset credits, las cuales cuentan con un retorno = a 0. (pasando de 181mb a 33mb)

<h4>4. Datos y fuentes </h4>
Datasets Originales: https://drive.google.com/drive/folders/1X_LdCoGTHJDbD28_dJTxaD4fVuQC9Wt5
Datasets Organizados Json: https://drive.google.com/drive/folders/1hFkjdaWb-ZDytw2Cm9c9tKFpKacq1ET8?usp=sharing
Datasets usados para despliegue: https://github.com/dianitafeliz/Henry-PPIndividual/tree/main/Datasets

<h4>5. Metodología</h4>
Para crear el sistema de recomendaciones, hice uso de la similitid del coseno, la cual es una métrica utilizada para medir la similitud entre dos vectores en un espacio multidimensional, es decir, se utiliza para comparar la similitud entre elementos, que para este caso se hizo basado en titulos y generos de las peliculas.
Librería usada:
scikit-learn
funciones: 
TfidfVectorizer
cosine_similarity

<h4>6. Resultados y conclusiones<h4>
1. Se extrajeron los datos del datasets poco funcionales
2. Se transformaron los datos para conseguir mejor calidad de datos
3. Se cargaron los datos en nuevos datasets listos para el analisis
4. Se crearon funciones con el fin de analizar diferentes comportamientos pertinentes para la toma de decisiones
5. Se creó un sistema de recomendación de peliculas según el titulo y generos.
6. Se logra desplegar la api en render.
