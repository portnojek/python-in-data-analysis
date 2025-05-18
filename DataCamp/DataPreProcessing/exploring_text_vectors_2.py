'''
Exploring text vectors, part 2
Using the return_weights() function you wrote in the previous exercise, you're now going to extract the top words from each document in the text vector, return a list of the word indices, and use that list to filter the text vector down to those top words.

Instructions
100 XP
Call return_weights() to return the top weighted words for that document.
Call set() on the returned filter_list to remove duplicated numbers.
Call words_to_filter, passing in the following parameters: vocab for the vocab parameter, tfidf_vec.vocabulary_ for the original_vocab parameter, text_tfidf for the vector parameter, and 3 to grab the top_n 3 weighted words from each document.
Finally, pass that filtered_words set into a list to use as a filter for the text vector.
'''
from sklearn.feature_extraction.text import TfidfVectorizer

from DataCamp.DataPreProcessing.exploring_text_vectors_1 import return_weights

'''
def words_to_filter(vocab, original_vocab, vector, top_n):
    filter_list = []
    for i in range(0, vector.shape[0]):
    
        # Call the return_weights function and extend filter_list
        filtered = ____(vocab, original_vocab, vector, i, top_n)
        filter_list.extend(filtered)
        
    # Return the list in a set, so we don't get duplicate word indices
    return ____(filter_list)

# Call the function to get the list of word indices
filtered_words = ____(____, ____, ____, ____)

# Filter the columns in text_tfidf to only those in filtered_words
filtered_text = text_tfidf[:, list(____)]
'''
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
import pandas as pd


def words_to_filter(vocab, original_vocab, vector, top_n):
    filter_list = []
    for i in range(0, vector.shape[0]):
        # Call the return_weights function and extend filter_list
        filtered = return_weights(vocab, original_vocab, vector, i, top_n)
        filter_list.extend(filtered)

    # Return the list in a set, so we don't get duplicate word indices
    return set(filter_list)


# Call the function to get the list of word indices
filtered_words = words_to_filter(vocab, tfidf_vec.vocabulary_, text_tfidf, 3)

# Filter the columns in text_tfidf to only those in filtered_words
filtered_text = text_tfidf[:, list(filtered_words)]