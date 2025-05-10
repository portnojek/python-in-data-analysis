'''
Using PCA
In this exercise, you'll apply PCA to the wine dataset, to see if you can increase the model's accuracy.

Instructions
100 XP
Instantiate a PCA object.
Define the features (X) and labels (y) from wine, using the labels in the "Type" column.
Apply PCA to X_train and X_test, ensuring no data leakage, and store the transformed values as pca_X_train and pca_X_test.
Print out the .explained_variance_ratio_ attribute of pca to check how much variance is explained by each component.

# Instantiate a PCA object
pca = ____()

# Define the features and labels from the wine dataset
X = wine.drop(____, ____)
y = wine["Type"]

X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=42)

# Apply PCA to the wine dataset X vector
pca_X_train = ___.____(____)
pca_X_test = ___.____(____)

# Look at the percentage of variance explained by the different components
print(____)
'''

from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_wine
import pandas as pd

# Load wine dataset
wine_data = load_wine()
wine = pd.DataFrame(wine_data.data, columns=wine_data.feature_names)
wine["Type"] = wine_data.target

# Instantiate a PCA object
pca = PCA()

# Define the features and labels from the wine dataset
X = wine.drop("Type", axis=1)
y = wine["Type"]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=42)

# Apply PCA to the wine dataset X vector
pca.fit(X_train)  # Fit PCA only on training data to avoid data leakage
pca_X_train = pca.transform(X_train)
pca_X_test = pca.transform(X_test)

# Look at the percentage of variance explained by the different components
print(pca.explained_variance_ratio_)

'''
This ensures:
	•	PCA is fit only on X_train (avoiding data leakage).
	•	pca_X_train and pca_X_test are the PCA-transformed versions of the train/test features.
	•	The explained_variance_ratio_ shows how much variance each principal component explains.

Would you like to visualize the variance explained or choose the optimal number of components?
'''

import matplotlib.pyplot as plt
import numpy as np

# Calculate cumulative explained variance
cumulative_variance = np.cumsum(pca.explained_variance_ratio_)

# Plot cumulative explained variance
plt.figure(figsize=(8, 5))
plt.plot(range(1, len(cumulative_variance) + 1), cumulative_variance, marker='o', linestyle='--')
plt.title('Cumulative Explained Variance by PCA Components')
plt.xlabel('Number of Principal Components')
plt.ylabel('Cumulative Explained Variance')
plt.grid(True)
plt.axhline(y=0.95, color='r', linestyle=':')  # Optional: Show 95% threshold
plt.show()

'''

Training a model with PCA
Now that you have run PCA on the wine dataset, you'll finally train a KNN model using the transformed data.

Instructions
100 XP
Fit the knn model to the PCA-transformed features, pca_X_train, and training labels, y_train.
Print the test set accuracy of the knn model using pca_X_test and y_test.

from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Instantiate the KNN classifier
knn = KNeighborsClassifier()

# Fit the model to the PCA-transformed training data
knn.fit(pca_X_train, y_train)

# Predict using the test set
y_pred = knn.predict(pca_X_test)

# Print the test set accuracy
print("Test set accuracy with PCA:", accuracy_score(y_test, y_pred))
'''

from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Instantiate the KNN classifier
knn = KNeighborsClassifier()

# Fit the model to the PCA-transformed training data
knn.fit(pca_X_train, y_train)

# Predict using the test set
y_pred = knn.predict(pca_X_test)

# Print the test set accuracy
print("Test set accuracy with PCA:", accuracy_score(y_test, y_pred))

from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_wine
import pandas as pd
from sklearn.decomposition import PCA

# Load and prepare the wine dataset
wine_data = load_wine()
wine = pd.DataFrame(wine_data.data, columns=wine_data.feature_names)
wine["Type"] = wine_data.target

X = wine.drop("Type", axis=1)
y = wine["Type"]

X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=42)

# ---------- Without PCA ----------
knn_plain = KNeighborsClassifier()
knn_plain.fit(X_train, y_train)
y_pred_plain = knn_plain.predict(X_test)
plain_accuracy = accuracy_score(y_test, y_pred_plain)
print("Test set accuracy WITHOUT PCA:", plain_accuracy)

# ---------- With PCA ----------
pca = PCA()
pca.fit(X_train)
pca_X_train = pca.transform(X_train)
pca_X_test = pca.transform(X_test)

knn_pca = KNeighborsClassifier()
knn_pca.fit(pca_X_train, y_train)
y_pred_pca = knn_pca.predict(pca_X_test)
pca_accuracy = accuracy_score(y_test, y_pred_pca)
print("Test set accuracy WITH PCA:", pca_accuracy)