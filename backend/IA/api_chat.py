import openai
import time
import os
from dotenv import load_dotenv
from DB.obtener_peliculas import obtener_peliculas_BD
from DB.peliculas_usuarios import verificar_genero_actor
from dotenv import load_dotenv
import re

load_dotenv()

# Configura la API key
openai.api_key = os.getenv("API_KEY")

def IA_peliculas(genero, actor ,username,n):

    peliculas=obtener_peliculas_BD(username,actor,genero)
    print(peliculas)
    peliculas_gustadas=[]

    n=5-n

    if n==1:
        promt="Recomiendame solo el nombre de una pelicula en ingles sin informacion antes ni despues ,"
        
        if genero:
            promt += "de genero, "
            for i in genero:
                promt = promt + i + ","

        if actor:
            promt += " con el actores, "
            for i in actor:
                promt = promt + i + ","        

        if len(peliculas)!=0:

            promt += "sabiendo que me gustan las peliculas "

            for i in peliculas:
                if peliculas[i]==1:
                    peliculas_gustadas.append(i)
                    promt = promt + i + ","


            promt += " y sabiendo que no me gustan las peliculas "

            for i in peliculas:
                if peliculas[i]==0:
                    promt = promt + i + ","                 
            
        promt+="y devuelvemelo en formato python de lista, en una sola linea, sin informacion extra, sin el año de estreno, sin corchetes, separado por comas, sin comillas, sin espacios y sin puntos."

    else:
        # Genera una respuesta a partir de un prompt
        promt="Recomiendame solo los nombres de " + str(n) +" peliculas distintas en ingles sin informacion antes ni despues ,"
        
        if genero:
            promt += "de genero, "
            for i in genero:
                promt = promt + i + ","

        if actor:
            promt += " con el actor, "
            for i in actor:
                promt = promt + i + ","        

        if len(peliculas)!=0:

            promt += " sabiendo que me gustan las peliculas "

            for i in peliculas:
                if peliculas[i]==1:
                    peliculas_gustadas.append(i)
                    promt = promt + i + ","


            promt += " y sabiendo que no me gustan las peliculas "

            for i in peliculas:
                if peliculas[i]==0:
                    promt = promt + i + ","                 
            
        promt+="y devuelvemelo en formato python de lista, en una sola linea, sin informacion extra,  sin el año de estreno, sin corchetes, separado por comas, sin comillas, sin espacios y sin puntos."


    print(promt)

    start_time = time.time()

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": promt },
        ],
    temperature=0.2)

    end_time = time.time()

    print("Tiempo de ejecucion: ", end_time - start_time , " segundos")

    # Extraer la respuesta generada por el modelo, la cual se encuentra en el primer elemento de la lista
    respuesta_generada = response['choices'][0]['message']['content']

    # Mostrar la respuesta
    respuesta_generada = respuesta_generada.split(",")

    if n!=5:
        for i in peliculas_gustadas:
            respuesta_generada.append(i)

    respuesta={
        "movies":respuesta_generada,
        "time": end_time - start_time
    }

    return respuesta

    






