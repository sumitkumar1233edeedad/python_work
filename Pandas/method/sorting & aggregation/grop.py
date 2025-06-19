import pandas as pd

data = {
    'name':['ram', 'arun', 'rahul', 'narun', 'marun'],
    'salary':[20000, 30000, 10000, 20000, 52000],
    'age':[28, 34, 22, 34, 28]
}

df = pd.DataFrame(data)


grouped = df.groupby('age')['salary'].sum()
print(grouped)
'''
groupby function:-> 
        work: 
            dr.groupby('age')
            age = 22 > [10,000]
            age = 28  [20,000,   52,000]
            age = 34  [30,000, 20,000]
            
            ['salary'].sum()
            age = 22 > [10,000] = 10,000
            age = 28  [20,000,   52,000] = 72,000
            age = 34  [30,000, 20,000] = 50,000        
'''
