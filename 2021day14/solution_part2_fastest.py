#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: qcao

** This assumes keys are always FIXED number of characters
** This assumes no memory constraint, dictionary lookup is vectorized

"""

import numpy as np
from collections import defaultdict

insertionDict = defaultdict(str) # default value is ''

with open("input") as file:
    for l, ll in enumerate(file):
        ll = ll.rstrip()
        
        if l==0:
            polymerTemplate = ll
        
        if "->" in ll:
            ll = ll.split(" -> ")
            insertionDict[ll[0]] = ll[1]

PATTERN_NCHAR = len(list(insertionDict.keys())[0])

array2string = lambda stringArray: "".join(list(stringArray))

def interleaveStringArray(arr0,arr1):
    interleaved = np.empty((2*arr0.size,), dtype=str)
    interleaved[0::2] = arr0
    interleaved[1::2] = arr1
    return interleaved

#%% Part II not quite as fast as I'd hoped

polymer = np.array([char for char in polymerTemplate])
Nsteps = 40

for step in range(Nsteps):
    
    polymerRolled = np.roll(polymer,shift=-1)
    polymerRolled[-1] = ''
    polymerChunks = np.char.add(polymer,polymerRolled)

    inserts = np.vectorize(insertionDict.get)(polymerChunks)
    
    interleaved = interleaveStringArray(polymer,inserts)
    polymer = interleaved[:-1]
    
    print("After step "+str(step+1) + ": "+str(len(polymer)))
    
uniqueChars, uniqueCounts = np.unique(np.array([char for char in polymer]), return_counts=True)
print(np.max(uniqueCounts) - np.min(uniqueCounts))
    
    


