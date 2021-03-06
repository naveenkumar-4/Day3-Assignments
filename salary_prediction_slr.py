# -*- coding: utf-8 -*-
"""Salary_prediction_SLR.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/gist/naveenkumar-4/a0329657adf7036a4077a1f69cbf91de/salary_prediction_slr.ipynb
"""

import pandas as pd

data = pd.read_csv('Salary_Data_SLR.csv')

data

# INdepndent Variable (X)

X = data.iloc[:,0].values
X=X.reshape(-1,1)

X

Y=data.iloc[:,1].values

Y

from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2)

X_train

X_test

Y_train

Y_test

# Y=f(X)=aX+b

from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(X_train,Y_train)


LinearRegression(copy_X=True, fit_intercept=True, n_jobs=None,normalize=False)

regressor.coef_

regressor.intercept_

regressor.predict([[6]])

regressor.predict(X_test)

Y_test