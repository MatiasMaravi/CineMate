#from recommendation.core import get_genre_recommendations
from flask import Flask, jsonify, request
from supabase import create_client, Client
from DB.peliculas_usuarios import usuario_peliculas
from IA.api_chat import IA_peliculas,IA_generos
import os 
from dotenv import load_dotenv
load_dotenv()
app = Flask(__name__)


url = "https://inlhowinxzuskmodrpix.supabase.co"
key = os.getenv("SUPABASE_KEY")
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
        print(generos)
        return jsonify(generos), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 404


def create_app():
    return app

if __name__ == '__main__':
    app.run(debug=True)
