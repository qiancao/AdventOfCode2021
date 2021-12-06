#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 23:58:14 2021

@author: qcao
"""

import numpy as np

ndays = 80

with open("input") as file:
    for l, ll in enumerate(file):
        ll = ll.rstrip()
        ll = ll.split(",")
        
ages = np.array(ll).astype(int)
agesList = list(ages)

for d in range(ndays):
    
    ages = np.array(agesList)
    
    ages = ages - 1
    
    numNewAges = np.sum(ages<0)
    
    ages[ages<0] = 6
    
    agesList = list(ages)
    
    for n in range(numNewAges):
        
        agesList.append(8)
        
print(len(agesList))

#%% Part II

ndays = 256

with open("input") as file:
    for l, ll in enumerate(file):
        ll = ll.rstrip()
        ll = ll.split(",")
        
ages = np.array(ll).astype(int)
histAges, histDays = np.histogram(ages,bins=np.arange(11)) # 9 elements!

for d in range(ndays):
    addTo6 = histAges[0]
    histAges = np.roll(histAges,-1)
    histAges[6] = histAges[6] + addTo6
    histAges[8] = addTo6
    histAges[-1] = 0
    
    # print(histAges)
        
print(np.sum(histAges[0:-1]))