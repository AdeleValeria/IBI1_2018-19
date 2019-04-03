# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 09:42:57 2019

@author: HP
"""
#To specify the range of input to be between 1 to 23
acceptable_values = list(range(1, 24))
num = input("Please input numbers to compute 24 (use a comma to separate the number):")
x = num.split(",")
for i in range(0, len(x)): 
   x[i] = int(x[i]) 
for i in range(0,len(x)):
    if x[i]>= 1 and x[i]<24:
        continue
    else:
        print("The input number must be integers from 1 to 23")
        break
    
