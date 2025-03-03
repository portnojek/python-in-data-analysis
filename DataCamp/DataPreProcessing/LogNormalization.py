import numpy as np
import pandas as pd

# Załóżmy, że mamy DataFrame o nazwie 'wine'
# wine = pd.read_csv('wine_dataset.csv')  # Odkomentuj tę linię, jeśli chcesz wczytać dane z pliku CSV

# Przykładowe dane, jeśli nie masz pliku CSV
wine = pd.DataFrame({
    'Proline': [1065, 1050, 1185, 1480, 735]
})

# Print out the variance of the Proline column
print(wine["Proline"].var())

# Apply the log normalization function to the Proline column
wine["Proline_log"] = np.log(wine["Proline"])

# Check the variance of the normalized Proline column
print(wine["Proline_log"].var())

print(np.log(30))
print(np.log(300))
print(np.log(3000))