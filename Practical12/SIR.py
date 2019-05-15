# -*- coding: utf-8 -*-
"""
Created on Wed May  8 09:14:40 2019

@author: HP
"""

#import neccesary libraries
import numpy as np
import matplotlib.pyplot as plt

#population 
N = 10000

Susceptible = 9999
Infected = 1
Recover = 0

Beta = 0.3
Gamma = 0.05
S = []
I = []
R = []

#Loop over 1000 time points
for i in range (0,1000):
    """For a susceptible individual to be infected, 
    consider not only the infection rate upon contact (beta),
    but also the probability of making contact
    To get the value of making contact, multiply beta by the 
    proportion of infected people in the population"""
    Make_Contact = Beta * (Infected/N)
    """First the set from which to choose elements, second the
    number of elements to be chosen and third a list of probabilities for choosing each member
    of a set.""" 
    Random = np.random.choice(range(2), Susceptible, p=[1-Make_Contact, Make_Contact])
    Get_Infected = sum(Random)
    #pick infected individuals at random to become recovered
    Random2 = np.random.choice(range(2), Infected, p=[1-Gamma, Gamma])
    Get_Recovered = sum(Random2)
    Recover = Recover + Get_Recovered
    Infected= Infected + Get_Infected - Get_Recovered
    Susceptible=Susceptible - Get_Infected
    S.append(Susceptible)
    I.append(Infected)
    R.append(Recover)

 
#SIR figure
plt.figure(figsize=(6,4),dpi=150)
plt.plot(S, label = "Susceptible") 
plt.plot(I, label = "Infected")
plt.plot(R, label = "Recover")
plt.xlabel('Time')
plt.ylabel('Number of People')
plt.title('SIR Model')
plt.legend()
#gcf : get current figure
plt.gcf()
plt.show
#blank figure will be saved if gcf is not used
plt.gcf().savefig('SIR.png')