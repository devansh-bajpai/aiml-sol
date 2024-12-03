import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

data = pd.read_csv("wineqialitu.csv", delimiter=';')

X = data.drop(columns=["quality"])
Y = data.quality
