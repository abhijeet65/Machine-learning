# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 22:34:16 2019

@author: Abhijeet Saraf
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset=pd.read_csv('Salary_Data.csv')
X=dataset.iloc[:,:-1].values
y=dataset.iloc[:, 1].values

from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1/3, random_state=0)
 
#fitting linear regression model in traning set

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train,y_train)

#predicting test set results

y_pred = regressor.predict(X_test)



