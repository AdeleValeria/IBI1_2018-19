# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 10:21:03 2019

@author: HP
"""
from fractions import Fraction

input_numbers = input("Type some numbers between 1 and 23: ").split(",")
#Convert the integer
input_numbers = list(map(int, input_numbers))
#Check is the numbers provided by the user match the requirement or not
valid_number = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,21,23)
check = all(i in valid_number for i in input_numbers)
     
count = 0
solution = 0

if check is True: 
      
    def dfs(n):
        global count
        global solution
        count = count + 1
        
        if n == 1:
            if(float(input_numbers[0])==24):
                solution = solution + 1
                return 1
            else:
                return 0
        
        for i in range (0, n):
            for j in range(i+1, n):
                a = input_numbers[i]
                b = input_numbers[j]
                input_numbers[j] = input_numbers[n-1]
                
                input_numbers[i] = a+b
                if(dfs(n-1)):
                    return 1
                
                input_numbers[i] = b-a
                if(dfs(n-1)):
                    return 1
                
                input_numbers[i] = a*b
                if(dfs(n-1)):
                    return 1
                
                if a:
                    input_numbers[i] = Fraction(a,b)
                    if(dfs(n-1)):
                        return 1
                if b:
                    input_numbers[i] = Fraction(a,b)
                    if (dfs(n-1)):
                        return 1
                    
                input_numbers[i] = a
                input_numbers[j] = b
        return 0
    
    if (dfs(len(input_numbers))):
        print("Yes")
    else:
        print("No")
    print('Recursion times:', count,', Solution:', solution)

elif check is False:
    print("The numbers must be between 1 and 23")    