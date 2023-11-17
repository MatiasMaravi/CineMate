import openai
import time
import os
from dotenv import load_dotenv
load_dotenv()

# Configura la API key
openai.api_key = os.getenv("API_KEY")

def IA_peliculas(generos, actores):

    # Genera una respuesta a partir de un prompt

    promt="Recomiendame solo los nombres de 10 peliculas sin informacion antes ni despues, de generos de "
    
    for i in generos:
        promt = promt + i + ", "

    promt += "con los actores, "
    for i in actores:
        promt = promt + i + ", "     
    
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
    respuesta_generada = respuesta_generada.replace('"', '')
    respuesta_generada = respuesta_generada.split(", ")

    respuesta={
        "movies":respuesta_generada,
        "time": end_time - start_time
    }

    return respuesta

def IA_generos():
    promt="Recomiendame solo los nombres de 5 generos "
    pass

def IA_anios(anios: list):
    # Genera una respuesta a partir de un prompt

    promt="Recomiendame solo los nombres de 10 peliculas sin informacion antes ni despues, que salieron en los siguientes años: "
    
    for i in anios:
        promt = promt + i + ", "
    
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
    respuesta_generada = respuesta_generada.replace('"', '')
    respuesta_generada = respuesta_generada.split(", ")

    respuesta={
        "movies":respuesta_generada,
        "time": end_time - start_time
    }

    return respuesta

def IA_idiomas(idiomas: list):
    # Genera una respuesta a partir de un prompt

    promt="Recomiendame solo los nombres de 10 peliculas sin informacion antes ni despues, que salieron en los siguientes idiomas: "
    
    for i in idiomas:
        promt = promt + i + ", "
    
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
    respuesta_generada = respuesta_generada.replace('"', '')
    respuesta_generada = respuesta_generada.split(", ")

    respuesta={
        "movies":respuesta_generada,
        "time": end_time - start_time
    }

    return respuesta