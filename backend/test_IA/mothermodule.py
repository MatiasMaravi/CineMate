from .get_genre_recommendations import *

def get_genre_recommendations(movie_title, n=5):
    similar_movies = cosine_similarity_matrix.loc[movie_title]
    # Excluye la película de referencia si se encuentra en la lista
    if movie_title in similar_movies.index:
        similar_movies = similar_movies.drop(movie_title)
    recommendations = similar_movies.sort_values(ascending=False).head(n)
    return recommendations

if __name__ == '__main__':
    # Ejemplo de recomendación
    movie_title = 'The Lego Movie (2014)'
    recommendations = get_genre_recommendations(movie_title, n=5)

    # Obtener los nombres de las películas recomendadas
    recommended_movie_titles = recommendations.index

    print("Recomendaciones de películas basadas en géneros:")
    for title in recommended_movie_titles:
        print(title)
