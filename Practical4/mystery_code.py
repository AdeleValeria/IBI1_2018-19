# What does this piece of code do?
# Answer: Show random prime number between 1 to 100

# Import libraries
# randint allows drawing a random number, 
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

p=False
while p==False:
    p=True
    #Take random value between 1 to 100
    n = randint(1,100)
    #Take the next higher integer of n^0.5 and insert the value to u
    u = ceil(n**(0.5))
    for i in range(2,u+1):
    #if the value of n can be divided by i, p = False and will return to the loop.
    #if it cannot be divided, it will print the value of n. 
        if n%i == 0:
            p=False

     
print(n)
            