import pandas as pd

data = {
  "name": ['ram', None ,'shayam', 'rohit', 'aditi', 'rohit', 'rahul', 'kumar', 'kunal'],
  'age' :[19, None, 20,  20, 19, 29, 23, 49, 31],
  'salary':[50000, None,  60000, 70000, 45000, 87000, 70000, 45000, 49000],
  'performance':[85, None,  98, 89, 90, 78, 78, 90, 78]
  
}

# Create a DataFrame from the dictionary
df = pd.DataFrame(data)
print(df)

# Uncomment the following lines to fill all missing values with 0
# df.fillna(0, inplace=True)
# print(df)

# Fill missing values in 'age' column with the mean of the 'age' column
df['age'].fillna(df['age'].mean(), inplace=True)

# Fill missing values in 'salary' column with the mean of the 'salary' column
df['salary'].fillna(df['salary'].mean(), inplace=True)

# Print the DataFrame after filling missing values
print(df)