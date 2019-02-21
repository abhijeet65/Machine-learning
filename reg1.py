# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 22:34:16 2019

@author: Abhijeet Saraf
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset=pd.read_csv('Salary_Data.csv')
X=dataset.iloc[:].values
y=dataset.iloc[:, 1].values

print(X)