#fancy indexing
import numpy as np

arr = np.empty((8, 4))
for i in range(8):
    arr[i] = i

print(arr)

print(arr[[4, 3, 0, 6]])
print(arr[[-3, -5, -7]])

arr = np.arange(32).reshape((8, 4))
print(arr)
print(arr[[1, 5, 7, 2], [0, 3, 1, 2]])

#transponowanie tablic i zamiana osi
arr2 = np.arange(100).reshape((20, 5))
print(arr2)
print(arr2.T)
arr4 = np.arange(1, 16).reshape((5,3))

#mnożenie macierzy poprzez np.dot i @
arr3 = np.array([[0, 1, 0], [1, 2, -2], [6, 3, 2], [-1, 0, -1], [1, 0, 1]])
print(arr3)

#np.dot
print(np.dot(arr3.T, arr3))

#@
print(arr3.T @ arr3)

#moje
print((arr3))
print(arr3.swapaxes(1, 2))