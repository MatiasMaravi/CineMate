import os
import json
import logging
from supabase import Client, create_client
from dotenv import load_dotenv

# Para ocultar la información adicional de los fetch realizados por supabase
logging.getLogger("httpx").setLevel(logging.WARNING)

load_dotenv()

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")

supabase = create_client(url, key)

def get_genres_recommendation(usr: str):
    data = supabase.table('genre_recommendation').select('genre').eq('email_user', usr).execute()
    data_json = json.loads(data.model_dump_json())
    data_json = data_json['data']

    return [g["genre"] for g in data_json]

def get_disliked(usr: str):
    data = supabase.table('r_history').select('title_movie').eq('dislike', True).execute()
    data_json = json.loads(data.model_dump_json())
    data_json = data_json['data']
    
    return [m["title_movie"] for m in data_json]

def get_liked(usr: str):
    data = supabase.table('r_history').select('title_movie').eq('like', True).execute()
    data_json = json.loads(data.model_dump_json())
    data_json = data_json['data']
    
    return [m["title_movie"] for m in data_json]

usr = "test@gmail.com"
print(get_genres_recommendation(usr))