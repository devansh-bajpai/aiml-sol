import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_score, recall_score, f1_score, confusion_matrix
data = pd.read_csv("Sonar.csv")
x = data.iloc[:, :-1]
y = data.Class
xTrain, xTest, yTrain, yTest = train_test_split(x, y, test_size=0.2, random_state=42)
model = GaussianNB()
model.fit(xTrain, yTrain)
yPredicted = model.predict(xTest)
pr = precision_score()