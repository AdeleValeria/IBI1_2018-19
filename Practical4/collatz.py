# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 23:54:51 2019

@author: HP
"""
#Make a function which calculates the Collatz sequence
#Check if the number is even
#Check if the number is odd
#Repeat the function until it reaches 1

def collatz(n):
    if (n % 2 == 0): 
        n = n / 2
    else:
        n = n * 3 + 1
    print (n)
    return (n)

n = 100
while (n != 1):
    n = collatz(n)