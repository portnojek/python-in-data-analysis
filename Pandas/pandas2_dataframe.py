import numpy as np
import pandas as pd

data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
        'year': ['2000', '2001', '2002', '2003', '2004', '2005'],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
frame = pd.DataFrame(data)
print(frame)

print(frame.head()) # wybiera tylko 5 pierwszych wierszy
print(frame.tail()) # wybiera ostatnie wiersze

frame2 = (pd.DataFrame(data, columns=['year', 'state', 'pop', 'debt'])) # wybór kolejności kolumn
print(frame2)
print(frame2['state'])
print(frame2.year) #jeśli nazwa bedzie miala spacje lub znak podkreślenia to to nie zadziała

#iloc i loc
print(frame2.loc[1])
print(frame2.iloc[2])

#przypisanie wartości do całej kolumny
frame2['debt'] = 16.5
print(frame2)
frame2['debt'] = np.arange(6.)
print(frame2)

#dodanie nowej kolumenty
frame2['eastern'] = frame2.state == 'Ohio'
print(frame2)

#kasowanie kolumny
del frame2['eastern']
print(frame2)

#zagnieżdzony słownik słowników
populations2 = {"Ohio": {2000: 1.5, 2001: 1.7, 2002: 3.6},
                "Nevada": {2001: 2.4, 2002: 2.9}}

frame3 = pd.DataFrame(populations2)
print(frame3)

#transponowanie DataFrame
print(frame3.T)