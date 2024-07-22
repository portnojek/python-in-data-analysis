import pandas as pd
from pandas import Series, DataFrame
import numpy as np

obj = pd.Series([4, 5, -7, 3])
print(obj)
print(obj.array)
print(obj.index)

#obiekt Series z indeksem identyfikującym każdy element serii za pomocą etykiety
obj2 = pd.Series([4, 5, -7, 3], index=['d', 'b', 'a', 'c'])
print(obj2)
print(obj2['a'])
obj2['d']= 6
print(obj2[['c', 'a', 'd']])
print(obj2[obj2 > 0])
print(obj2 * 2)
print(np.exp(obj2)) # oblicza wartość wykładniczą każdego elementu w podanej tablicy
print('b' in obj2)
print('e' in obj2)

# zamiana słownika na serię
sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
obj3 = pd.Series(sdata)
print(obj3)
print(obj3.to_dict()) #zamiana z powrotem na słownik

#zamiana kolejności generowania wartości ze słownika
states = ['California', 'Ohio', 'Oregon', 'Texas']
obj4 = pd.Series(sdata, index=states)
print(obj4)
print(pd.isnull(obj4))
print(pd.notnull(obj4))
print(obj4.isnull())
print(obj3)
print(obj4)
print(obj3 + obj4)

#nadawanie atrybutu name dla serii oraz indeksów
obj4.name = 'population'
obj4.index.name = 'state'
print(obj4)

print(obj)
obj.index = ['Bob', 'Steve', 'Jeff', 'Ryan']
print(obj)