# Import packages
import matplotlib.pyplot as plt
import seaborn as sns

# Set seaborn style
sns.set(color_codes=True)

# Create a list of labels:cd
cd = ['clinton', 'trump', 'sanders', 'cruz']

# Define numerical values
values = [50, 60, 40, 30]

# Define custom colors
colors = ['red', 'blue', 'green', 'orange']

# Plot the bar chart
ax = sns.barplot(x=cd, y=values, palette=colors)
ax.set(ylabel="count")
plt.show()