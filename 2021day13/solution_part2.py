#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 11:42:24 2021

@author: qcao
"""

import numpy as np
import matplotlib.pyplot as plt

dots0 = set()
folds = []

with open("input") as file:
    for l, ll in enumerate(file):
        ll = ll.rstrip()
        if ("," in ll): 
            ll = ll.split(",")
            dots0.add((int(ll[0]), int(ll[1])))
        if ("fold along" in ll):
            ll = ll.split(" ")
            ll = ll[2].split("=")
            folds.append([ll[0], int(ll[1])])


#%% Part II

dots = dots0.copy()

for foldingIter in range(len(folds)):
    
    fold = folds[foldingIter]
    dotsToRemove = set()
    dotsToAdd = set()
    
    if fold[0] == "x":
        for dot in dots:
            if dot[0] >= fold[1]:
                print("Removing: "+str(dot))
                dotsToRemove.add(dot)
                if dot[0] > fold[1]:
                    distToFold = dot[0] - fold[1]
                    print("adding: "+str((fold[1]-distToFold,dot[1])))
                    dotsToAdd.add((fold[1]-distToFold,dot[1]))
    if fold[0] == "y":
        for dot in dots:
            if dot[1] >= fold[1]:
                print("Removing: "+str(dot))
                dotsToRemove.add(dot)
                if dot[1] > fold[1]:
                    distToFold = dot[1] - fold[1]
                    print("adding: "+str((dot[0],fold[1]-distToFold)))
                    dotsToAdd.add((dot[0],fold[1]-distToFold))
                    
    dots = (dots - dotsToRemove) | dotsToAdd
    
dotsArray = np.array(list(dots))
plt.figure()
plt.plot(dotsArray[:,0], dotsArray[:,1],'x')
plt.gca().invert_yaxis()