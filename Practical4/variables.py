# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 09:20:14 2019

@author: HP
"""
#Exercise some simple math
a = 123
b = 123456
#To check if b can be divided by 7 or not
if b%7 == 0:
    print ("b can be divided by 7")
else:
    print ("b cannot be divided by 7")
    
c = b/7
d = c/11
e = d/13
print ("The value of e is " +str(e)+ ". Therefore, ")
#To check is e is bigger than a or not
if e>a:
    print ("e is bigger than a")
else:
    print ("a is bigger than e")
    




#Booleans either x or y
X = True
Y = False
Z = (X and not Y) or (Y and not X)
print (Z) #Z will be false

#Exercise 4.2 sub 3
W = X != Y
print (W) 
#Note: if both values are true, the Z and W will show "false"
if str(Z) == str(W):
    print ("Therefore, Z and W are the same")
else:
    print ("Therefore, Z and W are different")