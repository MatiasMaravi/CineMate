import openai
import time

clave = "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"

# Configura la API key
openai.api_key = clave

# Genera una respuesta a partir de un prompt

promt="Recomiendame solo 5 nombres de peliculas sin informacion extra, de generos de accion y romance ,  con los actores Tom Cruise y Brad Pitt y devuelvemelo solo como una lista de nombres en formato de codigo de python, sin informacion antes ni despues , sin corchetes, separado por comas, sin comillas."

start_time = time.time()


response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": promt },
    ]
)

end_time = time.time()

print("Tiempo de ejecucion: ", end_time - start_time , " segundos")

# Extraer la respuesta generada por el modelo, la cual se encuentra en el primer elemento de la lista
respuesta_generada = response['choices'][0]['message']['content']

# Mostrar la respuesta
respuesta_generada = respuesta_generada.split(",")
print("Respuesta generada:")
for i in respuesta_generada:
    print(i)

