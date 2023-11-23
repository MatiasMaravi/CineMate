import os
import json
import logging
from supabase import Client, create_client
from dotenv import load_dotenv

load_dotenv()

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")

supabase = create_client(url, key)  

def obtener_peliculas_BD(username):

    data = supabase.table('r_history').select('*').eq('user', username).execute()
    data = json.loads(data.model_dump_json())
    respuesta = {}
    print(data)
    for i in data['data']:
        if i['title_movie'] not in respuesta:
            respuesta[i['title_movie']] = i['interaction']
            
    return respuesta

