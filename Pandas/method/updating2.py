import pandas as pd

data = {
  "name": ['ram', 'shayam', 'rohit', 'aditi', 'rohit', 'rahul', 'kumar', 'kunal'],
  'age' :[19, 20, 20, 19, 29, 23, 49, 31],
  'salary':[50000, 60000, 70000, 45000, 87000, 70000, 45000, 49000],
  'performance':[85, 98, 89, 90, 78, 78, 90, 78]
  
}

df = pd.DataFrame(data)
print(df)


#incressing salary by 5%
df['salary'] = df['salary'] * 1.05
print(df)


