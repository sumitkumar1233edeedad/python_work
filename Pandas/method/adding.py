import pandas as pd

data = {
  "name": ['ram', 'shayam', 'rohit', 'aditi', 'rohit', 'rahul', 'kumar', 'kunal'],
  'age' :[19, 20, 20, 19, 29, 23, 49, 31],
  'salary':[50000, 60000, 70000, 45000, 87000, 70000, 45000, 49000],
  'performance':[85, 98, 89, 90, 78, 78, 90, 78]
  
}

df = pd.DataFrame(data)

#adding columns df['column'] = some_data

print(df)

df['bonus'] = df['salary'] * 0.1

print(df)

#using insert method df.insert(loc,  'column', some_data) loc is location

df.insert(0, "employee id", [10, 20 , 30, 40, 50, 60, 70, 80])

print(df)