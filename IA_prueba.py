import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import MultiLabelBinarizer

# Cargar datos de películas
movies = pd.read_csv('movies.csv')
movies['genres'] = movies['genres'].str.split('|')

# Procesar géneros utilizando MultiLabelBinarizer
mlb = MultiLabelBinarizer()
genre_matrix = mlb.fit_transform(movies['genres'])

print(genre_matrix)


# Calcular similitud de coseno entre géneros
cosine_sim = cosine_similarity(genre_matrix, genre_matrix)

# Crear un DataFrame de similitud de géneros
cosine_similarity_matrix = pd.DataFrame(cosine_sim, index=movies['title'], columns=movies['title'])

print(cosine_similarity_matrix)

# Función para obtener recomendaciones de películas basadas en géneros
def get_genre_recommendations(genres, n=5):
    # Filtrar las películas que cumplen con el filtro de géneros
    genre_filter = movies['genres'].apply(lambda x: any(genre in genres for genre in x))
    filtered_movies = movies[genre_filter]
    
    # Obtener el índice de las películas filtradas
    filtered_movie_indices = filtered_movies.index

    
    # Filtrar la matriz de similitud para las películas que cumplen con el filtro
    similarities = cosine_similarity_matrix.loc[filtered_movie_indices, filtered_movie_indices]
    
    # Calcular la similitud promedio entre las películas
    mean_similarities = similarities.mean(axis=1) 
    
    # Ordenar las películas en función de la similitud promedio
    recommendation_scores = mean_similarities.sort_values(ascending=False)
    
    # Excluir las películas que tienen todos los géneros proporcionados
    recommendation_scores = recommendation_scores[~recommendation_scores.index.isin(movies[movies['genres'].apply(lambda x: set(genres).issubset(x))].index)]
    
    # Obtener las películas recomendadas
    recommended_movie_titles = recommendation_scores.head(n).index
    
    return recommended_movie_titles


# Ejemplo de recomendación por género
desired_genres = ['Action', 'Adventure', 'Science Fiction']
recommended_movie_titles = get_genre_recommendations(desired_genres, n=5)

print("Recomendaciones de películas basadas en géneros:")
for title in recommended_movie_titles:
    print(title)
