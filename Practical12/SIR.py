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

#basic variables of the model
Susceptible = 9999
Infected = 1
Recover = 0


#Keep track how the variables evolve over time
#arr = {"Suspectible":[], "Infected":[], "Recovered":[]}
Suspectible = list(range(10000))
Beta = 0.3
Gamma = 0.05

#Loop over 1000 time points
for i in range (0,1000):
    """For a susceptible individual to be infected, 
    consider not only the infection rate upon contact (beta),
    but also the probability of making contact
    To get the value of making contact, multiply beta by the 
    proportion of infected people in the population"""
    Make_Contact = Beta * (Infected/N)
    Random = np.random.choice(range(2), Susceptible, p=[1-Make_Contact,Make_Contact])
    Get_Infected = sum(Random)
    #pick infected individuals at random to become recovered
    Random2 = np.random.choice(range(2), Infected, p=[0.95, 0.05])
    Get_Recovered = sum(Random2)
    Recover = Recover + Get_Recovered
    #print(Recover)
    Infected= Infected + Get_Infected - Get_Recovered
    #print(Infected)
    Susceptible=Susceptible - Get_Infected
    #print(Susceptible)
    

