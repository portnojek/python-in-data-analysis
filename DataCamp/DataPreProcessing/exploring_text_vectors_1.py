import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

# Przykładowe dane tekstowe
texts = [
    "UFO sighting in California",
    "Bright light in the sky",
    "Flying object hovered over the city",
    "UFO appeared and disappeared quickly",
    "Triangle shaped UFO spotted in Nevada"
]

# Utworzenie i dopasowanie TF-IDF
tfidf_vec = TfidfVectorizer()
text_tfidf = tfidf_vec.fit_transform(texts)

# Słownik indeksów -> słów
vocab = {v: k for k, v in tfidf_vec.vocabulary_.items()}

# Funkcja do wyciągania najwyżej ocenionych słów
def return_weights(vocab, original_vocab, vector, vector_index, top_n):
    zipped = dict(zip(vector[vector_index].indices, vector[vector_index].data))
    zipped_series = pd.Series({vocab[i]: zipped[i] for i in vector[vector_index].indices})
    zipped_index = zipped_series.sort_values(ascending=False)[:top_n].index
    return [original_vocab[i] for i in zipped_index]

# Użycie funkcji
print(return_weights(
    vocab=vocab,
    original_vocab=tfidf_vec.vocabulary_,
    vector=text_tfidf,
    vector_index=1,  # np. 1. dokument w liście
    top_n=3
))