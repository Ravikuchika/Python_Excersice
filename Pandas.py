import pandas as pd
import numpy as np

s = pd.Series([1,2,3,4,5, 'abc'])
print(s)
print(s.values)
print(s.index)
s.name = 'numbers'
print(s.name)
print(s)

#indexing
print(s[0])
print(s[2:4])

print(s.iloc[[2,3]])

s = pd.Series([1,2,3,4,5,6])
s.name='numbers'
print(s)
index=['a','b','c','d','e','f']
s.index = index
print(s)

print(pd.__version__)


print(s[s>3]) #conditional stmts
print(s[(s>3) & (s<6)])
print(s[~(s>1)])
s['a'] =100
print(s)


series = pd.Series([1,np.nan,3,4,np.nan])
print(series)
print(series.notnull().sum())
print(series.isnull().sum())

#Dataframes
data={''}
#/Users/ravikuchika/Downloads/job_salary_prediction_dataset.csv
file_path = '/Users/ravikuchika/Downloads/job_salary_prediction_dataset.csv'
df = pd.read_csv(file_path)
print(df.head())
print(df.tail())