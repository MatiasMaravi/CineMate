import os
from supabase import create_client, Client
import json
from dotenv import load_dotenv
load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(url, key)

class Usuario:
    @staticmethod
    def insertar(user):
        data, count = supabase.table('usuario').insert(user).execute()
        return data
