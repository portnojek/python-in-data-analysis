from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import make_classification
import pandas as pd

#Generowanie syntetycznych danych
X, y = make_classification(n_samples=100, n_features=5, n_informative=3, n_classes=2, random_state=42)

#Konwersja do DataFrame
df = pd.DataFrame(X, columns=[f'feature_{i+1}' for i in range(5)])
df['label'] = y

#zapisanie do pliku CSV
df.to_csv('synthetic_dataset.csv', index=False)

#Split the dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=42)

knn = KNeighborsClassifier()

#Fit the knn model to the training data
knn.fit(X_train, y_train)

#Score the model on the test data
print(knn.score(X_test, y_test))