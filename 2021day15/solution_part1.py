#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: qcao

dijkstra shortest path using priority queue

"""

import numpy as np
from queue import PriorityQueue # by default, it is a min-queue

risk = list(np.loadtxt("input", dtype = str))
risk = np.array([[char for char in row] for row in risk]).astype(int)

#%% Part I

def getNeighborPositions(xy): # x is down, y is right
    neighbors = []
    if xy[0] > 0:
        neighbors.append((xy[0]-1,xy[1]))
    if xy[1] > 0:
        neighbors.append((xy[0],xy[1]-1))
    if xy[0] < risk.shape[0]-1:
        neighbors.append((xy[0]+1,xy[1]))
    if xy[1] < risk.shape[1]-1:
        neighbors.append((xy[0],xy[1]+1))
    return neighbors

# Start and ending coordinates
RISK_START = 0
positionStart = (0,0)
positionEnd = tuple(risk.shape)

# Determined risk
riskTotal = np.ones(risk.shape,dtype=int)*np.inf
riskTotal[positionStart]=RISK_START

# Queue of vertices, keyed by cost
queue = PriorityQueue()
queue.put((RISK_START,positionStart))

# Dijkstra go!
position = positionStart
while True:
    positionTotalRisk, position = queue.get()
    neighborPositions = getNeighborPositions(position)
    for neighborPosition in neighborPositions:
        riskTotalToPosition = riskTotal[position] + risk[neighborPosition]
        if riskTotalToPosition < riskTotal[neighborPosition]:
            riskTotal[neighborPosition] = riskTotal[position] + risk[neighborPosition]
            queue.put((riskTotal[neighborPosition], neighborPosition))
    # print(riskTotal)
    if queue.empty():
        break

print(riskTotal)

