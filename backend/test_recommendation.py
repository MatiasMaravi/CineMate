import unittest
from flask import Flask
from flask_testing import TestCase
from app import create_app
import json

class TestMoviesEndpoint(TestCase):
    def create_app(self):
        return create_app()
    def test_get_movies_endpoint(self):
        movie_data = {
            "name": "The Lego Movie (2014)"
        }
        response = self.client.post('/movies', json=movie_data)
        data = json.loads(response.data.decode('utf-8'))

        # Verifica que el código de estado de la respuesta sea 200
        self.assertEqual(response.status_code, 200)

        # Verifica que la estructura de la respuesta sea la esperada
        self.assertIn('movies', data)
        self.assertIsInstance(data['movies'], list)

        # Agrega más aserciones según sea necesario para verificar el contenido de la respuesta

if __name__ == '__main__':
    unittest.main()
