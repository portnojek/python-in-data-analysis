import re
import numpy as np
import pandas as pd


data = {
    "length_of_time": ["5 minutes", "about 30 minutes", "10 mins", "1 minute", "45 minutes"],
    "seconds": [300, 1800, 600, 60, 2700],
    "country": ["us", "ca", "us", "gb", "us"],
    "type": ["light", "triangle", "disk", "light", "circle"]
}

ufo = pd.DataFrame(data)

def return_minutes(time_string):
    # Search for numbers in time_string
    num = re.search(r'\d+', time_string)
    if num is not None:
        return int(num.group(0))


# Apply the extraction to the length_of_time column
ufo["minutes"] = ufo["length_of_time"].apply(return_minutes)

# Take a look at the head of both of the columns
print(ufo[["length_of_time", "minutes"]].head())

# Check the variance of the seconds and minutes columns
print(ufo[["seconds", "minutes"]].var())

# Log normalize the seconds column
ufo["seconds_log"] = np.log(ufo["seconds"])

# Print out the variance of just the seconds_log column
print(ufo["seconds_log"].var())