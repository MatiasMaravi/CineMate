import os
from supabase import create_client, Client
import json


class SupabaseManager:
    def __init__(self, url, key):
        self.supabase = create_client(url, key)

    def insertar_generos(self, usuarios_generos):
        datos_mock = []
        
        for usuario, generos in usuarios_generos.items():
            for genero in generos:
                datos_mock.append({
                    'email_user': usuario,
                    'genre': genero
                })

        response = self.supabase.table('genre_recomendation').upsert(datos_mock, on_conflict=['email_user', 'genre']).execute()


        print(response)

    def insertar_actores(self, usuarios_actores):
        datos_mock = []
        
        for usuario, actores in usuarios_actores.items():
            for actor in actores:
                datos_mock.append({
                    'user_name': usuario,
                    'actor': actor
                })

        response = self.supabase.table('actor_preference').upsert(datos_mock, on_conflict=['user_name', 'actor']).execute()


        print(response)

def main():

    url = "https://inlhowinxzuskmodrpix.supabase.co"
    key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImlubGhvd2lueHp1c2ttb2RycGl4Iiwicm9sZSI6ImFub24iLCJpYXQiOjE2OTY5NjI5ODYsImV4cCI6MjAxMjUzODk4Nn0.jII7SbPyktiAuUrKirqQ6eD7_2uu-Mb8crpnT0MkMfo"

    supabase_manager = SupabaseManager(url, key)


    # Ejemplo de usuarios y sus géneros
    usuarios_generos_ejemplo = {
        'Ana': ['Rock', 'Pop', 'Salsa'],
        'Juan': ['Pop', 'Reggae', 'Jazz']
    }

    supabase_manager.insertar_generos(usuarios_generos_ejemplo)


    usuarios_actores_ejemplo = {
        'Ana': ['Brad Pitt', 'Emma Watson', 'Tom Hanks'],
        'Juan': ['Johnny Depp', 'Scarlett Johansson']
    }

    supabase_manager.insertar_actores(usuarios_actores_ejemplo)

if __name__ == "__main__":
    main()
