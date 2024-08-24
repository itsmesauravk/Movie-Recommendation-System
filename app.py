import streamlit as st
import pandas as pd
import pickle
import requests

# Load the dataset in form of a dictionary
movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity  = pickle.load(open('similarity.pkl', 'rb'))

# Function to fetch movie poster images
def fetch_poster(movie_id):
    response = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=0bf04db1ea0cc1a0fbfa551a8c9e1216&language=en-us")
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

# Function for movie recommendations
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:11]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_movies_posters

# Streamlit UI
st.write("Hello, There 👋")
st.title("Find Similar Movies of Your Choice")

selected_movie_name = st.selectbox(
    'Select a movie from the dropdown',
     movies['title'].values)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)
    st.markdown(
    f"""
    <style>
    .highlighted-text {{
        font-size: 24px;
        font-weight: bold;
        color: #002366;
        text-align: center;
    }}
    .movie-name {{
        color: #FF5733; 
    }}
    </style>
    <div class='highlighted-text'>Top 10 recommended movies for you if you liked <span class='movie-name'>{selected_movie_name}</span></div>
    """,
    unsafe_allow_html=True
)
    # Customizing the layout with HTML/CSS
    st.markdown(
        """
        <style>
        .movie-title {
            font-size: 20px;
            font-weight: bold;
            color: #4CAF50;
            text-align: center;
        }
        .movie-poster {
            display: flex;
            justify-content: center;
            padding: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Adjust the layout to show all 10 movies in a grid
    num_columns = 5
    rows = len(names) // num_columns + (len(names) % num_columns > 0)
    
    for row in range(rows):
        cols = st.columns(num_columns)
        for i in range(num_columns):
            index = row * num_columns + i
            if index < len(names):
                cols[i].markdown(f"<div class='movie-title'>{names[index]}</div>", unsafe_allow_html=True)
                cols[i].markdown(f"<div class='movie-poster'><img src='{posters[index]}' width='100'></div>", unsafe_allow_html=True)
