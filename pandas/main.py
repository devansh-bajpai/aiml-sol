import pandas as pd
import numpy as np

myDict = {
    "name" : ["aman", "shradha", "harry", "mukesh"],
    "branch" : ["cse", "ece", "ee", "ee"],
    "age" : [22, 24, 30, 56]
}

df = pd.DataFrame(myDict)
df.to_csv("mydf.csv")