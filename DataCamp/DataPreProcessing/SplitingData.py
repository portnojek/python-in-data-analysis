import pandas as pd
import matplotlib.pyplot as plt
# Assuming the dataset is already loaded into a DataFrame called 'df'
# If not, load it first:
# df = pd.read_csv('volunteer_dataset.csv')
volunteer = pd.read_csv('cost_revenue_clean.csv', sep=';', decimal=',')
# Count the occurrences of each category description
category_counts = volunteer['production_budget_usd'].value_counts()

# Filter for categories with less than 50 occurrences
rare_categories = category_counts[category_counts < 50]

# Display the rare categories and their counts
print("Categories with less than 50 occurrences:")
print(rare_categories)

# Optional: Display the total number of rare categories
print(f"\nTotal number of rare categories: {len(rare_categories)}")

# Plot the distribution of all categories
plt.figure(figsize=(12, 6))
category_counts.plot(kind='bar')
plt.title('Distribution of Category Descriptions')
plt.xlabel('Category')
plt.ylabel('Count')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()