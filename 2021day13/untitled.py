#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: qcao
"""

import numpy as np
import matplotlib.pyplot as plt

dots0 = set()
folds = []

with open("test") as file:
    for l, ll in enumerate(file):
        ll = ll.rstrip()
        if ("," in ll): 
            ll = ll.split(",")
            dots0.add((int(ll[0]), int(ll[1])))
        if ("fold along" in ll):
            ll = ll.split(" ")
            ll = ll[2].split("=")
            folds.append([ll[0], int(ll[1])])


#%% Part I Only the first fold

dots = dots0.copy()

print(len(dots0))

fold = folds[0]
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

print(len(dots))

dotsArray = np.array(list(dots))
plt.figure()
plt.plot(dotsArray[:,1], dotsArray[:,0],'x')
plt.close("all")

#%% DEBUG - This shows a square

fold = folds[1]
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
plt.plot(dotsArray[:,1], dotsArray[:,0],'x')
plt.close("all")