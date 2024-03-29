# -*- coding: utf-8 -*-
"""Analysing BigMar Sales.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15rhYBqW_8zdl1QP3YIE0NShvc4tzjwVv
"""

from google.colab import drive
from google.colab import files
#drive.mount('/content/drive')
import pandas as pd
import numpy as np
data=pd.read_csv("/content/sales_pred.csv")
data

data.head(5)

data.describe()

data['Outlet_Establishment_Year']=2009-data['Outlet_Establishment_Year']

data.head(5)

data['Item_Fat_Content'].unique()

data.Item_Fat_Content=data['Item_Fat_Content'].replace(('Low Fat','low fat'),'LF')

data.Item_Fat_Content=data['Item_Fat_Content'].replace(('reg','Regular'),'RF')

data['Item_Fat_Content'].unique()

from sklearn import preprocessing
label_encoder=preprocessing.LabelEncoder()
data['Item_Fat_Content']=label_encoder.fit_transform(data['Item_Fat_Content'])

data.head(5)

data.info()

data.isna().sum()

g=data.groupby('Item_Type')

g.get_group('Household')['Item_Visibility'].mean()

g.get_group('Household').mean()

g.mean().Item_Visibility

data[(data.Item_Type=='Houshold')].Item_Visibility.replace(0.000000,0.0613)

data[data.Item_Visibility==0.0613].Item_Type.unique()

data[data.Item_Type=='Household'].Item_Visibility.head(20)

data['Item_Visibility'] =data['Item_Visibility'].replace(0.0000000, np.nan)

data['Item_Visibility'] =data['Item_Visibility'].fillna(data.groupby('Item_Type')['Item_Visibility'].transform('mean'))

data.head(5)



data['Item_Identifier'].value_counts()

data.drop(['Item_Identifier'],axis=1)

data['Item_Weight'].isna().sum()

g.mean().Item_Weight

data['Item_Weight'] =data['Item_Weight'].fillna(data.groupby('Item_Type')['Item_Weight'].transform('mean'))

data.head(10)

#data.drop('Item_Identifier',axis=1,inplace=True)

data.head(4)

g=data.groupby('Outlet_Size')

data['Outlet_Identifier'].value_counts()
data[data.Outlet_Identifier=='OUT049'].Outlet_Size.replace(np.NaN,'Medium',inplace=True)

data.head(5)

data.tail(20)

data.head(40)

data.Outlet_Location_Type.value_counts()

from sklearn import preprocessing
label_encoder=preprocessing.LabelEncoder()
data['Outlet_Location_Type']=label_encoder.fit_transform(data['Outlet_Location_Type'])

data.head(5)

data.Outlet_Type.value_counts()

out_ident = pd.get_dummies(data['Outlet_Type'], drop_first=True, dtype=int) 
concated_sum = pd.concat([data, out_ident],sort=True, axis=1)

data=concated_sum

data.drop(['Outlet_Type'],axis=1,inplace=True)

data.head(2)

g=data.groupby('Outlet_Size')

g.max()

data.loc[0,'Outlet_Identifier']=49

for i in range(1,data.Outlet_Size.count()):
  data.loc[i,'Outlet_Identifier']=int(data.Outlet_Identifier[i][4:])

data.head(4)

data.Item_Type.unique()

data['Item_Type']=data.Item_Type.replace(('Hard Drinks','Soft Drinks'),'Drinks')
data['Item_Type']=data.Item_Type.replace(('Seafood','Snack Foods','Frozen Foods','Starchy Foods'),'Foods')
data['Item_Type']=data.Item_Type.replace(('Breads'),'Baking Goods')
data['Item_Type']=data.Item_Type.replace(('Fruits and Vegetables'),'Health and Hygiene')

data.Item_Type.value_counts()

data.head(1)

g=data.groupby('Item_Type')
g.describe()

data['Outlet_Size'] =data['Outlet_Size'].replace(np.nan, 'Medium')

out_ident = pd.get_dummies(data['Item_Type'], drop_first=True, dtype=int) 
concated_sum = pd.concat([data, out_ident],sort=True, axis=1)

concated_sum

data.drop('Item_Identifier',axis=1,inplace=True)

data.Outlet_Size.unique()

from sklearn import preprocessing
label_encoder=preprocessing.LabelEncoder()
data['Outlet_Size']=label_encoder.fit_transform(data['Outlet_Size'])

########################################################## FINAL DATASETS

data.head(10)

