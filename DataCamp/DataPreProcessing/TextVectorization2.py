import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

# Sample UFO dataset
ufo = pd.DataFrame({
    "city": ["seattle", "vancouver", "new york", "london", "los angeles"],
    "country": ["us", "ca", "us", "gb", "us"],
    "lat": [47.6062, 49.2827, 40.7128, 51.5074, 34.0522],
    "long": [-122.3321, -123.1207, -74.0060, -0.1278, -118.2437],
    "state": ["wa", "bc", "ny", "ldn", "ca"],
    "date": ["2020-01-01", "2020-01-05", "2020-02-01", "2020-02-20", "2020-03-15"],
    "recorded": ["2020-01-10", "2020-01-15", "2020-02-05", "2020-02-25", "2020-03-20"],
    "seconds": [300, 1800, 600, 60, 2700],
    "minutes": [5, 30, 10, 1, 45],
    "length_of_time": ["5 minutes", "about 30 minutes", "10 mins", "1 minute", "45 minutes"],
    "desc": [
        "Bright light hovered in the sky for several minutes.",
        "Three lights in a triangular formation moving quickly.",
        "Disc-shaped object silently flying over the neighborhood.",
        "Small glowing light appeared and vanished instantly.",
        "Circular craft with blinking lights seen above the trees."
    ],
    "type": ["light", "triangle", "disk", "light", "circle"]
})

# Instantiate and apply TF-IDF vectorizer
vec = TfidfVectorizer()
desc_tfidf = vec.fit_transform(ufo['desc'])

# Define vocab using feature names from the vectorizer
vocab = vec.get_feature_names_out()

# Make a list of features to drop
to_drop = ['city', 'country', 'lat', 'long', 'state', 'date', 'recorded', 'seconds', 'minutes', 'length_of_time', 'desc']

# Drop those features
ufo_dropped = ufo.drop(columns=to_drop)

# Define words_to_filter function (example implementation)
def words_to_filter(vocab, vocab_dict, tfidf_matrix, top_n):
    import numpy as np
    word_scores = tfidf_matrix.sum(axis=0).A1  # sum tfidf scores for each word
    top_indices = word_scores.argsort()[::-1][:top_n]  # get indices of top words
    return [vocab[i] for i in top_indices]

# Now call words_to_filter with vocab as the first argument
filtered_words = words_to_filter(vocab, vec.vocabulary_, desc_tfidf, 4)

# Optional: check output
print("Filtered top 4 words:", filtered_words)
