import pandas as pd
import numpy as np

#/Users/ravikuchika/Downloads/job_salary_prediction_dataset.csv
file_path = '/Users/ravikuchika/Downloads/job_salary_prediction_dataset.csv'
df = pd.read_csv(file_path)
df1=df.head(10)
print(df1)
print(df1.iloc[2:4])

print(df1.loc[2:4,['job_title','experience_years']])

df1.drop('skills_count',axis=1,inplace=True)
print(df1.shape)
print(df1.info)