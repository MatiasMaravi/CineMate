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

    data = supabase.table('r_history').select('title_movie','interaction').eq('user', username).execute()
    data = json.loads(data.model_dump_json())
    respuesta = []

    for i in data['data']:
        if i["interaction"] == '1':
            respuesta.append({'title': i['title_movie'], 'like': True})
        else:
            respuesta.append({'title': i['title_movie'], 'like': False})

    return respuesta        

#supabase.table('r_history').update({'interaction': '1'}).eq('email_user', 'cristianvargas.com').eq('title_movie', 'Sideways').execute()
