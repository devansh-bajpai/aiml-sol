import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

data = pd.read_csv("Sonar.csv")
X = data.drop(columns=["Class"])
Y = data.Class
model = KMeans(n_clusters=2, random_state=42)
model.fit(X)
predicted_clusters = model.labels_

unnamedStates = sum(predicted_clusters != Y)

plt.scatter(X.iloc[:, 0], X.iloc[:, 1])
plt.show()