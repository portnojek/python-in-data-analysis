import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

# Pełny zbiór danych
data = {
    "length_of_time": [
        "5 minutes", "30 minutes", "10 mins", "1 minute", "45 minutes",
        "15 minutes", "20 minutes", "8 minutes", "2 minutes", "25 minutes",
        "35 minutes", "3 minutes", "7 minutes", "18 minutes", "28 minutes",
        "22 minutes", "40 minutes", "4 minutes", "9 minutes", "12 minutes"
    ],
    "seconds": [
        300, 1800, 600, 60, 2700,
        900, 1200, 480, 120, 1500,
        2100, 180, 420, 1080, 1680,
        1320, 2400, 240, 540, 720
    ],
    "country": [
        "us", "ca", "us", "gb", "us",
        "gb", "ca", "us", "us", "gb",
        "ca", "us", "us", "ca", "gb",
        "us", "ca", "gb", "us", "gb"
    ],
    "type": [
        "light", "triangle", "disk", "light", "circle",
        "circle", "triangle", "disk", "light", "light",
        "disk", "light", "triangle", "triangle", "circle",
        "disk", "light", "circle", "triangle", "circle"
    ]
}

# Tworzenie DataFrame
ufo = pd.DataFrame(data)

# Zakodowanie kraju jako 1 (us) lub 0 (inne)
ufo["country_enc"] = ufo["country"].apply(lambda x: 1 if x == "us" else 0)

# Przygotowanie cech i etykiet
X = ufo[["seconds", "country_enc"]]
y = ufo["type"]

# Podział na zbiory treningowy i testowy z zachowaniem proporcji klas
X_train, X_test, y_train, y_test = train_test_split(
    X, y, stratify=y, random_state=42
)

# Przykład 1: KNN bez skalowania
knn = KNeighborsClassifier()
knn.fit(X_train, y_train)
print(f"Dokładność bez skalowania: {knn.score(X_test, y_test):.2f}")

# Przykład 2: KNN ze skalowaniem
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
knn.fit(X_train_scaled, y_train)
print(f"Dokładność ze skalowaniem: {knn.score(X_test_scaled, y_test):.2f}")
print(data)
print(ufo)
