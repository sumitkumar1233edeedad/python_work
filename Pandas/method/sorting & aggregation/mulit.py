import pandas as pd

data = {
    'name':['ram', 'arun', 'rahul', 'narun', 'marun'],
    'salary':[20000, 30000, 10000, 20000, 52000],
    'age':[28, 34, 22, 34, 28]
}

df = pd.DataFrame(data)


grouped = df.groupby(['age', 'name'])['salary'].sum()
print(grouped)