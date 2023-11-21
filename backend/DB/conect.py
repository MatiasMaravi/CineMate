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

"""

    def obtener(self):
        response = supabase.table('usuario').select("*").execute()
        data = response.data
        formatted_data = json.dumps(data, indent=4)

        print(f'Data: {formatted_data}')





    def update(self):
        return f'Nombre: {self.nombre}\nApellido: {self.apellido}\nCorreo: {self.correo}'

# Ejemplo de cómo crear un objeto de usuario
usuario1 = Usuario("alejo@gmail.com", "Alejo", "chupetin23")

# Acceder a los atributos del usuario

usuario1.insertar()
"""