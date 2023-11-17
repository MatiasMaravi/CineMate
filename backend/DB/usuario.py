import json
import os
from supabase import create_client

url = "https://inlhowinxzuskmodrpix.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImlubGhvd2lueHp1c2ttb2RycGl4Iiwicm9sZSI6ImFub24iLCJpYXQiOjE2OTY5NjI5ODYsImV4cCI6MjAxMjUzODk4Nn0.jII7SbPyktiAuUrKirqQ6eD7_2uu-Mb8crpnT0MkMfo"


supabase = create_client(url, key)


class Usuario:

    def __init__(self, email, name, password):
        self.email = email
        self.name = name
        self.password = password

    def insertar(self):
        data, count = supabase.table('usuario').insert([{"email": self.email, "name": self.name, "password": self.password}]).execute()
        print(f'Usuario creado Satisfactoriamente: {data}')   

    def obtener(self):
        response = supabase.table('usuario').select("*").execute()
        data = response.data
        formatted_data = json.dumps(data, indent=4)

        print(f'Data: {formatted_data}')

    def buscar(self, email):
        response = supabase.table('usuario').select("*").eq('email', email).execute()
        data = response.data
        formatted_data = json.dumps(data, indent=4)

        print(f'Usuario Encontrado: {formatted_data}')

    def update(self, email, name, password):
        data, count = supabase.table('usuario').update({"name": name, "password": password}).eq('email', email).execute()
        print(f'Usuario Actualizado: {data}')


# Prueba de la clase Usuario

# Crear un usuario

usuario1 = Usuario("juan@gmail.com", "Juan", "123456")
#usuario1.insertar()            
usuario1.update("juan@gmail.com","Juan Perez", "123456789")



