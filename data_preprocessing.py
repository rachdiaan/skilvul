import pandas as pd
import numpy as np

# Load datasets
customer_interactions = pd.read_csv('customer_interactions.csv')
purchase_history = pd.read_csv('purchase_history.csv')
product_details = pd.read_csv('product_details.csv')

# Display the first few rows of each dataframe
print(customer_interactions.head())
print(purchase_history.head())
print(product_details.head())

# Basic info and stats
print(customer_interactions.info())
print(purchase_history.info())
print(product_details.info())
print(customer_interactions.describe())
print(purchase_history.describe())
print(product_details.describe())

# Handle missing values
customer_interactions.fillna(0, inplace=True)
purchase_history.dropna(inplace=True)
product_details.dropna(inplace=True)

# Merge datasets for a comprehensive view
purchase_history = purchase_history.merge(product_details, on='Product_ID', how='left')
merged_data = customer_interactions.merge(purchase_history, on='Customer ID', how='left')

# Encoding categorical variables if necessary
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
product_details['Category'] = le.fit_transform(product_details['Category'])

print(product_details.head())

