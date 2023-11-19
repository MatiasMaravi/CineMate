import os
import json
import logging
from supabase import Client, create_client
from dotenv import load_dotenv

load_dotenv()

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")

supabase = create_client(url, key)

def obtener_peliculas_BD(usuario, genero):
    data = supabase.table('r_history').select('*').eq('user', usuario).execute()
    data = json.loads(data.model_dump_json())

    movies = [movie['title_movie'] for movie in data['data'] if movie['genre'] == genero and movie['interaction'] == 1]
    return movies, len(movies)

#Test manual
usuario = "MATIUS"
genero = "genero1"
print(obtener_peliculas_BD(usuario, genero))