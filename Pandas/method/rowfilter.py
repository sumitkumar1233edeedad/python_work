
import pandas as pd

data = {
  "name": ['ram', 'shayam', 'rohit', 'aditi', 'rohit', 'rahul', 'kumar', 'kunal'],
  'age' :[19, 20, 20, 19, 29, 23, 49, 31],
  'salary':[50000, 60000, 70000, 45000, 87000, 70000, 45000, 49000],
  'performance':[85, 98, 89, 90, 78, 78, 90, 78]
  
}


#filter use method
df = pd.DataFrame(data)
#single rwo condition
high_salary = df[df['salary']>50000]
print('above for 50000', high_salary)

#double rwo check condition
filter = df[(df['age'] >20) & (df['salary'] > 50000)]
print(filter)


#using or condition one is true than return
filter_or = df[(df['age'] > 22) | (df['performance'] > 80)]
print('this one condition is show this person age 20 sa above and performance 75 sa above than show the answer', filter_or)

