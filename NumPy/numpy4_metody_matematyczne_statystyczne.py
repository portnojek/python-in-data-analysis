import numpy as np

rng = np.random.default_rng(seed=12345)
arr = rng.standard_normal((5, 4))

#different methods
print(arr)
print(arr.mean())
print(np.mean(arr))
print(arr.sum())
print(arr.mean(axis=1))
print(arr.sum(axis=0))
print("")
print(arr.cumsum(axis=0))
print("")
arr2 = np.arange(8)
print(arr2.cumsum())

#metody tablic logicznych
arr3  = rng.standard_normal(100)
print((arr3>0).sum())
print((arr3<0).sum())

#metody any i all
bools = np.array([False, False, True, False])
print(bools.any())
print(bools.all())

#sortowanie
arr4 = rng.standard_normal(6)

print(arr4)
arr4.sort()
print(arr4)

#sortowanie na tablicy; axis=0 sortuje wg wierszy a axis=1 sortuje wg kolumn
arr5 = rng.standard_normal((5, 3))
print(arr5)
arr5.sort(axis=0)
print(arr5)

arr5.sort(axis=1)
print(arr5)

#wartości unikalne
names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
print(np.unique(names))

#odpowiednik w czystym Pythonie
print(sorted(set(names)))

#funkcja np.inld (od wersji 2.0 jest to np.isin)
values = np.array([6, 0, 0, 3, 2, 5, 6])
print(np.isin(values, [2, 3, 6]))