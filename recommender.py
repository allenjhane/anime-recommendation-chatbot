# recommender.py

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def load_anime_data(path="data/anime.csv"):
    """
    Loads your anime dataset from CSV.
    Returns a DataFrame with at least 'name' and 'genre' columns.
    """
    df = pd.read_csv(path)
    # Drop rows missing genre or name
    df = df.dropna(subset=['name', 'genre'])
    return df

def recommend_anime(title, df, top_n=5):
    """
    Given an anime title and the DataFrame, returns a list of 'top_n'
    most similar anime (by genre).
    """
    # Build TF-IDF matrix on genres
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(df['genre'])

    # Compute cosine similarity
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

    # Map titles to indices
    indices = pd.Series(df.index, index=df['name']).drop_duplicates()

    idx = indices.get(title)
    if idx is None:
        return [f"No match for '{title}'. Try another anime name."]

    # Get similarity scores, sort most similar first (skip self)
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1 : top_n+1]

    # Return the names of the top matches
    rec_indices = [i for i, _ in sim_scores]
    return df['name'].iloc[rec_indices].tolist()
