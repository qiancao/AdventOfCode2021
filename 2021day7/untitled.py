#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 23:58:14 2021

@author: qcao
"""

import numpy as np

with open("input") as file:
    for l, ll in enumerate(file):
        ll = ll.rstrip()
        ll = ll.split(",")
        
hpos = np.array(ll).astype(int)

#%% Part I
targetpos = np.arange(np.max(hpos)+1)

fuel = np.sum(np.abs(hpos[:,None]-targetpos[None,:]),axis=0)
print(np.min(fuel))

#%% Part II

def fuelfunc(x):
    dist = np.abs(x)
    return dist*(dist+1)/2

fuel = np.sum(fuelfunc(hpos[:,None]-targetpos[None,:]),axis=0)
print(np.min(fuel))
