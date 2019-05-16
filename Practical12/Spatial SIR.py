# -*- coding: utf-8 -*-
"""
Created on Thu May 16 14:06:25 2019

@author: HP
"""

import numpy as np
import matplotlib.pyplot as plt

#make array of all susceptible population
#0: susceptible, 1: infected, 2:recovered
population = np.zeros((100,100))
'''randomly select the x and y coordinates of where the outbreak
is happening and store this in an array called outbreak'''
#Pick 2 random numbers between 1 and 100
outbreak = np.random.choice(range(100),2)
#Because the outbreak numbers are in array, we use index to call.
#Change the value in row, column coordinate to 1 (infected)
population[outbreak[0], outbreak[1]] = 1
#infection rate upon contact
beta = 0.3
#recovery probability
gamma = 0.05

#loop 100 times
for j in range(0,101):
    # find infected points because 1 is infected
    infectedIndex = np.where(population==1)
    # loop through all infected points
    for i in range(len(infectedIndex[0])):
        # get x, y coordinates for each point
        # from the first arrray, take the i position
        x = infectedIndex[0][i]
        #from the second array, take the i position
        y = infectedIndex[1][i]
        
        # infect each neighbour with probability beta
        # infect all 8 neighbours
        for xNeighbour in range(x-1,x+2):
            for yNeighbour in range(y-1,y+2):
                if (xNeighbour,yNeighbour) != (x,y):
                    if xNeighbour != -1 and yNeighbour != -1 and xNeighbour!=100 and yNeighbour!=100:
                        # only infect neighbours that are not already infected
                        if population[xNeighbour,yNeighbour]==0:
                            #choose 0 or 1
                            population[xNeighbour,yNeighbour]=np.random.choice(range(2),1,p=[1-beta,beta])[0] 

        #choose 1 or 2(recover)
        population[x,y]=np.random.choice(range(1,3),1,p=[1-gamma,gamma])[0]
       
    #plot the graph for time point 0,10,50 and 100
    time=[0,10,50,100]
    if j in time:
        plt.figure(figsize=(6,4),dpi=130)
        #gcf : get current figure
        plt.gcf()
        plt.imshow(population,cmap='viridis',interpolation='nearest')
        plt.title('Spatial SIR '+str(j))
        #blank figure will be saved if gcf is not used
        plt.gcf().savefig('Spatial SIR '+str(j))