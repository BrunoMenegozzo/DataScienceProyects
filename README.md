# GenrePredictor
# Predictor de genero musical
Explorando la información que proporciona Spotify mediante la API me di cuenta de que no incluía el género de la canción, esto me llamó poderosamente la atención ya proporcionar otros datos tan abstractos como la “bailabilidad”. Sin embargo, es entendible que no proporcione esta información ya que es difícil de definir, hay canciones que se encuentran influenciadas por distintos géneros y eso hace complicado una determinación precisa. Además, mucha gente no distingue géneros, he estado en muchas conversaciones donde la confusión entre cumbia y cuarteto o entre trap y rap se da.

Motivado con esta idea encare este proyecto, vamos a ver si es posible distinguir entre distintos géneros utilizando la información proporcionada por la API de spotify y haciendo un poco de scraping de datos.

El proyecto se divide en 3 fases

├── notebooks/

│   ├── `Spotify_ManejoDeDatos.ipynb`        # Recopilación y preprocesamiento de datos

│   ├── `Spotify_Visualizacion.ipynb`        # Análisis exploratorio y visualización

│   └── `Spotify_ModelosDePrediccion.ipynb`  # Entrenamiento y evaluación de modelos

## Paso 1: Recopilación de Datos
│   ├── `Spotify_ManejoDeDatos.ipynb`


Buscando crear un dataset con valores devueltos de la API de Spotify, etiquetando por artistas conocidos y que se dedican exclusivamente a un género. Por ejemplo "La Mona Jimenez" es un referente del cuarteto y es el único género al cual se dedica. Y además, mediante web scraping se obtuvieron las letras de las canciones a las cuales se les aplicó un sentiment analysis para determinar el promedio de positividad de cada una de sus frases, para así obtener un nuevo feature.
    Por su puesto, con toda esta información en bruto se prepararon los datos, limpiando algunos registros que habían quedado nulos, entre otras acciones, para un correcto análisis y visualización de datos.

## Paso 2: Visualizacion de datos
│   ├── `Spotify_Visualizacion.ipynb`

En esta fase, se realizó un análisis exploratorio exhaustivo de los datos recopilados, utilizando diversas técnicas de visualización para comprender mejor las características y relaciones entre las variables. Se generó un heatmap para visualizar las correlaciones entre las diferentes features, lo que permitió identificar patrones y dependencias significativas. Se crearon histogramas para cada una de las características, proporcionando una visión clara de la distribución de los datos en cada variable. Además, se utilizaron gráficos de cajas (box plots) para detectar outliers y comprender la dispersión de los datos en cada categoría. Finalmente, se elaboró un pairplot que muestra la relación entre todas las features, ofreciendo una perspectiva global de cómo interactúan las variables entre sí y cómo se agrupan los diferentes géneros musicales en función de estas características. Estas visualizaciones fueron fundamentales para guiar las decisiones en la etapa de modelado y para obtener insights valiosos sobre las particularidades de cada género musical.
![PairPlotSpotify](https://github.com/BrunoMenegozzo/DataScienceProyects/assets/101132664/25b86be9-56e7-4304-b1a2-bc240b3736d1)
## Paso 3: Entrenamiento del modelo de clasificación
│   └── `Spotify_ModelosDePrediccion.ipynb`

Se entrenó un modelo de regresión logística inicialmente para clasificar entre los datos obtenidos. Además se obtuvo la correspondiente matriz de confusión, se realizó la correspondiente optimización de hiperparametros y se graficó la curva ROE que permite observar el desempeño de este modelo.
    Por último, se evaluaron otros modelos de clasificación (como random forest, máquinas vectoriales, KNN, MLP) para observar el desempeño de otros modelos y compararlos. Graficando el desempeño de cada uno en un conjunto de gráficos de dos dimensiones logrado gracias a una reducción de la dimensionalidad con PCA
    
![ModelosVariosResultados](https://github.com/BrunoMenegozzo/DataScienceProyects/assets/101132664/1c90ecdc-8a63-48f9-86f7-bde3ab7358ac)


# EVI_Lago_San_Roque

Soy de Villa Carlos Paz, una ciudad ubicada en Córdoba, Argentina. Todos los años sufrimos un evento ambiental denominado "eutrofización", que es un crecimiento desmedido de la población de cianobacterias presentes en nuestro lago. Esto trae consigo diversos problemas, desde un impacto en la actividad turística de la ciudad hasta un problema de salud, ya que las cianobacterias son un vector de enfermedades hepáticas para humanos y animales.

Lo que se realizó en este proyecto fue un modelo de regresión para predecir la proliferación de las cianobacterias en el lago de mi ciudad. Las mediciones se lograron obtener vía satélite a través de EVIs (índice de vegetación mejorado), tomando imágenes satelitales mensuales (https://dgg321982.users.earthengine.app/view/copernicus).
![Curvas por año](https://github.com/user-attachments/assets/fbacd783-0091-432e-a0dd-bd2fd21457f1)
