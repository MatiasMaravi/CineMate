import os
import json
from supabase import Client, create_client
from dotenv import load_dotenv

load_dotenv()

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")

supabase = create_client(url, key)

def obtener_peliculas_por_actor(usuario, actor):
    data = supabase.table('r_history').select('*').eq('user', usuario).filter('actor', 'eq', actor).filter('interaction', 'eq', 1).execute()
    data = json.loads(data.model_dump_json())

    movies = [movie['title_movie'] for movie in data['data']]
    return movies, len(movies)

# Test manual
usuario = "MATIUS"
actor = "actor1"
print(obtener_peliculas_por_actor(usuario, actor))
