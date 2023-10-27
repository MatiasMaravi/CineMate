from flask import Flask, jsonify
from flask import request
import json
from recommendation.core import get_genre_recommendations
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
        n = int(n)
        with open('movies.json', 'r') as json_file:
            data = json.load(json_file)
        return jsonify(data["movies"][:n])
    except FileNotFoundError:
        return jsonify({"error": "El archivo 'movies.json' no se encontró."}), 404

if __name__ == '__main__':
    app.run(debug=True)
