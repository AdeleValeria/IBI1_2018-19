# -*- coding: utf-8 -*-
"""
Created on Sat April  20 20:21:48 2019

@author: Adele
"""

import xml.dom.minidom
import pandas as pd
import re

result = set()
def Child(id_no, result):
    for i in collection:
        parents = i.getElementsByTagName("is_a")
        cnodes = i.getElementsByTagName("id")[0].childNodes[0].data
        for j in parents:
            if j.childNodes[0].data == id_no:
                result.add(cnodes)
                Child(cnodes, result)
                

DOMTree = xml.dom.minidom.parse("go_obo.xml")
collection = DOMTree.documentElement.getElementsByTagName("term")

df = pd.DataFrame(columns=['ID','Name','Definition','Childnodes'])

for term in collection:
    desc = term.getElementsByTagName("defstr")[0].childNodes[0].data
    if re.search("autophagosome", desc):
        id_no = term.getElementsByTagName("id")[0].childNodes[0].data
        name = term.getElementsByTagName("name")[0].childNodes[0].data
        defn = term.getElementsByTagName("defstr")[0].childNodes[0].data
    
        Child(id_no, result)
        dc = {"ID":[id_no], "Name":[name], "Definition":[defn], "Childnodes":[len(result)]}
        df = df.append(pd.DataFrame(data = dc))
        
df.to_excel(r'C:\GitKraken\IBI1_2018-19\Practical8\Autophagosome.xlsx', index=False)
        
        
        
    