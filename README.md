# SameSame Movie: A Content-Based Recommender

An interactive movie recommendation system built with **Python** and **Streamlit**. This application uses a **content-based filtering** approach with **TF-IDF** and **Cosine Similarity** to suggest movies that are thematically and stylistically similar based on their genres and user-generated tags.

-----

## Table of Contents

  - [1. Project Vision & Problem Statement](https://www.google.com/search?q=%231-project-vision--problem-statement)
  - [2. The Recommendation Engine: How It Works](https://www.google.com/search?q=%232-the-recommendation-engine-how-it-works)
  - [3. Core Features & Functionality](https://www.google.com/search?q=%233-core-features--functionality)
  - [4. Project Structure Explained](https://www.google.com/search?q=%234-project-structure-explained)
  - [5. Technical Stack](https://www.google.com/search?q=%235-technical-stack)
  - [6. Local Setup & Usage Guide](https://www.google.com/search?q=%236-local-setup--usage-guide)
  - [7. Author & License](https://www.google.com/search?q=%237-author--license)

-----

## 1\. Project Vision & Problem Statement

In the vast landscape of cinema, discovering a new movie that truly matches your taste can be challenging. Many recommendation systems rely on what other users watch (collaborative filtering), which can lead to popularity bias and may not capture the specific "vibe" of a movie.

The vision for **SameSame Movie** is to solve this by providing recommendations based on a movie's intrinsic **content**. By analyzing the combination of genres and descriptive tags, this system identifies movies that share a similar thematic DNA, helping users discover hidden gems and titles that genuinely align with their preferences.

-----

## 2\. The Recommendation Engine: How It Works

The application implements a classic content-based filtering pipeline using Natural Language Processing (NLP) techniques.

### Step 1: Data Loading & Preprocessing

  - The MovieLens dataset, containing `movies.csv`, `tags.csv`, and other files, is loaded using Pandas.
  - For each movie, the genres and all user-generated tags are combined into a single text string, or "content soup." This string acts as a rich descriptor of the movie's themes and style.

### Step 2: Text Vectorization with TF-IDF

  - To enable mathematical comparison, the textual "content soup" for each movie is converted into a numerical vector using the **`TfidfVectorizer`** from Scikit-learn.
  - **TF-IDF (Term Frequency-Inverse Document Frequency)** assigns a weight to each word (genre or tag), emphasizing terms that are highly characteristic of a specific movie but relatively rare across the entire dataset.

### Step 3: Calculating Similarity with Cosine Similarity

  - With all movies represented as numerical TF-IDF vectors, their similarity can be calculated. **Cosine Similarity** measures the cosine of the angle between two vectors in a multi-dimensional space.
  - A similarity score close to 1 indicates that two movies are very similar in content, while a score near 0 indicates they are dissimilar. A matrix containing these scores for all pairs of movies is computed.

### Step 4: Generating Recommendations

  - When a user selects a movie, the system finds its corresponding vector and uses the pre-computed similarity matrix to identify the top 'n' most similar movies.
  - These top movies are then presented to the user as recommendations.

-----

## 3\. Core Features & Functionality

  - **Content-Based Engine:** Recommendations are driven by the movie's core content (genres and tags), providing thematically relevant suggestions.
  - **Fuzzy Search:** Implements fuzzy string matching to handle typos and partial movie titles, ensuring a smooth user search experience.
  - **Top 100 Popular Movies Dropdown:** An alternative discovery path for users who are unsure what to search for, featuring a curated list of popular titles.
  - **Rich Visual Output:** Recommendations are displayed as interactive cards, featuring the movie poster and direct links to **IMDb, TMDb, and Google Search** for further exploration.
  - **Interactive UI:** A clean, modern, and responsive user interface built with Streamlit makes the application accessible and easy to use.

-----

## 4\. Project Structure Explained

```
movie_recommendation_MRS/
│
├── data/
│   ├── movies.csv          # Core movie data with titles and genres.
│   ├── tags.csv            # User-generated tags for movies.
│   └── ...                 # Other dataset files like ratings.csv.
│
├── movie_recommender.py    # Python script containing the core recommendation logic.
├── app.py                  # The main Streamlit application script for the frontend UI.
├── requirements.txt        # A list of all Python dependencies.
└── README.md               # This detailed project documentation.
```

-----
![MRA](https://github.com/user-attachments/assets/2b8c0a97-3a05-44d3-9252-14b6678e16f0)
## 5\. Technical Stack

  - **Core Language:** Python
  - **Web Framework:** Streamlit
  - **Data Manipulation:** Pandas
  - **Machine Learning / NLP:** Scikit-learn
      - **Text Vectorization:** `TfidfVectorizer`
      - **Similarity Metric:** `cosine_similarity`
  - **Fuzzy Matching:** `fuzzywuzzy` (or similar)

-----

## 6\. Local Setup & Usage Guide

To run this application on your local machine, please follow these steps.

### Step 1: Clone the Repository

```bash
git clone https://github.com/MrCoss/movie-recommendation-MRS.git
cd movie-recommendation-MRS
```

### Step 2: Create and Activate a Virtual Environment (Recommended)

```bash
# Create the environment
python -m venv venv

# Activate on Windows
.\venv\Scripts\activate

# Activate on macOS/Linux
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Place Datasets

Ensure that the required `.csv` files (e.g., `movies.csv`, `tags.csv`) from the MovieLens dataset are placed inside the `data/` folder.

### Step 5: Run the Streamlit Application

```bash
streamlit run app.py
```

Your web browser will automatically open with the running application, typically at `http://localhost:8501`.

-----

## 7\. Author & License

  - **Author:** Costas Pinto
  - **GitHub:** [MrCoss](https://github.com/MrCoss)
  - **License:** This project is open-source and available for educational and personal use.
