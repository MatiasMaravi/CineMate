import unittest
import json
from app import create_app  # Reemplaza "your_app_module" con el nombre de tu módulo principal

class APITestCase(unittest.TestCase):
    
    def setUp(self):
        self.app = create_app().test_client()

    def test_get_movies_endpoint(self):
        data = {
            "usuario":"ana1@gmail.com",
            "generos":["terror","comedia"],
            "actores":["Brad Pit"]
}
        response = self.app.post('/movies', json=data)
        self.assertEqual(response.status_code, 200)

        # Verifica la estructura de la respuesta
        response_data = json.loads(response.data.decode('utf-8'))
        self.assertIn('movies', response_data)
        self.assertIsInstance(response_data['movies'], list)

        # Puedes agregar más aserciones según sea necesario para verificar el contenido de la respuesta

if __name__ == '__main__':
    unittest.main()


