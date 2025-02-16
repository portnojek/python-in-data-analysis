import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

#importujemy punkty
df = pd.read_csv('https://bit.ly/3goOAnt', delimiter=",")

#wyodrębniamy dane wejściowe (wszystkie wiersze, wszystkie kolumny oprócz ostatniej)
X = df.values[:, :-1]

#wyodrębniamy kolumnę wyjściową (wszystkie wiersz, ostatnia kolumna)
Y = df.values[:, -1]

#dopasowujemy linię do punktów
dopasowanie = LinearRegression().fit(X, Y)

m = dopasowanie.coef_.flatten()
b = dopasowanie.intercept_.flatten()

print("m = {0}".format(m))
print("b = {0}".format(b))

#pokazujemy na wykresie
plt.plot(X, Y, 'o') #wykres punktowy
plt.plot(X, m*X+b) #linia
plt.show()
