import unittest
from api_chat import IA_peliculas, IA_generos

class TestAPIChat(unittest.TestCase):

    def test_IA_peliculas(self):
        generos = ["terror", "comedia"]
        actores = ["Brad Pit"]
        respuesta = IA_peliculas(generos, actores)

        self.assertIsInstance(respuesta, dict)  
        self.assertIn("movies", respuesta)  
        self.assertIn("time", respuesta)  
        self.assertIsInstance(respuesta["movies"], list) 
        self.assertTrue(respuesta["time"] >= 0)

    def test_IA_generos(self):
        respuesta = IA_generos()

        self.assertIsInstance(respuesta, str) 

if __name__ == '__main__':
    unittest.main()
