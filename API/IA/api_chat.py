import openai
import time
import os
from dotenv import load_dotenv
from DB.obtener_peliculas import obtener_peliculas_BD
from supabase import Client, create_client
from dotenv import load_dotenv

load_dotenv()

# Configura la API key
openai.api_key = os.getenv("API_KEY")

def IA_peliculas(generos, actores,username):

    peliculas=obtener_peliculas_BD(username)

    # Genera una respuesta a partir de un prompt
    promt="Recomiendame solo los nombres de 5 peliculas distintas sin informacion antes ni despues ,"
    
    if len(generos)!=0:
        promt += "de generos, "
        for i in generos:
            promt = promt + i + ","

    if len(actores)!=0:
        promt += " con los actores, "
        for i in actores:
            promt = promt + i + ","        

    if len(peliculas)!=0:

        promt += " sabiendo que me gustan las peliculas "

        for i in peliculas:
            if i["like"]==True:
                promt = promt + i["title"] + ","


        promt += " y sabiendo que no me gustan las peliculas "

        for i in peliculas:
            if i["like"]==False:
                promt = promt + i["title"] + ","                 
        
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

    






