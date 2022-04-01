import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#Cleaning
data= pd.read_csv("house-data.csv")
data= data.drop (["date"], axis=1)
print(data)
print(data.nunique())
data= data.drop(['street','city','country','statezip'], axis=1)   #drop the object data due to we dont use it.
print(data.isnull().sum()) # I dont have any null values.

#Preprocessing
c= data.corr()
#sns.heatmap(c, annot=True)
plt.scatter(data["sqft_living"],data["bedrooms"])
plt.show()

#Ending
