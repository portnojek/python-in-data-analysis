# Import libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Load a sample dataset from Seaborn
df = sns.load_dataset("penguins")

# Create a scatter plot with Seaborn
plt.figure(figsize=(8,6))
sns.scatterplot(x='bill_length_mm', y='bill_depth_mm', hue='species', data=df, palette='Set1')

# Add title and labels
plt.title('Bill Length vs. Bill Depth (Penguins)', fontsize=16)
plt.xlabel('Bill Length (mm)', fontsize=12)
plt.ylabel('Bill Depth (mm)', fontsize=12)

# Show plot
plt.show()