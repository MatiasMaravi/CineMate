# API - CHAT-GPT 3.5 TURBO

### Instalación

```bash
pip3 install openai
```
o

```bash
pip install openai
```

### Ejemplo basico de uso

```python

    import openai

    clave="API_KEY"

    openai.api_key = clave

    promt="¿Cuál es el mejor lenguaje de programación?"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo"
        message={"role": "user", "content": promt },
    )

    respuesta=response['choices'][0]['message']['content']
  ```

  - La clave sirve para poder acceder a la API, la cual se obtiene en la página de OPENAI, en la sección de API KEYS.

  - El modelo es el que se va a utilizar para generar la respuesta, en este caso se utilizó el modelo gpt-3.5-turbo, el cual es un modelo recientemente lanzado.

  - En la parte de promt se escribe la pregunta que se le va a hacer al modelo.

  - En response se empieza a utilizar la API, en la cual se le pasa el modelo y el mensaje que se le va a enviar al modelo.

  - En respuesta se obtiene la respuesta del modelo la cual se extraee del response.


  # Tiempos de respuesta

    - El tiempo de respuesta del modelo gpt-3.5-turbo es de 3.3 segundos aproximadamente.


