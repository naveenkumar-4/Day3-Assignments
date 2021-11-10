# -*- coding: utf-8 -*-
"""day-3-data-preprocessing-template.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/gist/naveenkumar-4/afa49f274d22316a051bfaac6db4b7e3/day-3-data-preprocessing-template.ipynb
"""

# step 1: Import Data from csv
import pandas as pd
data = pd.read_csv('Data.csv') #reading data in table format/matrix



data

data.columns

data['Country']

data['Country'][0]

data['Age'][6]

data[:3]

data.head(3)

data[::-1]

data.tail(3)

# step 2: Separate both input and output variables

# Independent Variables - Country, Age, Salary

X = data.iloc[:,0:-1].values

X

# Dependent Variables - Purchased
Y = data.iloc[:,-1].values

Y

print(Y)

# step 3 : Talk About Missing Data
!pip install sklearn

# Missing data in x
# Missing data - mean
from sklearn.impute import SimpleImputer
import numpy as np
imputer = SimpleImputer(missing_values = np.nan,strategy = 'mean')
imputer.fit(X[:,1:3]) # identification
X[:,1:3] = imputer.transform(X[:,1:3])

X

# step 4 : Taking care of string data

# Independent Variable at index 0

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

ct = ColumnTransformer(transformers=[('encoder',OneHotEncoder(),[0])],remainder='passthrough')
X = ct.fit_transform(X)

X

#Encode the Dependent Variable

from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
Y = le.fit_transform (Y)

Y

#step 5 : Feature Scaling

from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
X[:,3:5] = sc.fit_transform(X[:,3:5])

X

#step 6 : Spliting the data into Train and Test
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size = 0.2)

X_train

X_test

Y_train

Y_test