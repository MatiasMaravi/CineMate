import requests

# URL de la API que deseas probar

title = "The Matrix"
url = "https://www.omdbapi.com/?t="+title+"&apikey=5161e29"  # Reemplaza con la URL de la API real

# Realiza una solicitud GET a la API
response = requests.get(url)

# Verifica si la solicitud fue exitosa (código de respuesta 200)
if response.status_code == 200:
    data = response.json()  # Si la respuesta es JSON
    print("Respuesta JSON:")
    print(data["Poster"])
else:
    print(f"Error: La solicitud no se pudo completar. Código de respuesta: {response.status_code}")
