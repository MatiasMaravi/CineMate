import requests
from dotenv import load_dotenv
import os
import re
import openai
import time

load_dotenv()

# Set up the OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# OMDB API key
omdb_api_key = os.getenv("OMDB_API_KEY")


clave = os.getenv("OPENAI_API_KEY")
# Configura la API key
openai.api_key = clave

def IA_peliculas(generos, actores):

    # Genera una respuesta a partir de un prompt

    promt="Recomiendame solo los nombres de 10 peliculas sin informacion antes ni despues , de generos de "
    
    for i in generos:
        promt = promt + i + ","

    promt += " con los actores, "
    for i in actores:
        promt = promt + i + ","     
    
    promt+="y devuelvemelo en formato python de lista, en una sola linea, sin informacion extra, sin corchetes, separado por comas, sin comillas."

    print(promt)

    start_time = time.time()

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": promt },
        ],
        temperature=0.7
    )

    end_time = time.time()

    print("Tiempo de ejecucion: ", end_time - start_time , " segundos")

    # Extraer la respuesta generada por el modelo, la cual se encuentra en el primer elemento de la lista
    respuesta_generada = response['choices'][0]['message']['content']

    # Mostrar la respuesta
    respuesta_generada = respuesta_generada.split(",")

    respuesta={
        "movies":respuesta_generada,
        "time": end_time - start_time
    }

    return respuesta

def IA_generos():

    promt="Recomiendame solo los nombres de 5 generos "

    pass



def get_movie_director(title):

    omdb_url = f"http://www.omdbapi.com/?t={title}&apikey={omdb_api_key}"
    response = requests.get(omdb_url)
    
    if response.status_code == 200:
        movie_data = response.json()
        director = movie_data.get("Director", "")
        return director
    else:
        return None


def IA_director_movies(user, directors, top_n=10):
    # Function to generate a top N list of movie recommendations based on a list of directors for a user
    prompt = f"Recomiéndame las mejores {top_n} películas dirigidas por {' y '.join(directors)} para {user}."

    start_time = time.time()

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": prompt},
        ],
        temperature=0.7
    )

    end_time = time.time()

    respuesta_generada = response['choices'][0]['message']['content']

    movie_titles = [title.strip('" ') for title in re.findall(r'"([^"]*)"', respuesta_generada)[:top_n]]

    respuesta = {
        "movies": movie_titles,
        "time": end_time - start_time
    }

    return respuesta



def get_movies_by_awards(awards, top_n=10):

    awards_str = ",".join(awards)
    omdb_url = f"http://www.omdbapi.com/?s=&apikey={omdb_api_key}&awards={awards_str}&type=movie"
    response = requests.get(omdb_url)
    
    if response.status_code == 200:
        movies_data = response.json().get("Search", [])

        movie_titles = [movie.get("Title", "").strip('" ') for movie in movies_data]
        return movie_titles[:top_n] 
    else:
        return []  

def IA_awards_movies(user, awards, top_n=10):

    movie_titles = get_movies_by_awards(awards, top_n)

    awards_str = ", ".join(awards)
    prompt = f"Recomiéndame las mejores {top_n} películas que han ganado premios {awards_str} para {user}."

    start_time = time.time()

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": prompt},
        ],
        temperature=0.7
    )

    end_time = time.time()

    respuesta_generada = response['choices'][0]['message']['content']
    

    additional_movie_titles = [title.strip('" ') for title in re.findall(r'"([^"]*)"', respuesta_generada)[:top_n - len(movie_titles)]]

    respuesta = {
        "movies": movie_titles + additional_movie_titles,
        "time": end_time - start_time
    }

    return respuesta
