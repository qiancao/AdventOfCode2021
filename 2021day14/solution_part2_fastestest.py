#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: qcao

** Just work with histogram.
1. Insertions have predictable neighbors
2. First and last elements of template does not change

"""

import numpy as np
import itertools

stateTransitionDict = dict()
characterSet = set()

with open("input") as file:
    for l, ll in enumerate(file):
        ll = ll.rstrip()
        
        if l==0:
            polymerTemplate = ll
            
            for char in polymerTemplate:
                characterSet.add(char)
        
        if "->" in ll:
            ll = ll.split(" -> ")
            stateTransitionDict[ll[0]] = (ll[0][0]+ll[1], ll[1]+ll[0][1])
            
            characterSet.add(ll[1])
            for char in ll[0]:
                characterSet.add(char)

# Define Histogram of all string combinations
stateDictKeys = [x+y for x,y in list(itertools.product(characterSet, repeat=2))]
stateDict = dict()
for key in stateDictKeys:
    stateDict[key] = 0

# Meh
stateDictZero = stateDict.copy()

# Initialize Histogram with Polymer Template
for pos in range(len(polymerTemplate)-1):
    stateDict[polymerTemplate[pos:pos+2]] += 1

# Save first and last character for final tabulation    
charFirst = polymerTemplate[0]
charLast = polymerTemplate[-1]

# Initialize a character histogram
def tabulateCharacterCount(stateDict):
    
    characterHistogram = dict()
    for char in characterSet:
        characterHistogram[char] = 0
        
    for key in stateDict.keys():
        for keyLetter in key:
            characterHistogram[keyLetter] += 0.5*stateDict[key] # every character is double-counted
            
    characterHistogram[charFirst] += 0.5 # ... except first and last
    characterHistogram[charLast] += 0.5
    
    return characterHistogram

def countsMaxMinusMin(characterHistogram):
    counts = list(characterHistogram.values())
    return np.max(counts) - np.min(counts)
        
#%%
    
# Iterate and update stateDict
Nsteps = 40

for step in range(Nsteps):
    
    # Use this to save updates in each iteration
    stateDictUpdate = stateDictZero.copy()
    
    for key in stateDict.keys():
        
        # All instances of old sequence is destroyed
        stateDictUpdate[key] -= stateDict[key]
        # print("removing: " + key)
        
        # ... and converted to new pair of sequences
        newPairs = stateTransitionDict[key]
        for pair in newPairs:
            stateDictUpdate[pair] += stateDict[key]
            # print("adding: " + pair)
            
    for key in stateDict.keys():
        stateDict[key] += stateDictUpdate[key]
            
    print(step)
    print(int(countsMaxMinusMin(tabulateCharacterCount(stateDict))))


#     inserts = np.vectorize(insertionDict.get)(polymerChunks)
    
#     interleaved = interleaveStringArray(polymer,inserts)
#     polymer = interleaved[:-1]
    
#     print("After step "+str(step+1) + ": "+str(len(polymer)))
    
# uniqueChars, uniqueCounts = np.unique(np.array([char for char in polymer]), return_counts=True)
# print(np.max(uniqueCounts) - np.min(uniqueCounts))
    
    


