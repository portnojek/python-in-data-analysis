# Count the missing values in the length_of_time, state, and type columns, in that order
print(ufo[["length_of_time", "state", "type"]].isna().sum())

# Drop rows where length_of_time, state, or type are missing
ufo_no_missing = ufo.dropna(subset=["length_of_time", "state", "type"])

# Print out the shape of the new dataset
print(ufo_no_missing.shape)