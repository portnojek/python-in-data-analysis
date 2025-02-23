# to taki mocno zakrzywiony przyklad

import pandas as pd

# Print the head of the hits column
volunteer = pd.read_csv('cost_revenue_clean.csv', sep=';', decimal=',')

print(volunteer["production_budget_usd"].head())

# Convert the hits column to type int
volunteer["production_budget_usd"] = volunteer["production_budget_usd"].astype("int")
volunteer["worldwide_gross_usd"] = volunteer["worldwide_gross_usd"].astype("int")

# Look at the dtypes of the dataset
print(volunteer.dtypes)
print(volunteer)