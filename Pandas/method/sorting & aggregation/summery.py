"""df['column name'].mean()
df['column name'].mim()
df['column name'].max()
df['column name'].sum()"""

import pandas as pd

data = {
    'name':['ram', 'arun', 'rahul'],
    'salary':[20000, 30000, 10000],
    'age':[20, 19, 20]
}

df = pd.DataFrame(data)

average = df['salary'].mean()
print(average)