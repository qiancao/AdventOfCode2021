#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: qcao
"""

import numpy as np

insertionRules = []

with open("test") as file:
    for l, ll in enumerate(file):
        ll = ll.rstrip()
        
        if l==0:
            polymerTemplate = ll
        
        if "->" in ll:
            ll = ll.split(" -> ")
            insertionRules.append((ll[0],ll[1]))

array2string = lambda stringArray: "".join(list(stringArray))

def findSubstringPositions(string,substring):
    isMatched = [string[x:x+len(substring)]==substring for x in range(len(string)-len(substring)+1)]
    isMatched.append(False)
    return np.array(isMatched)

#%% Part II not quite as fast as I'd hoped

polymer = np.array([char for char in polymerTemplate])
Nsteps = 10

for step in range(Nsteps):

    inserts = np.empty(len(polymer),dtype=str)
    inserts[:] = ""
    
    for r, rule in enumerate(insertionRules):
        insertIndices = findSubstringPositions(array2string(polymer), rule[0])
        inserts[insertIndices] = rule[1]
    
    interleaved = np.empty((2*inserts.size,), dtype=str)
    interleaved[0::2] = polymer
    interleaved[1::2] = inserts
    polymer = interleaved[:-1]
    
    print("After step "+str(step+1) + ": "+str(len(polymer)))
    uniqueChars, uniqueCounts = np.unique(np.array([char for char in polymer]), return_counts=True)
    print(polymer)
    print(np.max(uniqueCounts) - np.min(uniqueCounts))
    
    


