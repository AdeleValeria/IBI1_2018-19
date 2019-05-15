# -*- coding: utf-8 -*-
"""
Created on Wed May 15 09:11:31 2019

@author: HP
"""

import os
import xml.dom.minidom
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Convert the xml file to cps
#def xml_to_cps():
#    os.system("C:\GitKraken\IBI1_2018-19\Practical13\CopasiSE -i predator-prey.xml -s predator-prey.cps")
    
#    cpsTree = xml.dom.minidom.parse("predator-prey.cps")
#    cpsCollection = cpsTree.documentElement
    
#    reportFile = xml.dom.minidom.parse("report_ref.xml")
#    reportLine = reportFile.documentElement
    
#    tasks = cpsCollection.getElementsByTagName("Task")
#    for task in tasks:
#        if task.getAttribute("name")=="Time-Course":
#            task.setAttribute("scheduled","true")
#            task.insertBefore(reportLine,task.childNodes[0])
#            break
        
    
#    for taskDetails in task.childNodes:
#        if taskDetails.nodeType ==1:
#            if taskDetails.nodeName == "Problem":
#                problem = taskDetails
                
#    for param in problem.childNodes:
#        if param.nodeType ==1:
#            if param.getAttribute("name")=="StepNumber":
#                param.setAttribute("value","200")
#            if param.getAttribute("name")=="StepSize":
#                param.setAttribute("value","1")
#            if param.getAttribute("name")=="Duration":
#                param.setAttribute("value","200")
           
            
#    report18 = xml.dom.minidom.parse("report18.xml")
#    report = report18.documentElement
    
#    listOfReports  =  cpsCollection.getElementsByTagName("ListOfReports")[0]
#    listOfReports.appendChild(report)
    
#    cpsFile = open("predator-prey.cps","w", encoding = "utf-8")
#    cpsTree.writexml(cpsFile)
#    cpsFile.close()
    
#xml_to_cps()

#Reading and plotting simulation results
model = pd.read_csv("modelResults.csv")
header = model.columns.tolist()
header[0]=[]
header[1]=[]
header[2]=[]
Arr = []

for index, row in model.iterrows():
    #make a list for each column
    header[0].append(row[0])
    header[1].append(row[1])
    header[2].append(row[2])
    #make a list for each row
    Arr.append([row[0],row[1], row[2]])
Results = np.array(Arr)
Results = Results.astype(np.float)

#Plotting
plt.figure(figsize=(6,4),dpi=120)
plt.plot(header[1], label = "Predator") 
plt.plot(header[2], label = "Prey Population")
plt.xlabel('Time')
plt.ylabel('Population Size')
plt.title('Time Course')
plt.legend()
#gcf : get current figure
plt.gcf()
plt.show
#blank figure will be saved if gcf is not used
plt.gcf().savefig('Time course of the predator and prey population.png')

#Limit cycle plot
plt.figure(figsize=(6,4),dpi=120)
plt.plot(header[1], header[2]) 
plt.xlabel('Predator Population')
plt.ylabel('Prey Population')
plt.title('Limit Cycle')
plt.legend()
#gcf : get current figure
plt.gcf()
plt.show
plt.gcf().savefig('predator population against prey population.png')