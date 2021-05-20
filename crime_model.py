import pandas as pd
import numpy as np
import io
import pickle
from datetime import datetime,date,time
from geopy.geocoders import Nominatim
import sys
import csv
from pandas import *
dataset1=pd.read_csv("data2.csv")
data=pd.read_csv('data2.csv')
dataset1.dropna(inplace=True)
data['timestamp'] = pd.to_datetime(data['timestamp'])
#format = '%d/%m/%Y %H:%M:%S'
column_1 = data.iloc[:,0]

db=pd.DataFrame({"year": column_1.dt.year,
              "month": column_1.dt.month,
              "day": column_1.dt.day,
              "hour": column_1.dt.hour,
              "dayofyear": column_1.dt.dayofyear,
              "week": column_1.dt.week,
              "weekofyear": column_1.dt.weekofyear,
              "dayofweek": column_1.dt.dayofweek,
              "weekday": column_1.dt.weekday,
              "quarter": column_1.dt.quarter,
             })
del dataset1['timestamp']
data1=pd.concat([db,dataset1],axis=1)
data1.dropna(inplace=True)

data1['Murder'] = data1['Murder'].astype(int)
data1['Rape'] = data1['Rape'].astype(int)
data1['Kidnapping'] = data1['Kidnapping'].astype(int)
data1['Speeding'] = data1['Speeding'].astype(int)
data1['Domestic Violence'] = data1['Domestic Violence'].astype(int)
data1['Robbery'] = data1['Robbery'].astype(int)
#data1.dropna(inplace=True)

X=data1.iloc[:,[1,2,3,4,16,17]].values
y=data1.iloc[:,[10,11,12,13,14,15]].values

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=50)

from sklearn.ensemble import RandomForestClassifier
rfc = RandomForestClassifier(n_estimators=100)
rfc.fit(X_train, y_train)
pickle.dump(rfc, open('model.pkl','wb'))