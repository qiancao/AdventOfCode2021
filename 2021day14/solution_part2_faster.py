#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: qcao

** This assumes keys are always FIXED number of characters
How is this so low, python has O(1) dictionary lookup...

"""

import numpy as np
from collections import defaultdict

insertionDict = defaultdict(str) # default value is ''

with open("test") as file:
    for l, ll in enumerate(file):
        ll = ll.rstrip()
        
        if l==0:
            polymerTemplate = ll
        
        if "->" in ll:
            ll = ll.split(" -> ")
            insertionDict[ll[0]] = ll[1]

PATTERN_NCHAR = len(list(insertionDict.keys())[0])

array2string = lambda stringArray: "".join(list(stringArray))

def findSubstringAndReplace(string,insertionDict):
    inserts = np.empty(len(string),dtype=str)
    inserts[:] = ""
    for pos in range(len(string)):
        inserts[pos:(pos+PATTERN_NCHAR)] = insertionDict[string[pos:(pos+PATTERN_NCHAR)]]
    return inserts

#%% Part II not quite as fast as I'd hoped

polymer = np.array([char for char in polymerTemplate])
Nsteps = 10

for step in range(Nsteps):

    inserts = findSubstringAndReplace(array2string(polymer),insertionDict)
    
    interleaved = np.empty((2*inserts.size,), dtype=str)
    interleaved[0::2] = polymer
    interleaved[1::2] = inserts
    polymer = interleaved[:-1]
    
    print("After step "+str(step+1) + ": "+str(len(polymer)))
    
uniqueChars, uniqueCounts = np.unique(np.array([char for char in polymer]), return_counts=True)
print(np.max(uniqueCounts) - np.min(uniqueCounts))
    
    


