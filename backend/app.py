from recommendation.core import get_genre_recommendations
from flask import Flask, jsonify, request
from supabase import create_client, Client
import os 
from dotenv import load_dotenv
load_dotenv()
app = Flask(__name__)


url = os.getenv("URL")
key = os.getenv("KEY")
supabase: Client = create_client(url, key)



@app.route('/movies', methods=['POST'])
def get_movies():
    try:
        request_data = request.json
        movie_title = request_data['title']
        recommendations = get_genre_recommendations(movie_title, n=5)
        # Obtener los nombres de las películas recomendadas
        recommended_movie_titles = recommendations.index
        
        diccionario= {"movies":[]}
        for title in recommended_movie_titles:
            data_to_insert = {"title": title}
            diccionario["movies"].append(title)
            data, count = supabase.table("movies").insert(data_to_insert).execute()

        return jsonify(diccionario), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 404
    

def create_app():
    return app

if __name__ == '__main__':
    app.run(debug=True)
