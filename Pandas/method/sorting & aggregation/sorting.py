#sorting data
#sorting data $ 1 column sort_value()

# df.sort_value(by='column name ', True/False , inplace = True)

import pandas as pd

data = {
    'name':['ram', 'arun', 'rahul'],
    'salary':[20000, 30000, 10000],
    'age':[20, 19, 20]
}

df = pd.DataFrame(data)
df.sort_values(by='age', ascending=True, inplace=True)
print(df)