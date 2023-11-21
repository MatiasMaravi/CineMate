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


def usuario_peliculas(usuario,peliculas):

    table_1="r_history"

    try:
            diccionario= {"movies":[]}
            for title in peliculas:
             try:
                data_to_insert = {"user": usuario,"title_movie": title,"interaction":1,"date":datetime.datetime.now().date().isoformat()}
                diccionario["movies"].append(title)
                supabase.table(table_1).insert(data_to_insert).execute()
             except Exception as e:
                print(f'Se alcanzo el limite de recomendaciones')
                print(f'Error: {e}')
                return "Se alcanzo el limite de recomendaciones para ese actor y genero"  
            return diccionario

    except Exception as e:
        print(f'Error: {e}')
        return None

def verificar_genero_actor(usuario):
        
        if usuario:
            data = supabase.table('r_history').select('*').eq('user', usuario).filter('interaction', 'eq', 1).execute()
            data = json.loads(data.model_dump_json())
                
        else:
            return None, 0        

        movies = [movie['title_movie'] for movie in data['data']]

        return movies, len(movies)

