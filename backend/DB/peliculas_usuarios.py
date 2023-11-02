# Peliculas que le gustan al usuario

import datetime
import json
from supabase import create_client

url = "https://inlhowinxzuskmodrpix.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImlubGhvd2lueHp1c2ttb2RycGl4Iiwicm9sZSI6ImFub24iLCJpYXQiOjE2OTY5NjI5ODYsImV4cCI6MjAxMjUzODk4Nn0.jII7SbPyktiAuUrKirqQ6eD7_2uu-Mb8crpnT0MkMfo"
supabase = create_client(url, key)


def usuario_peliculas(usuario,peliculas):

    table_1="preference_movie"

    try:

            diccionario= {"movies":[]}
            for title in peliculas:
                data_to_insert = {"email_user": usuario, "title": title,"interacion":0,"date": datetime.date.today() }
                diccionario["movies"].append(title)
                data, count = supabase.table(table_1).insert(data_to_insert).execute()
            return diccionario    
        

    except Exception as e:
        print(f'Error: {e}')
        return None
table_1 = 'preference_actor'

