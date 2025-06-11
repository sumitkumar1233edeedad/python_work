""" 
use info() method
show the info of data like that:
                               how the row and columns
                               columns name
                               int64 float64 object
                               non null counts
                               memory use data frame

"""
import pandas as pd

# pf = pd.read_json('sample_Data.json')

# print('data')
# print(pf.info())

#me file data access

data = {
     "Name" : ['Ram', 'Raman', 'Rahul'],
     "Age" : [10, 30, 40],
     'City': ['Nagpur', 'Mumbai', 'Delhi']
     
}

#data convert to the data frame

df = pd.DataFrame(data)

print('data')
print(df.info())