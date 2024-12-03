import pandas as pd
import numpy as np

df = pd.read_csv("titanic.csv")
# print(df.isnull().sum())
# print(df.drop(2, axis=0))
# print(df.replace('male', 0).loc[:,"Sex"])
# print(df["Cabin"].fillna("Fucj", inplace=True))
# df.replace({"Cabin": np.nan},"hi", inplace=True)
df["Sex"] = df["Sex"].map({'male':1, 'female': 0})
print(df)
# df["Cabin"] = df["Cabin"].map({np.nan:50})
# print(df[10:25])
df["Cabin"].fillna("No cabin", inplace=True)
print(df)





# Replace all male to 1 and female to 0
# df = df.replace('male', 0)
# df = df.replace('female', 1)
# print(df.loc[:,"Sex"])


# Fill missing values in age column:

# bool_series = pd.isnull(df["Age"])
# print(bool_series)
# # print(df[bool_series])
# print(df.notnull())