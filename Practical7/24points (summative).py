# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 10:21:03 2019

@author: Adele
"""
from fractions import Fraction

input_numbers = input("Type some numbers between 1 and 23: ").split(",")
#Convert the integer
input_numbers = list(map(int, input_numbers))
#Check if the numbers provided by the user match the requirement or not
valid_number = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,21,23)
check = all(i in valid_number for i in input_numbers)
     
count = 0

if check is True: 
#Create a function for recursion     
    def cnt(n):
        global count
        count = count + 1
        
        if n == 1:
            if(float(input_numbers[0])==24):
                return 1
            else:
                return 0
        
        for i in range (0, n):
            for j in range(i+1, n):
                a = input_numbers[i]
                b = input_numbers[j]
                input_numbers[j] = input_numbers[n-1]
                
                #Test all arithmetic combinations for two numbers
                input_numbers[i] = a+b
                if(cnt(n-1)):
                    return 1
                
                input_numbers[i] = b-a
                if(cnt(n-1)):
                    return 1
                
                input_numbers[i] = a*b
                if(cnt(n-1)):
                    return 1
                
                #divident is zero
                if a:
                    input_numbers[i] = Fraction(b,a)
                    if(cnt(n-1)):
                        return 1
                if b:
                    input_numbers[i] = Fraction(a,b)
                    if (cnt(n-1)):
                        return 1
                    
                input_numbers[i] = a
                input_numbers[j] = b
        return 0
    
    if (cnt(len(input_numbers))):
        print("Yes")
    else:
        print("No")
    #Count is the value for recursion times
    print('Recursion times:', count)

#if the input number is not between 1 and 23
elif check is False:
    print("The numbers must be between 1 and 23")   