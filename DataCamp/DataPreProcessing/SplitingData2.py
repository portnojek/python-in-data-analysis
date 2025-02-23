import pandas as pd
from sklearn.model_selection import train_test_split

from DataCamp.DataPreProcessing.SplitingData import volunteer

volunteer = pd.read_csv('cost_revenue_clean.csv', sep=';')

# Create a DataFrame with all columns except category_desc
X = volunteer.drop('category_desc', axis=1)

# Create a category_desc labels dataset
y = volunteer[['category_desc']]

# Use stratified sampling to split up the dataset according to the y dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=42)

# Print the category_desc counts from y_train
print(y_train['category_desc'].value_counts())