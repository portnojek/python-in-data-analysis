#mnożenie macierzy
import numpy as np

x = np.array([[1., 2., 3.],[4., 5., 6.]])
y = np.array([[6., 23.], [-1., 7], [8,9]])

print(x.dot(y))
print(np.dot(x, y))

from numpy.linalg import inv, qr
rng = np.random.default_rng(seed=1234)
X = rng.standard_normal((5, 5))
mat = X.T.dot(X)

print(inv(mat))

#obliczenie iloczynu skalarnego tablicy X i jej transponowanej wersjij X.T.
trans = mat @ inv(mat)
print(trans)