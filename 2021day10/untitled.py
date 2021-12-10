#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: qcao
"""

import numpy as np

nav = []

with open("input") as file:
    for l, ll in enumerate(file):
        ll = ll.rstrip()
        nav.append(ll)

#%% Part I

expectedCharDict = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<'
    }

charPointsDict = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
    }

wrongChar = []
stack = []
for line in nav:
    for ind, char in enumerate(line):
        # a better way to write this is char in '([{<'
        if (char == '(') or (char == '[') or (char == '{') or (char == '<'):
            stack.append(char)
        elif char == ")" or char == ']' or char == '}'  or (char == '>'):
            popped = stack.pop()
            if popped != expectedCharDict[char]:
                wrongChar.append(char)
                break
            
score = 0            
for char in wrongChar:
    # print(char)
    score = score + charPointsDict[char]

# print(score)

#%% Part II

completePointsDict = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4
    }

completeScoreList = []

for line in nav:
    stack = []
    for ind, char in enumerate(line):
        if (char == '(') or (char == '[') or (char == '{') or (char == '<'):
            stack.append(char)
        elif char == ")" or char == ']' or char == '}'  or (char == '>'):
            popped = stack.pop()
            if popped != expectedCharDict[char]:
                wrongChar.append(char)
                break
        if ind == len(line)-1 and len(stack) != 0: # incomplete lines
            completeScore = 0
            for charleft in stack[::-1]:
                completeScore = completeScore * 5
                completeScore = completeScore + completePointsDict[charleft]
            print(stack[::-1])
            print(completeScore)
            completeScoreList.append(completeScore)

scores = np.array(completeScoreList)
scores.sort()
print(int(np.median(scores)))