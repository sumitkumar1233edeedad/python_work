#df.sort_value(by=['age', 'salary'], ascending=[True, False], inplace=True)
#multi column sort in  one time
#ascending in your value according set the value ascending and descending in list formate
import pandas as pd

data = {
    'name':['ram', 'arun', 'rahul'],
    'salary':[20000, 30000, 10000],
    'age':[20, 19, 20]
}

df = pd.DataFrame(data)
print('multi column sorting')
df.sort_values(by=['age', 'salary'], ascending=[True, False], inplace=True)
print(df)