import numpy as np
from numpy.linalg import inv, qr, eig, svd, det, solve, lstsq, norm, cholesky, pinv

# 1. inv - Oblicza macierz odwrotną
A = np.array([[1, 2], [3, 4]])
A_inv = inv(A)
print("Macierz odwrotna A:\n", A_inv)

# 2. qr - Przeprowadza dekompozycję QR
Q, R = qr(A)
print("\nQ z dekompozycji QR:\n", Q)
print("R z dekompozycji QR:\n", R)

# 3. eig - Oblicza wartości własne i wektory własne
w, v = eig(A)
print("\nWartości własne A:\n", w)
print("Wektory własne A:\n", v)

# 4. svd - Przeprowadza dekompozycję SVD
U, s, V = svd(A)
print("\nU z dekompozycji SVD:\n", U)
print("Wartości osobliwe s:\n", s)
print("V z dekompozycji SVD:\n", V)

# 5. det - Oblicza wyznacznik
determinant = det(A)
print("\nWyznacznik A:\n", determinant)

# 6. solve - Rozwiązuje układ równań liniowych
B = np.array([[3, 1], [1, 2]])
b = np.array([9, 8])
x = solve(B, b)
print("\nRozwiązanie układu równań Bx = b:\n", x)

# 7. lstsq - Rozwiązuje układ równań metodą najmniejszych kwadratów
C = np.array([[1, 1], [1, 2], [1, 3]])
d = np.array([1, 2, 2])
x_lstsq, residuals, rank, s_lstsq = lstsq(C, d, rcond=None)
print("\nRozwiązanie układu równań metodą najmniejszych kwadratów:\n", x_lstsq)

# 8. norm - Oblicza normę
v = np.array([3, 4])
v_norm = norm(v)
print("\nNorma wektora v:\n", v_norm)

# 9. cholesky - Przeprowadza dekompozycję Cholesky'ego
D = np.array([[4, 2], [2, 3]])
L = cholesky(D)
print("\nMacierz dolnotrójkątna L z dekompozycji Cholesky'ego macierzy D:\n", L)

# 10. pinv - Oblicza macierz pseudoodwrotną
A_pinv = pinv(A)
print("\nMacierz pseudoodwrotna A:\n", A_pinv)