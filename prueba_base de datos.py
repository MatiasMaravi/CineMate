import json
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
        user_data = {
            'email': self.email,
            'name': self.name,
            'password': self.password
        }
        data, count = supabase.table('usuarios').insert([user_data]).execute()
        return data

    def obtener(self):
        response = supabase.table('usuarios').select("*").execute()
        data = response.data
        formatted_data = json.dumps(data, indent=4)

        print(f'Data: {formatted_data}')

    def actualizar(self, user_data, usuario_email):
        data, count = supabase.table('usuarios').update(user_data).eq('email', usuario_email).execute()
        return data 


# Ejemplo de cómo crear un objeto de usuario
usuario1 = Usuario("alejo@gmail.com", "Alejo", "chupetin23")

"""# Insertar el usuario en la base de datos
response = usuario1.insertar()
if response:
    print("Usuario insertado con éxito")"""

# Actualizar el usuario en la base de datos
user_data = {
    'email': "tuejemplo.com",
    'name': "Tu nombre",
    'password': "Tu contraseña"
}
response = usuario1.actualizar(user_data, "alejo@gmail.com")
if response:
    print("Usuario actualizado con éxito")

# Obtener los usuarios
usuario1.obtener()
