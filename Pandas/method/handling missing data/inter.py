import pandas as pd

data = {
  "name": ['ram', 'kumarr' ,'shayam', 'rohit', 'aditi', 'rohit', 'rahul', 'kumar', 'kunal'],
  'age' :[19, None, 20,  20, 19, 29, 23, 49, 31],
  'salary':[50000, None,  60000, 70000, 45000, 87000, 70000, 45000, 49000],
  'performance':[85, None,  98, 89, 90, 78, 78, 90, 78]
  
}

# Create a DataFrame from the dictionary
df = pd.DataFrame(data)
print(df)
#linear, polynomial, time

df.interpolate(method='linear', axis=0, inplace=True)