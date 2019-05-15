# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 22:36:05 2019


@author: HP
"""

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
    
    blosum_array1=[row.split(" ") for row in blosum_raw.split("\n")]   
    blosum_array2= [[c for c in row if c!=""] for row in blosum_array1]
    
    blosum62 = {}
    blosum_entry_count = len(blosum_array2)
    for j in range(0, blosum_entry_count):
        for k in range(1,blosum_entry_count): #skipping the first column which has the residue code still
            #the residues codes are all in the first column
            row = blosum_array2[j]
            key = row[0] + blosum_array2[k-1][0]
            value = int(row[k])
            blosum62[key] = value
    return blosum62

task = input("Select task:\n 1. Human-mouse\n 2. Human-random\n 3. Mouse-random\n")
if task == '1':
#HUMAN - MOUSE
    s1 = input("File path of human sequence (please include .txt):\n")
    with open(s1) as s1_open:
        s1_read = s1_open.read()
    s2 = input("File path of mouse sequence (please include .txt):\n")
    with open(s2) as s2_open:
        s2_read = s2_open.read()
    
elif task == '2':
#HUMAN - RANDOM
    s1 = input("File path of human sequence (include .txt):\n")
    with open(s1) as s1_open:
        s1_read = s1_open.read()
    s2 = input("File path of random sequence (include .txt):\n")
    with open(s1) as s2_open:
        s2_read = s2_open.read()

elif task == '3':
#MOUSE - RANDOM
     s1 = input("File path of mouse sequence (include .txt):\n")
     with open(s1) as s1_open:
        s1_read = s1_open.read()
     s2 = input("File path of random sequence (include .txt):\n")
     with open(s2) as s2_open:
        s2_read = s2_open.read()

   
score = 0
match = 0
for i in range (len(s1_read)):
    x = s1_read[i] + s2_read[i]
    compare = get_blosum62_dictionary()
    score = score + compare[x]
    
    if s1_read[i] == s2_read[i]:
        match += 1
perc = (match*100)/len(s1_read)
print('\nBLOSUM62 score:', score)
print('Percentage identity :', '%.2f' % perc, '%')


