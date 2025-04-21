'''Training Naive Bayes with feature selection
You'll now re-run the Naive Bayes text classification model that you ran at the end of Chapter 3 with our selection choices from the previous exercise: the volunteer dataset's title and category_desc columns.

Instructions
100 XP
Use train_test_split() on the filtered_text text vector, the y labels (which is the category_desc labels), and pass the y set to the stratify parameter, since we have an uneven class distribution.
Fit the nb Naive Bayes model to X_train and y_train.
Calculate the test set accuracy of nb.'''


'''
# Split the dataset according to the class distribution of category_desc
X_train, X_test, y_train, y_test = ____(____.toarray(), ____, stratify=____, random_state=42)

# Fit the model to the training data
nb.____

# Print out the model's accuracy
print(nb.____)
'''

from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

# Split the dataset according to the class distribution of category_desc
X_train, X_test, y_train, y_test = train_test_split(filtered_text.toarray(), y, stratify=y, random_state=42)

# Fit the model to the training data
nb = MultinomialNB()
nb.fit(X_train, y_train)

# Print out the model's accuracy
print(nb.score(X_test, y_test))