from flask import Flask, jsonify
from flask import request
import json
from test_IA.core import get_genre_recommendations
app = Flask(__name__)


# @app.route('/api/movies', methods=['GET'])
# def get_movies():
#     try:
#         with open('movies.json', 'r') as json_file:
#             data = json.load(json_file)
#         return jsonify(data)
#     except FileNotFoundError:
#         return jsonify({"error": "El archivo 'movies.json' no se encontró."}), 404

@app.route('/movies', methods=['POST'])
def get_movies():
    try:
        request_data = request.json
        movie_title = request_data['name']
        recommendations = get_genre_recommendations(movie_title, n=5)
        # Obtener los nombres de las películas recomendadas
        recommended_movie_titles = recommendations.index
        dictionary = {"movies":[]}
        for i in recommended_movie_titles:
            dictionary["movies"].append(i)
        return jsonify(dictionary)
    except FileNotFoundError:
        return jsonify({"error": "El archivo 'movies.json' no se encontró."}), 404


if __name__ == '__main__':
    app.run(debug=True)
