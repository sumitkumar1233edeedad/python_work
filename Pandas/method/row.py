import pandas as pd

'''
    head() tail()
    head(n) first row
    head() 5 row
    tail(n) last row show
    tail() last 5 row show
'''
df = pd.read_json('sample_Data.json')

print('display five row of first')
print(df.head(5))

print('display the five row of last')
print(df.tail(5))
