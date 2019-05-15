# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 22:36:05 2019


@author: Adele
"""

#BLOSUM62 matrix
def get_blosum62_dictionary():
    blosum_raw = """A  4 -1 -2 -2  0 -1 -1  0 -2 -1 -1 -1 -1 -2 -1  1  0 -3 -2  0 -2 -1  0 -4 
R -1  5  0 -2 -3  1  0 -2  0 -3 -2  2 -1 -3 -2 -1 -1 -3 -2 -3 -1  0 -1 -4 
N -2  0  6  1 -3  0  0  0  1 -3 -3  0 -2 -3 -2  1  0 -4 -2 -3  3  0 -1 -4 
D -2 -2  1  6 -3  0  2 -1 -1 -3 -4 -1 -3 -3 -1  0 -1 -4 -3 -3  4  1 -1 -4 
C  0 -3 -3 -3  9 -3 -4 -3 -3 -1 -1 -3 -1 -2 -3 -1 -1 -2 -2 -1 -3 -3 -2 -4 
Q -1  1  0  0 -3  5  2 -2  0 -3 -2  1  0 -3 -1  0 -1 -2 -1 -2  0  3 -1 -4 
E -1  0  0  2 -4  2  5 -2  0 -3 -3  1 -2 -3 -1  0 -1 -3 -2 -2  1  4 -1 -4 
G  0 -2  0 -1 -3 -2 -2  6 -2 -4 -4 -2 -3 -3 -2  0 -2 -2 -3 -3 -1 -2 -1 -4 
H -2  0  1 -1 -3  0  0 -2  8 -3 -3 -1 -2 -1 -2 -1 -2 -2  2 -3  0  0 -1 -4 
I -1 -3 -3 -3 -1 -3 -3 -4 -3  4  2 -3  1  0 -3 -2 -1 -3 -1  3 -3 -3 -1 -4 
L -1 -2 -3 -4 -1 -2 -3 -4 -3  2  4 -2  2  0 -3 -2 -1 -2 -1  1 -4 -3 -1 -4 
K -1  2  0 -1 -3  1  1 -2 -1 -3 -2  5 -1 -3 -1  0 -1 -3 -2 -2  0  1 -1 -4 
M -1 -1 -2 -3 -1  0 -2 -3 -2  1  2 -1  5  0 -2 -1 -1 -1 -1  1 -3 -1 -1 -4 
F -2 -3 -3 -3 -2 -3 -3 -3 -1  0  0 -3  0  6 -4 -2 -2  1  3 -1 -3 -3 -1 -4 
P -1 -2 -2 -1 -3 -1 -1 -2 -2 -3 -3 -1 -2 -4  7 -1 -1 -4 -3 -2 -2 -1 -2 -4 
S  1 -1  1  0 -1  0  0  0 -1 -2 -2  0 -1 -2 -1  4  1 -3 -2 -2  0  0  0 -4 
T  0 -1  0 -1 -1 -1 -1 -2 -2 -1 -1 -1 -1 -2 -1  1  5 -2 -2  0 -1 -1  0 -4 
W -3 -3 -4 -4 -2 -2 -3 -2 -2 -3 -2 -3 -1  1 -4 -3 -2 11  2 -3 -4 -3 -2 -4 
Y -2 -2 -2 -3 -2 -1 -2 -3  2 -1 -1 -2 -1  3 -3 -2 -2  2  7 -1 -3 -2 -1 -4 
V  0 -3 -3 -3 -1 -2 -2 -3 -3  3  1 -2  1 -1 -2 -2  0 -3 -1  4 -3 -2 -1 -4 
B -2 -1  3  4 -3  0  1 -1  0 -3 -4  0 -3 -3 -2  0 -1 -4 -3 -3  4  1 -1 -4 
Z -1  0  0  1 -3  3  4 -2  0 -3 -3  1 -1 -3 -1  0 -1 -3 -2 -2  1  4 -1 -4 
X  0 -1 -1 -1 -2 -1 -1 -1 -1 -1 -1 -1 -1 -1 -2  0  0 -2 -1 -1 -1 -1 -1 -4 
* -4 -4 -4 -4 -4 -4 -4 -4 -4 -4 -4 -4 -4 -4 -4 -4 -4 -4 -4 -4 -4 -4 -4  1 """
    
    #split each line in the matrix into row
    blosum_array1=[row.split(" ") for row in blosum_raw.split("\n")]   
    #c refers to each aplhabet in the row
    blosum_array2= [[c for c in row if c!=""] for row in blosum_array1]
    
    blosum62 = {}
    blosum_entry_count = len(blosum_array2)
    for j in range(0, blosum_entry_count):
        for k in range(1,blosum_entry_count):
            row = blosum_array2[j]
            key = row[0] + blosum_array2[k-1][0]
            #the score
            value = int(row[k])
            #match each pair with its value, make a dictionary
            blosum62[key] = value
    return blosum62

#main menu
task = input("Select task (input 1, 2 or 3):\n 1. Human-mouse\n 2. Human-random\n 3. Mouse-random\n")
if task == '1':
#HUMAN - MOUSE
    #'with open' closes automatically
    with open('Human.txt') as s1:
        s1_read = s1.read()
    with open('Mouse.txt') as s2:
        s2_read = s2.read()
    
elif task == '2':
#HUMAN - RANDOM
    with open('Human.txt') as s1:
        s1_read = s1.read()
    with open('Random.txt') as s2:
        s2_read = s2.read()

elif task == '3':
#MOUSE - RANDOM
     with open('Mouse.txt') as s1:
        s1_read = s1.read()
     with open('Random.txt') as s2:
        s2_read = s2.read()

   
score = 0
match = 0
align = []
for i in range (len(s1_read)):
    x = s1_read[i] + s2_read[i]
    compare = get_blosum62_dictionary()
    score = score + compare[x]
    
    if s1_read[i] == s2_read[i]:
        match += 1
        align.append(s1_read[i])
    elif compare[x]>0:
        align.append('+')
    else:
        align.append('-')

#Calculate normalized score
normalized = score/len(s1_read)

#calculate the percentage identity (how many amino acids are identical)        
perc = (match*100)/len(s1_read)

print('\nBLOSUM62 score:', score)
#%.2f means 2 numbers after decimal
print('\nNormalized score:', '%.2f' % normalized)
print('\nPercentage identity :', '%.2f' % perc, '%\n')
#to join the list into a single string
print(*align, sep='')