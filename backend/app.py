#from recommendation.core import get_genre_recommendations
from flask import Flask, jsonify, request
from supabase import create_client, Client
from DB.peliculas_usuarios import insertar_peliculas , verificar_peliculas
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

        peliculas_base,count=verificar_peliculas(usuario)

        if count==10:
            diccionario= peliculas_base
            return jsonify(diccionario), 200
        elif count<10:
            if len(movie_generos)==0 and len(movie_actores)==0:
                return jsonify({"message": "No se menciono ningun genero ni actor"}), 404
            elif len(movie_generos)==0 and len(movie_actores)!=0:
                recommendations = IA_peliculas(None, movie_actores,usuario,count)
            elif len(movie_generos)!=0 and len(movie_actores)==0:
                recommendations = IA_peliculas(movie_generos, None,usuario,count)
            else:
                recommendations = IA_peliculas(movie_generos, movie_actores,usuario,count)    

            # Obtener los nombres de las películas recomendadas
            recommended_movie_titles = recommendations["movies"]

            diccionario= insertar_peliculas(usuario,recommended_movie_titles)

            if len(peliculas_base)>0:
                diccionario["movies"].extend(peliculas_base)

            return jsonify(diccionario), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 404

@app.route('/movies/like', methods=['POST'])
def insertar():
    request_data = request.json
    email_user = request_data['usuario']
    title_movie = request_data['title_movie']
    interaction = request_data['interaction']

    # Verificar si la película existe en la base de datos
    movies = supabase.table('r_history').select('*').eq('user', email_user).eq('title_movie', title_movie).execute()
    
    if len(movies.data) > 0:
        if interaction == 0:
        # Actualizar la columna 'interaction' de todas las películas encontradas
            for movie in movies.data:
                supabase.table('r_history').update({'interaction': interaction}).eq('title_movie', movie['title_movie']).eq('user', movie['user']).execute()
            
            return jsonify({"message": f"Se han actualizado {len(movies.data)} película"}), 200
        else:
            return jsonify({"message": "Ya le diste dislike a esta película"}), 404
    else:
        return jsonify({"message": "No se encontró la película dentro de las recomendaciones"}), 404


def create_app():
    return app

if __name__ == '__main__':
    app.run(debug=True,port=5001)
