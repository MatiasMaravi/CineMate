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


def usuario_peliculas(usuario,peliculas,generos,actores):

    table_1="r_history"

    try:
            diccionario= {"movies":[]}
            for title in peliculas:
                data_to_insert = {"email_user": usuario, "title_movie": title,"interaction":0,"date":datetime.datetime.now().date().isoformat(),"genres": generos, "actors": actores}
                diccionario["movies"].append(title)
                data, count = supabase.table(table_1).insert(data_to_insert).execute()
            return diccionario

    except Exception as e:
        print(f'Error: {e}')
        return None

