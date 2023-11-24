from flask import Flask, jsonify, request
from flask_restful import Api, Resource, reqparse
from flask_swagger_ui import get_swaggerui_blueprint
from supabase import create_client, Client
from DB.peliculas_usuarios import insertar_peliculas , verificar_peliculas
from DB.conect import Usuario
from IA.api_chat import IA_peliculas
import os 
import re
from dotenv import load_dotenv
import datetime
app = Flask(__name__)

SWAGGER_URL = '/swagger'  # URL for exposing Swagger UI (without trailing '/')
API_URL = '/static/swagger.json'  # Our API url (can of course be a local resource)

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
    API_URL,
    config={  # Swagger UI config overrides
        'app_name': "Test application",
    },
)

app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(url, key)

@app.route('/register', methods=['POST'])
def register():
    try:
        request_data = request.json
        # Validación de campos completos
        if 'email' not in request_data or 'name' not in request_data or 'password' not in request_data:
            return jsonify({"error": "Todos los campos son obligatorios"}), 400

        email = request_data['email']
        name = request_data['name']
        password = request_data['password']

        # Validación de formato de correo electrónico
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return jsonify({"error": "Formato de correo electrónico inválido"}), 400



        respuesta = Usuario.insertar({
            'email': email,
            'name': name,
            'password': password
        })

        if respuesta:
            return jsonify({"message": "Usuario registrado correctamente"}), 200
        else:
            return jsonify({"error": "Error al registrar usuario"}), 500

    except Exception as e:
        if "duplicate key value violates unique constraint" in str(e):
            return jsonify({"error": "El usuario ya está registrado"}), 409
        return jsonify({"error": str(e)}), 400


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
