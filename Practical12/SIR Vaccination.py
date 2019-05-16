# -*- coding: utf-8 -*-
"""
Created on Wed May 15 23:31:23 2019

@author: Adele
"""

#import neccesary libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

for i in range (0, 11):
    N = 10000
    Beta = 0.3
    Gamma = 0.05
    S = []
    I = []
    R = []
    Vaccinated = i * 0.1 *N
    if Vaccinated == N:
        Infected = 0
        Susceptible = 0
    else:
        Susceptible = int(9999-Vaccinated)
        Infected = 1
    Recover = 0
    
    #Loop over 1000 time points
    j = 0
    while j <=1000:
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
        j += 1
        
         
    
    n = i * 10
    plt.plot(I, label=str(n)+'%',color=cm.viridis(i*35))
    plt.xlabel('Time')
    plt.ylabel('Number of People')
    plt.title('SIR MODEL WITH DIFFERENT VACCINATION RATES')
    plt.legend()
    #gcf : get current figure
    plt.gcf()
    plt.show
    #blank figure will be saved if gcf is not used
    plt.gcf().savefig('SIR vaccination 0 - 100%.png')