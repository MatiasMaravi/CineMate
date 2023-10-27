from recommendation.core import get_genre_recommendations
from flask import Flask, jsonify, request
import supabase
import os 
from dotenv import load_dotenv
load_dotenv()
app = Flask(__name__)


url = "https://inlhowinxzuskmodrpix.supabase.co"
key = os.getenv("KEY") #"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImlubGhvd2lueHp1c2ttb2RycGl4Iiwicm9sZSI6ImFub24iLCJpYXQiOjE2OTY5NjI5ODYsImV4cCI6MjAxMjUzODk4Nn0.jII7SbPyktiAuUrKirqQ6eD7_2uu-Mb8crpnT0MkMfo"
client = supabase.Client(url, key)



@app.route('/movies', methods=['POST'])
def get_movies():
    try:
        request_data = request.json
        movie_title = request_data['name']
        recommendations = get_genre_recommendations(movie_title, n=5)
        # Obtener los nombres de las películas recomendadas
        recommended_movie_titles = recommendations.index

        for title in recommended_movie_titles:
            data_to_insert = [{"name": title}]
            response, error = client.table("movies").upsert(data_to_insert, returning="representation")
            if error:
                return jsonify({"error" : f"No se pudo insertar la película: {title}"})
            
        dictionary = {"movies": recommended_movie_titles}  
        return jsonify(dictionary)
    except Exception as e:
        return jsonify({"error": str(e)}), 404
    

def create_app():
    return app

if __name__ == '__main__':
    app.run(debug=True)
