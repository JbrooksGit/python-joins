#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 16:41:35 2019

@author: jonathanbrooks
"""
import csv
import pandas as pd
import numpy as np

data = pd.read_csv("subjects.csv")
#data[['last_name','first_name','dob']] #pandas two dimensional series

data2 = pd.read_csv("test.csv",delimiter = ',',na_values = ['no info', '.'])
#print(data2.head()) #prints out number of rows based on argument of head
#print(data2['last_name'][:]) #prints out all last names
#row2 = data2.iloc[0] #prints out specific row. this one prints out abate
merged = data.merge(data2, on = 'last_name' and 'first_name' and 'dob')
#for i,j in data2.head().iterrows(): #the i is the index while the j is the row
 #   print(j)
 
merged.to_csv("output.csv", index=False)
 
#print(row2)
 
 
#data2.last_name == 'brooks'
#data2[data2.last_name == 'abate']
#liste = [row for row in data2]
'''
df2 = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
            columns=['a', 'b', 'c'])
print(df2)
'''