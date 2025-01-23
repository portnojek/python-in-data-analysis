import pandas
from pandas import DataFrame
import matplotlib.pyplot as plt

data = pandas.read_csv('cost_revenue_clean.csv', sep=';', decimal=',')
X = DataFrame(data, columns=['production_budget_usd'])
Y = DataFrame(data, columns=['worldwide_gross_usd'])

plt.scatter(X, Y)
plt.show()