import streamlit as st
from movie_recommender import recommend_movies, all_titles

st.set_page_config(page_title="🎬 Movie Recommender", layout="centered")

st.title("🎬 SameSameMovie")
st.write("Discover movies similar to your favorites!")

# Dropdown for popular movies
movie_input = st.selectbox("Select a popular movie:", all_titles, index=None, placeholder="Start typing...")

# On click
if movie_input:
    st.markdown("🔍 Searching for similar movies...")
    result = recommend_movies(movie_input)

    if isinstance(result, list):
        st.error(result[0])
    else:
        closest_title, recommendations = result
        st.success(f"✨ Recommendations based on: **{closest_title}**")

        for i, movie in enumerate(recommendations, start=1):
            st.markdown(f"### {i}. {movie['title']}")
            col1, col2 = st.columns([1, 3])
            with col1:
                if movie['poster']:
                    st.image(movie['poster'], width=120)
            with col2:
                st.write(f"⭐ **Rating**: {movie['rating']} ({movie['votes']} votes)")
                st.markdown(f"[IMDb 🔗]({movie['imdb_link']}) &nbsp;&nbsp; [TMDb 🔗]({movie['tmdb_link']})")
                st.markdown(f"[🔍 Google it]({movie['search_link']})")
