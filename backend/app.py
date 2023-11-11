#from recommendation.core import get_genre_recommendations
from flask import Flask, jsonify, request
from supabase import create_client, Client
from DB.peliculas_usuarios import usuario_peliculas
from IA.api_chat import IA_peliculas,IA_generos, IA_director_movies, IA_awards_movies, IA_lugar_grabacion, IA_same_peliculas, IA_anios, IA_idiomas
import os 
from dotenv import load_dotenv
load_dotenv()
app = Flask(__name__)



url = os.getenv("URL")
key = os.getenv("KEY")
supabase: Client = create_client(url, key)



@app.route('/movies', methods=['POST'])
def consulta_IA():
    try:
        request_data = request.json
        usuario= request_data['usuario']
        movie_generos = request_data['generos']
        movie_actores = request_data['actores']
        recommendations = IA_peliculas(movie_generos,movie_actores)
        print(recommendations)
        # Obtener los nombres de las películas recomendadas
        recommended_movie_titles = recommendations["movies"]

        diccionario= usuario_peliculas(usuario,recommended_movie_titles)

        return jsonify(diccionario), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 404


@app.route('/generos', methods=['POST'])
def obtener_generos():
    try:
        generos=IA_generos()
        print("Generos", generos)
        return jsonify(generos), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 404



@app.route('/director_movies', methods=['POST'])
def obtener_peliculas_por_director():
    try:
        request_data = request.json
        usuario = request_data['usuario']
        directores = request_data['directores']
        director_movies = IA_director_movies(usuario, directores, top_n=10)
        print(f"Top 10 películas dirigidas por {', '.join(directores)} para {usuario}", director_movies)
        return jsonify(director_movies), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 404



@app.route('/awards_movies', methods=['POST'])
def obtener_peliculas_por_premios():
    try:
        request_data = request.json
        usuario = request_data['usuario']
        awards = request_data['awards']
        awards_movies = IA_awards_movies(usuario, awards)
        print(f"Top 10 películas con premios {', '.join(awards)} para {usuario}", awards_movies)
        return jsonify(awards_movies), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 404

@app.route('/lugar_grabacion', methods=['POST'])
def obtener_peliculas_por_lugar_grabacion():
    try:
        request_data = request.json
        usuario = request_data['usuario']
        lugares = request_data['lugares']
        lugar_grabacion_movies = IA_lugar_grabacion(usuario, lugares, top_n=10)
        print(f"Top 10 películas grabadas en {', '.join(lugares)} para {usuario}", lugar_grabacion_movies)
        return jsonify(lugar_grabacion_movies), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 404


@app.route('/same_movies', methods=['POST'])
def obtener_recomendaciones_por_peliculas():
    try:
        request_data = request.json
        usuario = request_data['usuario']
        peliculas = request_data['movies']
        
        # Llamada a la función IA_peliculas
        recomendaciones = IA_same_peliculas(peliculas, top_n=10)

        print(f"Top 10 recomendaciones basadas en películas para {usuario}", recomendaciones)
        return jsonify(recomendaciones), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 404
    
@app.route('/anios', methods=['POST'])
def obtener_recomendacion_anios():
    try:
        request_data = request.json
        usuario = request_data['usuario']
        anios = request_data['anios']
        recommendations = IA_anios(anios)
        print(recommendations)
        # Obtener los nombres de las películas recomendadas
        recommended_movie_titles = recommendations["movies"]

        diccionario= usuario_peliculas(usuario, recommended_movie_titles)

        return jsonify(diccionario), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 404

@app.route('/idiomas', methods=['POST'])
def obtener__recomendacion_idiomas():
    try:
        request_data = request.json
        usuario = request_data['usuario']
        idiomas = request_data['idiomas']
        recommendations = IA_idiomas(idiomas)
        print(recommendations)
        # Obtener los nombres de las películas recomendadas
        recommended_movie_titles = recommendations["movies"]

        diccionario= usuario_peliculas(usuario, recommended_movie_titles)

        return jsonify(diccionario), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 404


def create_app():
    return app

if __name__ == '__main__':
    app.run(debug=True)

