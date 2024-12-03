import pandas as pd
import numpy as np

# Load CSV File
df = pd.read_csv("titanic.csv")


# Find missing values in each column
print(df.isna().sum())


# Drop columns from Data
print(df.drop("PassengerId", axis=1)) # To drop column PassengerId
print(df.drop(2, axis=0)) # To drop row 2

# Replace all 'male' to 1 and 'female' to 0:
df["Sex"] = df["Sex"].map({'male': 1, "female": 0})
df.replace({"Sex": 'male'}, 1, inplace=True) # Alternate Solution
df.replace({"Sex": 'female'}, 0, inplace=True)


# Fill missing values in age column
df["Age"].fillna("No Age", inplace=True)  