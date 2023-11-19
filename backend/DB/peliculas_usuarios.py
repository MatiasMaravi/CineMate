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


def usuario_peliculas(usuario,genero,actor,peliculas):

    table_1="r_history"

    try:
            diccionario= {"movies":[]}
            for title in peliculas:
             try:
                data_to_insert = {"user": usuario, "genre":genero,"actor":actor,"title_movie": title,"interaction":1,"date":datetime.datetime.now().date().isoformat()}
                diccionario["movies"].append(title)
                supabase.table(table_1).insert(data_to_insert).execute()
             except Exception as e:
                print(f'Se alcanzo el limite de recomendaciones')
                print(f'Error: {e}')
                return None   
            return diccionario

    except Exception as e:
        print(f'Error: {e}')
        return None

def verificar_genero_actor(usuario,genero,actor):
        
        if actor and genero:
            data = supabase.table('r_history').select('*').eq('user', usuario).filter('actor', 'eq', actor).filter('genre', 'eq', genero).filter('interaction', 'eq', 1).execute()
            data = json.loads(data.model_dump_json())
        elif actor:
            data = supabase.table('r_history').select('*').eq('user', usuario).filter('actor', 'eq', actor).filter('interaction', 'eq', 1).execute()
            data = json.loads(data.model_dump_json())

        elif genero:
            data = supabase.table('r_history').select('*').eq('user', usuario).filter('genre', 'eq', genero).filter('interaction', 'eq', 1).execute()
            data = json.loads(data.model_dump_json())
                
        else:
            return None, 0        

        movies = [movie['title_movie'] for movie in data['data']]

        return movies, len(movies)

