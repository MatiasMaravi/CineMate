import json
from supabase import create_client

url = "https://inlhowinxzuskmodrpix.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImlubGhvd2lueHp1c2ttb2RycGl4Iiwicm9sZSI6ImFub24iLCJpYXQiOjE2OTY5NjI5ODYsImV4cCI6MjAxMjUzODk4Nn0.jII7SbPyktiAuUrKirqQ6eD7_2uu-Mb8crpnT0MkMfo"
supabase = create_client(url, key)

def obtener_preferencia_usuario(usuario, table_1):

    try:

        preferencia_usuario = supabase.table(table_1).select("*").eq('email_user', usuario).execute()

        return preferencia_usuario.data  

    except Exception as e:
        print(f'Error: {e}')
        return None

def insertar_preferencia_usuario(usuario, table_1, ):

    try:

        data_to_insert = {"email_user": usuario, "title": pelicula}
        data, count = supabase.table(table_1).insert(data_to_insert).execute()

        return data

    except Exception as e:
        print(f'Error: {e}')
        return None    
