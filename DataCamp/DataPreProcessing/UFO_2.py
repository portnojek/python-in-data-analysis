import pandas as pd

data = {
    "length_of_time": ["5 minutes", "about 30 minutes", "10 mins", "1 minute", "45 minutes"],
    "seconds": [300, 1800, 600, 60, 2700],
    "country": ["us", "ca", "us", "gb", "us"],
    "state": ["ca", "qc", None, "tx", "ny"],
    "type": ["light", "triangle", "disk", "light", "circle"]
}

ufo = pd.DataFrame(data)


# Count the missing values in the length_of_time, state, and type columns, in that order
print(ufo[["length_of_time", "state", "type"]].isna().sum())

# Drop rows where length_of_time, state, or type are missing
ufo_no_missing = ufo.dropna(subset=["length_of_time", "state", "type"])

# Print out the shape of the new dataset
print(ufo_no_missing.shape)