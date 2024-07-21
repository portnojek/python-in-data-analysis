#bladzenie losowe w czystym pythonie

#!blockstart
import random

import matplotlib.pyplot as plt
import numpy as np

position = 0
walk = [position]
nsteps = 1000

for _ in range(nsteps):
    step = 1 if random.randint(0,1) else -1
    position += step
    walk.append(position)

#! Blockend
plt.plot(walk[:100])
plt.show()
plt.close()

#bladzenie losowe w numpy
nsteps2 = 1000
rng = np.random.default_rng(seed=1234) #Nowy generator
draws = rng.integers(0, 2, size=nsteps2)
steps = np.where(draws == 0, 1, -1)
walk = steps.cumsum()

print(walk.min())
print(walk.max())

#moment pierwszego przecięcia
cutpoints = (np.abs(walk) >=10).argmax()
print(cutpoints)

#jednoczesne symulowanie wielu błądzeń losowych
nwalks = 5000
nsteps = 1000
draws = rng.integers(0, 2, size=(nwalks, nsteps)) # 0 lub 1
steps = np.where(draws > 0, 1, -1)
walks = steps.cumsum(1)
print(walks)
print(walks.max())
print(walks.min())

#minimalny czas przecięcia wartości 30 lub -30
hits30 = (np.abs(walks) >= 30).any(axis=1)
print(hits30)
print(hits30.sum())

crossing_times = (np.abs(walks[hits30]) >= 30).argmax(axis=1)
print(crossing_times)
print(crossing_times.mean())