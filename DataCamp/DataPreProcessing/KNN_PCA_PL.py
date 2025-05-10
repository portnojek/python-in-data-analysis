# Importujemy potrzebne biblioteki
from sklearn.datasets import load_wine  # Dane o winach
from sklearn.model_selection import train_test_split  # Podział na trening/test
from sklearn.neighbors import KNeighborsClassifier  # Algorytm KNN
from sklearn.decomposition import PCA  # PCA - redukcja wymiarów
from sklearn.metrics import accuracy_score  # Do oceny trafności
import pandas as pd

# 1. Wczytanie danych o winach
wine_data = load_wine()
wine = pd.DataFrame(wine_data.data, columns=wine_data.feature_names)
wine["Type"] = wine_data.target  # Dodajemy kolumnę z etykietami (typ wina)

# 2. Podział danych na cechy (X) i etykiety (y)
X = wine.drop("Type", axis=1)  # Wszystko oprócz kolumny "Type"
y = wine["Type"]  # Etykiety

# 3. Podział na zbiór treningowy i testowy
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=42)

# 4. Trening modelu KNN na oryginalnych danych
knn = KNeighborsClassifier()
knn.fit(X_train, y_train)  # Uczymy model
y_pred_plain = knn.predict(X_test)  # Przewidujemy na testowym zbiorze
accuracy_plain = accuracy_score(y_test, y_pred_plain)  # Obliczamy trafność
print("Dokładność BEZ PCA:", accuracy_plain)

# 5. PCA - redukcja wymiarów
pca = PCA()
pca.fit(X_train)  # Uczymy PCA tylko na zbiorze treningowym
X_train_pca = pca.transform(X_train)
X_test_pca = pca.transform(X_test)

# 6. Trening modelu KNN na danych po PCA
knn_pca = KNeighborsClassifier()
knn_pca.fit(X_train_pca, y_train)
y_pred_pca = knn_pca.predict(X_test_pca)
accuracy_pca = accuracy_score(y_test, y_pred_pca)
print("Dokładność Z PCA:", accuracy_pca)