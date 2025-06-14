import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from rapidfuzz import process
import urllib.parse

# Load data
movies = pd.read_csv('data/movies.csv')
ratings = pd.read_csv('data/ratings.csv')
tags = pd.read_csv('data/tags.csv')
links = pd.read_csv('data/links.csv')

# Combine genres and tags
tags_grouped = tags.groupby('movieId')['tag'].apply(lambda x: ' '.join(x)).reset_index()
movies = pd.merge(movies, tags_grouped, on='movieId', how='left')
movies['tag'] = movies['tag'].fillna('')
movies['genres'] = movies['genres'].fillna('')
movies['combined'] = movies['genres'] + ' ' + movies['tag']

# Merge with links
movies = pd.merge(movies, links, on='movieId', how='left')

# Add popularity info
popularity = ratings.groupby('movieId')['rating'].count().reset_index()
popularity.columns = ['movieId', 'num_votes']
movies = pd.merge(movies, popularity, on='movieId', how='left')
movies['num_votes'] = movies['num_votes'].fillna(0)

# Filter popular movies (≥ 100 votes)
popular_movies = movies[movies['num_votes'] >= 100].copy()
popular_movies = popular_movies.drop_duplicates(subset='title')

# TF-IDF and cosine similarity
vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(movies['combined'])
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Title to index mapping
title_to_index = pd.Series(movies.index, index=movies['title']).drop_duplicates()
all_titles = sorted(popular_movies['title'].tolist())

# Helper to get closest match
def get_closest_title(user_input):
    match, score, _ = process.extractOne(user_input, all_titles)
    return match if score >= 60 else None

# Recommendation function
def recommend_movies(title, top_n=5):
    closest_title = get_closest_title(title)
    if not closest_title:
        return [f"❌ Movie '{title}' not found. Try another."]

    idx = title_to_index[closest_title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:top_n+1]

    results = []
    for i, _ in sim_scores:
        movie = movies.iloc[i]
        movie_id = movie['movieId']
        imdb_id = str(movie.get('imdbId')).zfill(7) if pd.notna(movie.get('imdbId')) else None
        tmdb_id = int(movie.get('tmdbId')) if pd.notna(movie.get('tmdbId')) else None

        imdb_link = f"https://www.imdb.com/title/tt{imdb_id}/" if imdb_id else "N/A"
        tmdb_link = f"https://www.themoviedb.org/movie/{tmdb_id}" if tmdb_id else "N/A"
        search_link = f"https://www.google.com/search?q={urllib.parse.quote(movie['title'] + ' movie')}"
        poster_url = f"https://img.omdbapi.com/?i=tt{imdb_id}&h=400&apikey=b044d975" if imdb_id else None

        avg_rating = ratings[ratings['movieId'] == movie_id]['rating'].mean()
        num_votes = ratings[ratings['movieId'] == movie_id]['rating'].count()

        results.append({
            'title': movie['title'],
            'rating': round(avg_rating, 2) if not pd.isna(avg_rating) else "N/A",
            'votes': num_votes,
            'search_link': search_link,
            'imdb_link': imdb_link,
            'tmdb_link': tmdb_link,
            'poster': poster_url
        })

    return closest_title, results
