#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: qcao
"""

import numpy as np
from scipy.signal import convolve2d
        
e0 = list(np.loadtxt("input", dtype = str))
e0 = np.array([[char for char in erow] for erow in e0]).astype(int)

#%% Part I

Nsteps = 100
totalNflashes = 0
e = e0.copy()
for s in range(Nsteps):
    e += 1
    ef = np.zeros(e.shape,dtype=bool) # mask for flashed elements
    while True:
        ef = ef | (e>9) # apparently, | takes precedence over >
        ec = convolve2d(e>9,np.ones((3,3)),'same').astype(int)
        e[np.invert(ef)] += ec[np.invert(ef)]
        e[ef] = 0
        if np.sum(e[np.invert(ef)]>9) == 0:
            break
    totalNflashes += np.sum(ef)
    
print(totalNflashes)

#%% Part II

step = 0
e = e0.copy()
while (True):
    e += 1
    ef = np.zeros(e.shape,dtype=bool) # mask for flashed elements
    while True:
        ef = ef | (e>9) # apparently, | takes precedence over >
        ec = convolve2d(e>9,np.ones((3,3)),'same').astype(int)
        e[np.invert(ef)] += ec[np.invert(ef)]
        e[ef] = 0
        if np.sum(e[np.invert(ef)]>9) == 0:
            break
    step += 1
    if np.sum(ef == True) == np.size(ef):
        break

print(step)