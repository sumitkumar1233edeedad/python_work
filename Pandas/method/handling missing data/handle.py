import pandas as pd

data = {
  "name": ['ram', None ,'shayam', 'rohit', 'aditi', 'rohit', 'rahul', 'kumar', 'kunal'],
  'age' :[19, None, 20,  20, 19, 29, 23, 49, 31],
  'salary':[50000, None,  60000, 70000, 45000, 87000, 70000, 45000, 49000],
  'performance':[85, None,  98, 89, 90, 78, 78, 90, 78]
  
}

df = pd.DataFrame(data)
print(df)
#dropna()

#index = 0, and index = 1
df.dropna(inplace=True)
print(df)
