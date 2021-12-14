#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: qcao
"""

import numpy as np

insertionRules = []

with open("input") as file:
    for l, ll in enumerate(file):
        ll = ll.rstrip()
        
        if l==0:
            polymerTemplate = ll
        
        if "->" in ll:
            ll = ll.split(" -> ")
            insertionRules.append((ll[0],ll[1]))

def findSubstringPositions(string,substring):  
    isMatched = [string[x:x+len(substring)]==substring for x in range(len(string)-len(substring)+1)]
    return [ind for ind, matched in enumerate(isMatched) if matched == True]

#%% Part II

polymer = polymerTemplate
Nsteps = 40

# print(polymerTemplate)

for step in range(Nsteps):

    inserts = []
    for r, rule in enumerate(insertionRules):
        insertIndices = findSubstringPositions(polymer, rule[0])
        for index in insertIndices:
            inserts.append((index+1,rule[1],rule[0])) # did not find "BB"
            
    inserts.sort()
    inserts.reverse()
    
    for i, insert in enumerate(inserts):
        polymer = polymer[:insert[0]] + insert[1] + polymer[insert[0]:]
    
    print("After step "+str(step+1) + ": "+str(len(polymer)))
    uniqueChars, uniqueCounts = np.unique(np.array([char for char in polymer]), return_counts=True)
    print(np.max(uniqueCounts) - np.min(uniqueCounts))
    
    # print(inserts)
    # print(polymer)
    


