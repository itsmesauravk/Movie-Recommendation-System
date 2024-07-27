# Movie Recommendation System

This project is a movie recommendation system that suggests movies similar to a selected movie. The system uses a dataset of movies and provides recommendations based on the similarity of the movies.

## Features

- Load a dataset of movies
- Recommend similar movies based on a selected movie
- Display movie posters alongside their titles
- User-friendly interface with Streamlit
- Styled using custom CSS for a better visual experience

## Dataset Link (Kaggle)

Link : https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/movie-recommendation-system.git
   cd movie-recommendation-system
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```bash
   streamlit run app.py
   ```

## Dataset

The dataset used in this project is stored in the form of a dictionary, which is loaded using the `pickle` library. Ensure you have the following files in your project directory:

- `movies_dict.pkl`
- `similarity.pkl`

## File Structure

```
movie-recommendation-system/
│
├── app.py               # Main Streamlit application
├── movies_dict.pkl      # Dataset of movies
├── similarity.pkl       # Precomputed similarity matrix
├── requirements.txt     # List of required packages
└── README.md            # This readme file
```

## Usage

1. **Open the application:**

   ```bash
   streamlit run app.py
   ```

2. **Select a movie from the dropdown menu:**
   The dropdown contains a list of movie titles from the dataset.

3. **Click the 'Recommend' button:**
   The application will display the top 10 movies similar to the selected movie, along with their posters.

## Customization

You can customize the style of the application using the provided CSS in the `app.py` file. For instance, you can change the color of the movie titles and posters as shown in the example below:

```python
st.markdown(
    """
    <style>
    .highlighted-text {
        font-size: 24px;
        font-weight: bold;
        color: #4CAF50;
        text-align: center;
    }
    .movie-name {
        color: #FF5733;  /* Different color for the movie name */
    }
    </style>
    <div class='highlighted-text'>Top 10 recommended movies for you if you liked <span class='movie-name'>{selected_movie_name}</span></div>
    """,
    unsafe_allow_html=True
)
```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue.

## License

This project is licensed under the MIT License.

---

Happy coding! If you have any questions, feel free to reach out.
