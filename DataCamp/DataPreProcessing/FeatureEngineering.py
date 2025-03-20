import pandas as pd
from sklearn.preprocessing import LabelEncoder

#1
# Wczytanie pliku CSV
hiking = pd.read_csv("Hiking.csv")

# Usunięcie ewentualnych spacji w nazwach kolumn
hiking.columns = hiking.columns.str.strip()

# Inicjalizacja obiektu LabelEncoder
enc = LabelEncoder()

# Zakodowanie kolumny "Accessible"
hiking["Accessible_enc"] = enc.fit_transform(hiking["Accessible"])

# Wyświetlenie porównania
print(hiking[["Accessible", "Accessible_enc"]].head())

#2
# Transform the category_desc column
category_enc = pd.get_dummies(hiking["Accessible"])

# Take a look at the encoded columns
print(category_enc.head())