from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

# Sample UFO dataset with a 'desc' column
data = {
    "length_of_time": ["5 minutes", "about 30 minutes", "10 mins", "1 minute", "45 minutes"],
    "seconds": [300, 1800, 600, 60, 2700],
    "country": ["us", "ca", "us", "gb", "us"],
    "type": ["light", "triangle", "disk", "light", "circle"],
    "desc": [
        "Bright light hovered in the sky for several minutes.",
        "Three lights in a triangular formation moving quickly.",
        "Disc-shaped object silently flying over the neighborhood.",
        "Small glowing light appeared and vanished instantly.",
        "Circular craft with blinking lights seen above the trees."
    ]
}

# Create DataFrame
ufo = pd.DataFrame(data)

# Take a look at the head of the desc field
print(ufo['desc'].head())

# Instantiate the tfidf vectorizer object
vec = TfidfVectorizer()

# Fit and transform desc using vec
desc_tfidf = vec.fit_transform(ufo['desc'])

# Look at the number of columns and rows
print(desc_tfidf.shape)
