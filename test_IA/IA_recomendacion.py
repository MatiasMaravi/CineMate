
# Esta recomendacion es basada en una pelicula que ya vio el usuario

import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import MultiLabelBinarizer

# Cargar datos de películas
movies = pd.read_csv('movies.csv')

# Procesar géneros utilizando MultiLabelBinarizer
mlb = MultiLabelBinarizer()
genre_matrix = mlb.fit_transform(movies['genres'].str.split('|'))

# Calcular similitud de coseno entre géneros
cosine_sim = cosine_similarity(genre_matrix, genre_matrix)

# Crear un DataFrame de similitud de géneros
cosine_similarity_matrix = pd.DataFrame(cosine_sim, index=movies['title'], columns=movies['title'])

# Función para obtener recomendaciones de películas basadas en géneros
def get_genre_recommendations(movie_title, n=5):
    similar_movies = cosine_similarity_matrix.loc[movie_title]
    # Excluye la película de referencia si se encuentra en la lista
    if movie_title in similar_movies.index:
        similar_movies = similar_movies.drop(movie_title)
    recommendations = similar_movies.sort_values(ascending=False).head(n)
    return recommendations

# Ejemplo de recomendación
movie_title = 'Titanic (1997)'
recommendations = get_genre_recommendations(movie_title, n=5)

# Obtener los nombres de las películas recomendadas
recommended_movie_titles = recommendations.index

print("Recomendaciones de películas basadas en géneros:")
for title in recommended_movie_titles:
    print(title)
