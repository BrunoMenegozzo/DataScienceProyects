## GENRE PREDICTOR with Spotify
## Music Genre Predictor
Exploring the information provided by Spotify through the API I realized that it did not include the genre of the song, this caught my attention powerfully and provide other data as abstract as the "danceability". However, it is understandable that it does not provide this information as it is difficult to define, there are songs that are influenced by different genres and that makes a precise determination complicated. In addition, many people do not distinguish genres, I have been in many conversations where confusion between cumbia and cuarteto or between trap and rap occurs.

Motivated by this idea I started this project, we are going to see if it is possible to distinguish between different genres using the information provided by the spotify API and doing some data scraping.

The project is divided into 3 phases.

├── notebooks/.

│ ├─── Spotify_DataManagement.ipynb # Data collection and preprocessing.

│ ├─── Spotify_Visualization.ipynb # Exploratory analysis and visualization.

│ └─── Spotify_ModelosDePrediccion.ipynb # Model training and evaluation.

Translated with DeepL.com (free version)

## Step 1: Data Collection
│ ├── Spotify_Data_Management.ipynb

Looking to create a dataset with values returned from the Spotify API, tagging by known artists that are exclusively dedicated to a genre. For example "La Mona Jimenez" is a reference of the quartet and is the only genre to which it is dedicated. In addition, by means of web scraping we obtained the lyrics of the songs to which a sentiment analysis was applied to determine the average positivity of each of their phrases, in order to obtain a new feature. Of course, with all this raw information we prepared the data, cleaning some records that had been null, among other actions, for a correct analysis and data visualization.

## Step 2: Data visualization
│ ├── Spotify_Visualization.ipynb

In this phase, a comprehensive exploratory analysis of the collected data was performed using various visualization techniques to better understand the characteristics and relationships between variables. A heatmap was generated to visualize the correlations between the different features, which allowed the identification of significant patterns and dependencies. Histograms were created for each of the features, providing a clear view of the distribution of the data in each variable. In addition, box plots were used to detect outliers and understand the dispersion of the data in each category. Finally, a pairplot was produced showing the relationship between all the features, providing a global perspective of how the variables interact with each other and how the different musical genres are grouped according to these characteristics. These visualizations were fundamental to guide decisions in the modeling stage and to obtain valuable insights about the particularities of each music genre. PairPlotSpotify

## Step 3: Training the classification model.
│ └── Spotify_ModelsOfPrediction.ipynb.

A logistic regression model was initially trained to rank among the obtained data. In addition, the corresponding confusion matrix was obtained, the corresponding hyperparameter optimization was performed, and the ROE curve was plotted which allows us to observe the performance of this model. Finally, other classification models (such as random forest, vector machines, KNN, MLP) were evaluated to observe the performance of other models and compare them. Plotting the performance of each on a set of two-dimensional graphs achieved thanks to dimensionality reduction with PCA

![ModelsVariousResults](https://github.com/user-attachments/assets/0fefe2a2-d7c2-44b3-874c-30ef72ffa596)
