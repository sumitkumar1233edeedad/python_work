import pandas as pd
import numpy as np


# Ensure the file path is correct and exists; if not, update the path accordingly.
df = pd.read_csv(r'C:\Users\sumit\OneDrive\Desktop\python_work\python_work\numpy\indian employee dataset\indian_employee_data.csv')
print(df.head())

# Ensure 'Salary (INR)' is numeric, coerce errors to NaN
df['Salary (INR)'] = pd.to_numeric(df['Salary (INR)'], errors='coerce')

#checking the missing value
print('missing value in each value')
print(df.isnull().sum())

df['Salary (INR)'] = df['Salary (INR)'].fillna(df['Salary (INR)'].mean())

df['Performance Rating'] = df['Performance Rating'].fillna(df['Performance Rating'].median())

df.replace([np.inf, -np.inf], np.nan, inplace=True)

numeric_cols = df.select_dtypes(include=[np.number]).columns
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())

#remove duplicate
df.drop_duplicates(inplace=True)

#replace negative  salary
df['Salary (INR)'] = np.where(df['Salary (INR)'] < 0, df['Salary (INR)'].mean(), df['Salary (INR)'])

salary_mean = df['Salary (INR)'].mean()
salary_std = df['Salary (INR)'].std()
lower =salary_mean - (3*salary_std)
upper = salary_mean + (salary_std)

#remove rwo hight and lowe
df = df[(df['Salary (INR)'] >= lower ) & (df['Salary (INR)'] <= upper)]

df.to_csv('cleaned_data.csv', index=False)
print('complete')