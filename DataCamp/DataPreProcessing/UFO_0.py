# Look at the first 5 rows of the date column
# Pełny zbiór danych
import pandas as pd
# Przykładowe dane JSON jako string
json_data = '''
[
  {"date": "2023-01-15T00:00:00.000"},
  {"date": "2023-02-20T00:00:00.000"},
  {"date": "2023-03-10T00:00:00.000"},
  {"date": "2023-04-05T00:00:00.000"},
  {"date": "2023-05-25T00:00:00.000"}
]
'''

# Załaduj dane JSON do DataFrame
ufo = pd.read_json(json_data)

print(ufo["date"].head())

# Extract the month from the date column
ufo["month"] = ufo["date"].dt.month

# Extract the year from the date column
ufo["year"] = ufo["date"].dt.year

# Take a look at the head of all three columns
print(ufo[["date", "month", "year"]].head())