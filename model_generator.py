import pandas as pd
import os
import csv
import numpy as np
import sklearn
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('C:\\Users\\chaitanya\\PycharmProjects\\MajorProject_dev\\venv\\coords.csv')
df=df.fillna(0)
df.classtype=df.classtype.map({'up':0,'down':1})
df=df.fillna(0)
x=df.drop(columns=['classtype'])
y=df['classtype']
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=2022)
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

from sklearn.tree import DecisionTreeClassifier

DT=DecisionTreeClassifier()
DT.fit(x_train,y_train)

import joblib
import pickle

# Save the model as a pickle in a file
joblib.dump(DT, 'DT.pkl')

# Load the model from the file
knn_from_joblib = joblib.load('DT.pkl')

# Use the loaded model to make predictions
print(knn_from_joblib.predict(x_test))