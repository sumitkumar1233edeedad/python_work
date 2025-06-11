#ste -1 sample data frame

import pandas as pd

data = {
  "name": ['ram', 'shayam', 'rohit', 'aditi', 'rohit', 'rahul', 'kumar', 'kunal'],
  'age' :[19, 20, 20, 19, 29, 23, 49, 31],
  'salary':[50000, 60000, 70000, 45000, 87000, 70000, 45000, 49000],
  'performance':[85, 98, 89, 90, 78, 78, 90, 78]
  
}

df = pd.DataFrame(data)
print('sample Dataframe')
print(df)
print('descreptive statistics',df.describe())

'''
count = number for element without null and null show
mean = average
std = two type small const.  and large const.
min = smallest value
25% :
50% :
75% :
max :
 smallest to highest value return 25% and max% show the data

'''