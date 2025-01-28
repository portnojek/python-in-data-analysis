import pandas
from pandas import DataFrame
import matplotlib.pyplot as plt

data = pandas.read_csv('cost_revenue_clean.csv', sep=';', decimal=',')
X = DataFrame(data, columns=['production_budget_usd'])
Y = DataFrame(data, columns=['worldwide_gross_usd'])
print(data.describe())
print(data.dtypes)

plt.figure(figsize=(10,6))
plt.scatter(X, Y, alpha=0.3)
plt.title('Film Cost vs Global Revenue', fontsize=14)
plt.xlabel('Production budget')
plt.ylabel('Worldwide Gross $')
plt.ylim(0, 3000000000)
plt.xlim(0, 450000000)
plt.grid()
plt.show()