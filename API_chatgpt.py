import openai

#openai.api_key = "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"

clave_personal="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"

openai.api_key = clave_personal

completion = openai.Completion.create(model="gpt-3.5-turbo", prompt="¿Recomiendame 5 peliculas con el genero de accion y romance?", max_tokens=2048)

print(completion.choices[0].text)