#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 00:15:53 2021

@author: qcao
"""

import numpy as np

bitarray2decimal = lambda arr: int("".join(str(x) for x in arr), 2)

def filterRows(a, ind, O2orCO2):
    """
    a: np.array of 0 and 1s
    ind: starting bit index to be filtered
    O2orCO2: filtering for most ("O2") or least ("CO2") common bits
    """
    if np.size(a) == M:
        return a
    else:
        Na = a.shape[0]
        keybits = a[:,ind]
        numofones = np.sum(keybits,axis=0)

        if O2orCO2 == "O2":
            if numofones >= Na/2: # ones are more common
                indkeep = keybits==1
            else:
                indkeep = keybits==0
        elif O2orCO2 == "CO2":
            if numofones < Na/2: # zeros are more common
                indkeep = keybits==1
            else:
                indkeep = keybits==0
        b = a[indkeep,:]
        # Python lacks tail call optimization
        return filterRows(b,ind+1, O2orCO2)
               
if __name__ == "__main__":

    #%% Read input into array of bits
    text = np.loadtxt("input", dtype = str)
    N, M = len(text), len(text[1])

    arr = np.zeros((N,M),dtype=int)
    
    for n in range(N):
        for m in range(M):
            arr[n,m] = int(text[n][m])
            
    #%% Part I
    gamma = np.zeros(M,dtype=int)
    
    numofones = np.sum(arr,axis=0)
    gamma[numofones>=N/2] = 1
    gamma[numofones<N/2] = 0
    num_gamma, num_epsilon = bitarray2decimal(gamma), bitarray2decimal(1-gamma)
    print(num_gamma*num_epsilon)
    
    #%% Part II
        
    bin_O2, bin_CO2 = filterRows(arr,0,"O2")[0], filterRows(arr,0,"CO2")[0]
    O2, CO2 = bitarray2decimal(bin_O2), bitarray2decimal(bin_CO2)
    print(O2*CO2)