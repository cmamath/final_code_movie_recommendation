**Movie Recommendation System**
This project is a Python-based movie recommendation system that fetches movie data from The Movie Database (TMDB) API based on a specified genre. It saves the movie data to a CSV file and recommends a random movie from the list.

**Features**
Fetches movies from TMDB based on the specified genre.
Saves the list of movies to a CSV file.
Recommends a random movie from the list.

**Requirements**
Python 3.x
requests library
pandas library

**Installation**

pip install requests
pip install beautifulsoup4
**Get TMDB API Key:**

Sign up at TMDB.
Go to your account settings and navigate to the API section.
Generate an API key.

**Usage**
Enter the Genre:

When prompted, enter the genre for which you want to fetch movies (e.g., action, comedy, drama).

View the Output:

The script will save the list of movies to a CSV file named <genre>_movies.csv and print a recommended movie.

**Example**
Enter the genre: action
Saved movies to action_movies.csv
Recommended Movie: The Dark Knight (2008) with rating 8.4

**Error Handling**
The script includes error handling for the following scenarios:

HTTP request failures when accessing the TMDB API.
No movies found for the specified genre.
Errors while parsing the movie data.
Errors while saving the CSV file.

![image](https://github.com/cmamath/final_code_movie_recommendation/assets/174296440/9b06596f-802a-4f2f-b94c-c4531c23125b)








