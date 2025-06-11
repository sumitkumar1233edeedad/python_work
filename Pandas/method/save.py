import pandas as pd

data = {
     "Name" : ['Ram', 'Raman', 'Rahul'],
     "Age" : [10, 30, 40],
     'City': ['Nagpur', 'Mumbai', 'Delhi']
     
}

#data convert to the data frame

df = pd.DataFrame(data)
print(df)

#different name file save the document
#index mean front in 0 to n count carry on this 
#first is True is on index 0 to n add
#second is False is on index off.
# df.to_csv('student_data.csv', index=False)
# df.to_excel('student_data.xlsx', index=False)
df.to_json('student_data.json', index=False)