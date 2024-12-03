import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

data = pd.read_csv("mycsv.csv", delimiter=';')
x = data.drop(columns="quality")
y = data.quality
xTrain, xTest, yTrain, yTest = train_test_split(x, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(xTrain, yTrain)
intercept = model.intercept_
slope = model.coef_

yPred = model.predict(xTest)
mse = mean_squared_error(yTest, yPred)
rmse = mse**0.5