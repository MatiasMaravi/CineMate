import requests

api_url = 'http://127.0.0.1:5000/api/movies' 

try:

    response = requests.get(api_url)


    if response.status_code == 200:

        data = response.json()

        for movie in data['movies']:
            print("Movie Name:", movie["name"])
            print("Rating:", movie["rating"])
            print("Genre:", movie["genre"])

            print("")

    else:
        print(f"Error al obtener datos de la API {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"Error de solicitud: {e}")
