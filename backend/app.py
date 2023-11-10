#from recommendation.core import get_genre_recommendations
from flask import Flask, jsonify, request
from supabase import create_client, Client
from DB.peliculas_usuarios import usuario_peliculas
from IA.api_chat import IA_peliculas,IA_generos, IA_director_movies, IA_awards_movies
import os 
from dotenv import load_dotenv
load_dotenv()
app = Flask(__name__)


url = "https://inlhowinxzuskmodrpix.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImlubGhvd2lueHp1c2ttb2RycGl4Iiwicm9sZSI6ImFub24iLCJpYXQiOjE2OTY5NjI5ODYsImV4cCI6MjAxMjUzODk4Nn0.jII7SbPyktiAuUrKirqQ6eD7_2uu-Mb8crpnT0MkMfo"
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


def create_app():
    return app

if __name__ == '__main__':
    app.run(debug=True)

