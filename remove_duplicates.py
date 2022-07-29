#! /usr/bin/python/

#import packages
import pandas as pd

#Declare variables
data = {
  "patient": ['001', '002', '003','002','004', '005','006','007','008'],
    "disease": ['A', 'B','A', 'B','A', 'B','B','A', 'B'],
    "age": [15,8,5,8,-9,6,0,6,12]
}

#load data into a DataFrame object:
df = pd.DataFrame(data)

#Remove duplicates 
dup_removed_data = df.drop_duplicates()

#Print the information with duplicates removed
print(dup_removed_data) 
