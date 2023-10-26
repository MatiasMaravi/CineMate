from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/api/movies', methods=['GET'])
def get_movies():
    try:
        with open('movies.json', 'r') as json_file:
            data = json.load(json_file)
        return jsonify(data)
    except FileNotFoundError:
        return jsonify({"error": "El archivo 'movies.json' no se encontró."}), 404

if __name__ == '__main__':
    app.run(debug=True)
