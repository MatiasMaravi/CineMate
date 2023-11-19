#from recommendation.core import get_genre_recommendations
from flask import Flask, jsonify, request
from supabase import create_client, Client
from DB.peliculas_usuarios import usuario_peliculas , verificar_genero_actor
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

        peliculas_base,count=verificar_genero_actor(usuario,movie_generos[0],movie_actores[0])

        if count==5:
            diccionario= peliculas_base
            return jsonify(diccionario), 200
        else:
            if(len(movie_generos) == 0):
                recommendations = IA_peliculas([],movie_actores,usuario,count)
            elif(len(movie_actores) == 0):
                recommendations = IA_peliculas(movie_generos,[],usuario,count)
            elif (len(movie_generos) != 0 and len(movie_actores)!=0):
                recommendations = IA_peliculas(movie_generos,movie_actores,usuario,count)
            print(recommendations)
            # Obtener los nombres de las películas recomendadas
            recommended_movie_titles = recommendations["movies"]

            diccionario= usuario_peliculas(usuario,movie_generos[0],movie_actores[0],recommended_movie_titles)

            return jsonify(diccionario), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 404

@app.route('/movies/like', methods=['POST'])
def insertar():
    request_data = request.json
    email_user = request_data['email_user']
    title_movie = request_data['title_movie']
    interaction = request_data['interaction']
    #Select * From r_history where email_user = email_user and title_movie = title_movie
    #Si no existe, insertar
    #Si existe, actualizar
    movies = supabase.table('r_history').select('*').eq('user', email_user).eq('title_movie', title_movie).execute()
    
    if(len(movies.data)):
        supabase.table('r_history').update({'interaction': interaction}).eq('user', email_user).eq('title_movie', title_movie).execute()
    else:
        supabase.table('r_history').insert([{'user': email_user, 'title_movie': title_movie, 'interaction': interaction,"date":datetime.datetime.now().date().isoformat()}]).execute()
        
    return jsonify({"message": "Se ha insertado la pelicula"}), 200


def create_app():
    return app

if __name__ == '__main__':
    app.run(debug=True,port=5002)
