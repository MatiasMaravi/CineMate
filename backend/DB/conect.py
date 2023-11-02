import os
from supabase import create_client, Client
import json

url = "https://inlhowinxzuskmodrpix.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImlubGhvd2lueHp1c2ttb2RycGl4Iiwicm9sZSI6ImFub24iLCJpYXQiOjE2OTY5NjI5ODYsImV4cCI6MjAxMjUzODk4Nn0.jII7SbPyktiAuUrKirqQ6eD7_2uu-Mb8crpnT0MkMfo"
supabase: Client = create_client(url, key)





class Usuario:
    def _init_(self, email, name, password):
        self.email = email
        self.name = name
        self.password = password

    def insertar(self,user):
        data, count = supabase.table('usuarios').insert(user).execute()
        return data

    def obtener(self):
        response = supabase.table('usuarios').select("*").execute()
        data = response.data
        formatted_data = json.dumps(data, indent=4)

        print(f'Data: {formatted_data}')





    def update(self):
        return f'Nombre: {self.nombre}\nApellido: {self.apellido}\nCorreo: {self.correo}'

# Ejemplo de cómo crear un objeto de usuario
usuario1 = Usuario("alejo@gmail.com", "Alejo", "chupetin23")

# Acceder a los atributos del usuario

usuario1.insertar()