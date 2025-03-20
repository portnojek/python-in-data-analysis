from sympy import *
from sympy.plotting import plot3d

x = symbols('x')
f = 2*x + 1
plot(f)

x, y = symbols(('x y'))
f = 2*x + 3*y
plot3d(f)

#sumowanie w pythonie
suma = sum(2*i for i in range(1,6))
print(suma)

#sumowanie elementów w pythonie
x = [1, 4, 6, 2]
n  = len(x)

suma = sum(10*x[i] for i in range(0, n))
print(suma)

#sumowanie w sympy
i, n = symbols('i n')

suma = Sum(2*i, (i, 1, n))
suma_do_5 = suma.subs(n, 5)
print(suma_do_5.doit())

#potegowanie
x = symbols('x')
wyrazenie = x**2/x**5
print(wyrazenie)