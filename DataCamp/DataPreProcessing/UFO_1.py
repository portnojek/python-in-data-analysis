import pandas as pd

data = {
    "length_of_time": ["5 minutes", "about 30 minutes", "10 mins", "1 minute", "45 minutes"],
    "seconds": [300, 1800, 600, 60, 2700],
    "country": ["us", "ca", "us", "gb", "us"],
    "type": ["light", "triangle", "disk", "light", "circle"]
}

ufo = pd.DataFrame(data)

# Print the DataFrame info
print(ufo.info())

# Change the type of seconds to float
ufo["seconds"] = ufo["seconds"].astype(float)

# Change the date column to type datetime
ufo["date"] = pd.to_datetime(ufo["date"])

# Check the column types
print(ufo.info())