import pandas as pd


data = {
    "length_of_time": ["5 minutes", "about 30 minutes", "10 mins", "1 minute", "45 minutes"],
    "seconds": [300, 1800, 600, 60, 2700],
    "country": ["us", "ca", "us", "gb", "us"],
    "type": ["light", "triangle", "disk", "light", "circle"]
}

ufo = pd.DataFrame(data)
# Use pandas to encode 'us' values as 1 and others as 0
ufo["country_enc"] = ufo["country"].apply(lambda x: 1 if x == "us" else 0)

# Print the number of unique type values
print(len(ufo["type"].unique()))

# Create a one-hot encoded set of the type values
type_set = pd.get_dummies(ufo["type"])

# Concatenate this set back to the ufo DataFrame
ufo = pd.concat([ufo, type_set], axis=1)