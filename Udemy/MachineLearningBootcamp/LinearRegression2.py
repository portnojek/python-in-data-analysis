import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Dane przykładowe
x = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)  # zmienne niezależne
y = np.array([2, 4, 5, 4, 5])                # zmienne zależne

# Model regresji
model = LinearRegression()
model.fit(x, y)

# Współczynniki
print(f"Współczynnik nachylenia: {model.coef_[0]}")
print(f"Wyraz wolny: {model.intercept_}")

# Wykres
plt.scatter(x, y, color="blue", label="Dane")
plt.plot(x, model.predict(x), color="red", label="Linia regresji")
plt.legend()
plt.show()
