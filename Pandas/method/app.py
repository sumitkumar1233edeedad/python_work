import pandas as pd
''' 

this method is show the how to data read for the author file pandas library use than easily access the
file.

like that :
            pd.read_than_file_extension('show the file name' , encoding add latin1)
            

'''
df = pd.read_csv("sales_data_sample.csv", encoding="latin1")
df1 = pd.read_json('sample_Data.json')
#google data access method  gcsfs
# print(df)
print(df1)

