# Movie-Recommendation-System

This project is a movie recommendation system built using machine learning techniques. The system provides personalized movie recommendations based on user input, leveraging data from the TMDB 5000 Movie Dataset.

### Project Overview
The recommendation system is developed as a web application using Streamlit, a popular Python library for creating web apps. The core of the project is a content-based recommendation model that suggests movies similar to a user-selected movie.

## Features
- User Input: Users can select a movie from a list of over 5000 titles using a dropdown menu.
- Movie Recommendations: The system returns five recommended movies based on similarity to the selected movie.
- Movie Posters: For each recommended movie, the system also displays the movie poster fetched via the TMDB API.

### How It Works
- Data Collection: The dataset used for building this system is sourced from the TMDB 5000 Movie Dataset.
- Model: A similarity matrix is computed using movie features like genre, keywords, and other metadata. The model returns a list of movies that are similar to the movie selected by the user.
- Web App: The application is built with Streamlit, providing a simple and interactive user interface.

Users select a movie from a dropdown.

The app displays five similar movies with their respective posters.
Technical Stack
- Frontend: Streamlit for user interface.
- Backend: Python for building the recommendation logic.

### Libraries:
- pickle: For loading pre-processed data (movie list and similarity matrix).
- requests: To fetch movie posters from the TMDB API.
- Streamlit: For building and running the web app.
- 
### Folder Structure
- app.py: Contains the main logic for the web app.
- artifacts/: Includes pre-trained models and datasets such as movie_list.pkl and similarity.pkl.
