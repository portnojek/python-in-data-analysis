# to taki mocno zakrzywiony przyklad

import pandas as pd

# Print the head of the hits column
volunteer = pd.read_csv('cost_revenue_clean.csv', sep=';', decimal=',')

print(volunteer["hits"].head())

# Convert the hits column to type int
volunteer["hits"] = volunteer["hits"].astype("int")

# Look at the dtypes of the dataset
print(volunteer.dtypes)