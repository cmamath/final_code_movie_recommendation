import requests
import random
import pandas as pd

API_KEY = '82a3ccb79549099fc99a1f3fdf1dd485'

class TMDBError(Exception):
    pass

def get_genre_id(genre_name):
    url = f"https://api.themoviedb.org/3/genre/movie/list?api_key={API_KEY}&language=en-US"
    response = requests.get(url)
    
    if response.status_code != 200:
        raise TMDBError(f"Failed to retrieve genres: {response.status_code}")
    
    genres = response.json().get('genres', [])
    for genre in genres:
        if genre['name'].lower() == genre_name.lower():
            return genre['id']
    raise TMDBError(f"Genre '{genre_name}' not found.")

def get_movies_by_genre(genre_id):
    url = f"https://api.themoviedb.org/3/discover/movie?api_key={API_KEY}&with_genres={genre_id}"
    response = requests.get(url)
    
    if response.status_code != 200:
        raise TMDBError(f"Failed to retrieve movies: {response.status_code}")
    
    movies = response.json().get('results', [])
    if not movies:
        raise TMDBError("No movies found for the given genre.")
    
    return [
        {
            'title': movie['title'],
            'rating': movie.get('vote_average', 'N/A'),
            'year': movie['release_date'].split('-')[0] if movie.get('release_date') else 'N/A'
        }
        for movie in movies
    ]

def recommend_movie(movies):
    if not movies:
        return "No movies found for the given genre."
    
    recommended_movie = random.choice(movies)
    return f"Recommended Movie: {recommended_movie['title']} ({recommended_movie['year']}) with rating {recommended_movie['rating']}"

def save_movies_to_csv(movies, genre):
    try:
        df = pd.DataFrame(movies)
        df.to_csv(f"{genre}_movies.csv", index=False)
        print(f"Saved movies to {genre}_movies.csv")
    except Exception as e:
        print(f"Error saving movies to CSV: {e}")

def main():
    genre = input("Enter the genre: ").strip().lower()
    try:
        genre_id = get_genre_id(genre)
        movies = get_movies_by_genre(genre_id)
        if movies:
            save_movies_to_csv(movies, genre)
        recommendation = recommend_movie(movies)
        print(recommendation)
    except TMDBError as e:
        print(f"An error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
