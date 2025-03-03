from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

# Podział danych na zbiory treningowe i testowe
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=42)

# Inicjalizacja klasyfikatora KNN i skalera
knn = KNeighborsClassifier()
scaler = StandardScaler()

# Skalowanie danych treningowych
X_train_scaled = scaler.fit_transform(X_train)

# Skalowanie danych testowych
X_test_scaled = scaler.transform(X_test)

# Trenowanie modelu KNN
knn.fit(X_train_scaled, y_train)

# Ocena modelu na zbiorze testowym
score = knn.score(X_test_scaled, y_test)
print(f"Dokładność modelu: {score:.2f}")
