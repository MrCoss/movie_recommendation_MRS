# 🎮 Movie Recommendation System

This is a content-based movie recommendation system built using Python, Streamlit, and machine learning libraries like scikit-learn. It suggests similar movies based on genres and tags using TF-IDF and cosine similarity.
![MRA](https://github.com/user-attachments/assets/2b8c0a97-3a05-44d3-9252-14b6678e16f0)

## 🚀 Features

* 🔍 Fuzzy search for movie titles
* 🕽️ Dropdown of top 100 popular movies
* 🎞️ Movie posters with links to IMDb, TMDb, and Google Search
* 🌐 Interactive UI built with Streamlit

## 📁 Folder Structure

```
movie_recommendation_MRS/
│
├── data/                  # CSV files (movies.csv, ratings.csv, etc.)
├── movie_recommender.py   # Core logic and recommendation functions
├── app.py                 # Streamlit UI
└── README.md              # Project description
```

## 🛆 Requirements

Install dependencies using:

```bash
pip install -r requirements.txt
```

> You can create this file with:
> `pip freeze > requirements.txt`

## 🧠 How it Works

* Uses TF-IDF Vectorizer to encode genres and tags
* Cosine similarity finds similar movies
* Fuzzy matching helps handle typos in movie names
* Popular movies dropdown helps with discoverability

## ▶️ Run the App

```bash
streamlit run app.py
```

Then open your browser at [http://localhost:8501](http://localhost:8501)

## 📸 Sample UI

![Movie Recommender Screenshot](https://via.placeholder.com/600x400?text=Add+Screenshot)

---

Made with ❤️ using Python & Streamlit.
