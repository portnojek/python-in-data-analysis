import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

# Dane wejściowe
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

# Podział na zbiór treningowy i testowy z zachowaniem proporcji klas
X_train, X_test, y_train, y_test = train_test_split(
    X, y, stratify=y, random_state=42
)

# Tworzenie i trenowanie modelu
nb = MultinomialNB()
nb.fit(X_train, y_train)

# Ocena modelu
accuracy = nb.score(X_test, y_test)
print(f"Dokładność modelu: {accuracy:.2f}")
