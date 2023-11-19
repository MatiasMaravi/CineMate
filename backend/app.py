#from recommendation.core import get_genre_recommendations
from flask import Flask, jsonify, request
from supabase import create_client, Client
from DB.peliculas_usuarios import usuario_peliculas
from IA.api_chat import IA_peliculas
import os 
from dotenv import load_dotenv
import datetime
app = Flask(__name__)

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(url, key)

@app.route('/movies', methods=['POST'])
def consulta_IA():
    try:
        request_data = request.json
        usuario= request_data['usuario']
        movie_generos = request_data['generos']
        movie_actores = request_data['actores']
        if(len(movie_generos) == 0):
            recommendations = IA_peliculas([],movie_actores,usuario)
        elif(len(movie_actores) == 0):
            recommendations = IA_peliculas(movie_generos,[],usuario)
        elif (len(movie_generos) != 0 and len(movie_actores)!=0):
            recommendations = IA_peliculas(movie_generos,movie_actores,usuario)
        print(recommendations)
        # Obtener los nombres de las películas recomendadas
        recommended_movie_titles = recommendations["movies"]

        diccionario= usuario_peliculas(usuario,recommended_movie_titles,movie_generos,movie_actores)

        return jsonify(diccionario), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 404

@app.route('/movies/insertar', methods=['POST'])
def insertar():
    request_data = request.json
    email_user = request_data['email_user']
    title_movie = request_data['title_movie']
    interaction = request_data['interaction']
    
    
    movies = supabase.table('r_history').select('*').eq('email_user', email_user).eq('title_movie', title_movie).execute()
    
    if len(movies.data) > 0:
        # Actualizar la columna 'interaction' de todas las películas encontradas
        for movie in movies.data:
            supabase.table('r_history').update({'interaction': interaction}).eq('title_movie', movie['title_movie']).eq('email_user', movie['email_user']).execute()
        
        return jsonify({"message": f"Se han actualizado {len(movies.data)} películas"}), 200
    else:
        return jsonify({"message": "No se encontró la película"}), 404



def create_app():
    return app

if __name__ == '__main__':
    app.run(debug=True,port=5000)
