# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 10:05:43 2019

@author: HP
"""
#Determine n value
#Find the highest value of 2 to the power of "exponent" that is lower than the value of n
#At the same time, count how many times the multiplication has been done, store it into exponent variable
#Make one variable for the output. 


#Insert the value
n = 1500
#str(n) convert number into string
answer = str(n)+" is "

#The end point of the loop is when it reaches 0
#Therefore, while n has not reached zero, it will perform the following calculation:
while n != 0:
    m = 1
    exponent = 0

    
    while m <= n:
            m = m * 2 
            #To count how many times m has been multiplied with 2
            exponent = exponent + 1
           
    #The following code is needed to prevent error
    exponent = exponent - 1
    
    #To check the rest value
    n = n - (m/2)
    #If no has not reached 0, the plus symbol is needed. After that, the loop will continue.
    if n != 0:
        answer = answer + " 2**" + str(exponent)+ " +"
    #When n has reached zero, the plus symbol needs to be removed. 
    #The code will not return to the loop. 
    else:
        answer = answer + " 2**" + str(exponent)
#Instead, it will continue rpint the whole answer.    
print(answer)
   


