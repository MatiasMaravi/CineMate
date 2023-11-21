# Peliculas que le gustan al usuario

import datetime
import json
from supabase import create_client
import os
from dotenv import load_dotenv
load_dotenv()


url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
supabase = create_client(url, key)


def insertar_peliculas(usuario,peliculas):

    table_1="r_history"

    try:
            diccionario= {"movies":[]}
            for title in peliculas:
             try:
                data_to_insert = {"user": usuario,"title_movie": title,"interaction":1,"date":datetime.datetime.now().date().isoformat()}
                data=supabase.table(table_1).select('*').eq('user', usuario).eq('title_movie', title).execute()
                if len(data.data) > 0:
                    continue
                supabase.table(table_1).insert(data_to_insert).execute()
                diccionario["movies"].append(title)
             except Exception as e:
                print(f'Se alcanzo el limite de recomendaciones')
                print(f'Error: {e}')
                return "Se alcanzo el limite de recomendaciones"
            return diccionario

    except Exception as e:
        print(f'Error: {e}')
        return None

def verificar_peliculas(usuario):
        # Verificar el numero de peliculas que le gustan al usuario

        data = supabase.table('r_history').select('*').eq('user', usuario).filter('interaction', 'eq', 1).execute()
        data = json.loads(data.model_dump_json())      

        movies = [movie['title_movie'] for movie in data['data']]

        return movies, len(movies)

