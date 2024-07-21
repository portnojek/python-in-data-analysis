import timeit

import numpy as np
from random import normalvariate

#probki standardowego rozkladu normalnego
samples = np.random.standard_normal(size=(4,4))
print(samples)

rng = np.random.default_rng(seed=12345) #seed oznacza stan generatora, stan zmienia się po każdorazowym wygenerowaniu danych za pomocą argumentu rng
data = rng.standard_normal(((2, 3)))
print(data)

data2 = rng.permutation(1, 2)
print(data2)

#funkcje uniwersalne (jednoargumentowe)

arr = np.arange(10)
sqrt = np.sqrt(arr)
exp = np.exp(arr)

print(sqrt)
print(exp)

#przykłady użycia uniwersalnych funkcji jednoargumentowych

# Tworzenie przykładowej tablicy
a = np.array([1, -2, 3.5, -4.7])

# Wartość bezwzględna
print("np.abs(a):", np.abs(a))

# Pierwiastek kwadratowy
print("np.sqrt(np.abs(a)):", np.sqrt(np.abs(a)))

# Funkcja wykładnicza
print("np.exp(a):", np.exp(a))

# Logarytm naturalny (wartości muszą być dodatnie)
print("np.log(np.abs(a) + 1):", np.log(np.abs(a) + 1))

# Sinus
print("np.sin(a):", np.sin(a))

# Najbliższa większa liczba całkowita
print("np.ceil(a):", np.ceil(a))

# Najbliższa mniejsza liczba całkowita
print("np.floor(a):", np.floor(a))

# Argument (kąt) dla liczb zespolonych
b = np.array([1+2j, 3-4j])
print("np.angle(b):", np.angle(b))

#funkcje uniwersalne (dwuargumentowe)
x = rng.standard_normal(8)
y = rng.standard_normal(8)
print(x, y)
print(np.maximum(x, y))

#przykłady użycia uniwersalnych funkcji dwuargumentowych

# Tworzenie przykładowych tablic
a = np.array([1, 2, 3, 4])
b = np.array([4, 3, 2, 1])

# Dodawanie
print("np.add(a, b):", np.add(a, b))

# Odejmowanie
print("np.subtract(a, b):", np.subtract(a, b))

# Mnożenie
print("np.multiply(a, b):", np.multiply(a, b))

# Dzielenie
print("np.divide(a, b):", np.divide(a, b))

# Potęgowanie
print("np.power(a, b):", np.power(a, b))

# Modulo
print("np.mod(a, b):", np.mod(a, b))

# Porównania
print("np.greater(a, b):", np.greater(a, b))
print("np.less(a, b):", np.less(a, b))
print("np.equal(a, b):", np.equal(a, b))

# Maksimum i minimum
print("np.maximum(a, b):", np.maximum(a, b))
print("np.minimum(a, b):", np.minimum(a, b))

# Funkcje trigonometryczne
print("np.arctan2(a, b):", np.arctan2(a, b))

# Długość przeciwprostokątnej
print("np.hypot(a, b):", np.hypot(a, b))

#programowanie z użyciem tablic
#numpy.meshgrid przyjmuje dwie tablice jednowymiarowe i generuje dwie dwuwymiarowe tablice
points = np.arange(-5, 5, 0.01) # 1000 równo oddalonych punktów
xs, ys  = np.meshgrid(points, points)
print(ys)

#obliczenie wartości funkcji
z = np.sqrt(xs ** 2 + ys ** 2)
print(z)

import matplotlib.pyplot as plt
plt.imshow(z, cmap=plt.cm.gray, extent=(-5, 5, -5, 5))
plt.colorbar()
plt.title("Wykres funkcji $\sqrt{X^2 + y^2}$ dla określonych wartości x i y")
plt.show()
plt.close()

#logiczne operacje warunkowe
xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
cond = np.array([True, False, True, True, False])

result = np.where(cond, xarr, yarr) #jeśli spełniony warunek dla True to zwraca wartość odpowiednią dla xarr, jeśli nie spełnia warunku to zwraca yarr
print(result)

#odpowiednikiem dla tego działania w czystym Pythonie będzie:
result2 = [(x if c else y)
for x, y , c in zip(xarr, yarr, cond)]
print(result2)

#example
arr = np.random.standard_normal((4, 4))
print(np.where(arr>0, 2, -2)) #zamiana wszystkich dodatnich liczb na 2 i ujemnych na -2
print(np.where(arr>0, "barabasz", arr))#zamiana wszystkich dodatnich liczb na barabasz i dla ujemnych pozostaje bez zmian