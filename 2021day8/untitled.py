#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: qcao
"""

import numpy as np
from itertools import permutations
from collections import defaultdict

signalList = []
outputList = []

with open("input") as file:
    for l, ll in enumerate(file):
        ll = ll.rstrip()
        ll = ll.split("|")
        
        signalList.append(ll[0].split())
        outputList.append(ll[1].split())
        
#%% Part I
outputCharLengths = np.zeros((len(outputList),4))
for ind in range(len(outputList)):
    output = outputList[ind]
    outputCharLengths[ind,:] = np.array([len(x) for x in output])
    
total_number = 0
for num in [2,4,3,7]:
    total_number = total_number + np.sum(outputCharLengths == num)
    
print(total_number)

#%% Part II

numbers = np.arange(10)
displayCodes = ["abcefg","cf","acdeg","acdfg", # 0 1 2 3
                "bdcf","abdfg","abdefg", # 4 5 6
                "acf","abcdefg","abcdfg"] # 7 8 9
display2num = defaultdict(lambda: None)
for ind in range(len(numbers)):
    display2num[frozenset(displayCodes[ind])] = str(numbers[ind])

segments = "abcdefg"
segmentsPermuted = list(permutations(segments))

total_sum = 0
for ind, (signal, output) in enumerate(zip(signalList, outputList)):
    
    number = -1
    for segmentsTuple in segmentsPermuted:
        
        segments2display = {segmentsTuple[i] : segments[i] for i in range(len(segmentsTuple))}
        
        numList = []
        for ind, string in enumerate(signal):
            displayString = frozenset("".join([segments2display[char] for char in string]))
            numList.append(display2num[displayString])

        if None not in numList:
            number = int("".join(numList))
            segments2displaySolution = segments2display
            break
    
    numList = []
    for ind, string in enumerate(output):
        displayString = frozenset("".join([segments2displaySolution[char] for char in string]))
        numList.append(display2num[displayString])

    if None not in numList:
        number = int("".join(numList))
        
    total_sum = total_sum + number
    
print(total_sum)