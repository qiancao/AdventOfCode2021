#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: qcao

dijkstra shortest path using priority queue

"""

import numpy as np
from queue import PriorityQueue # by default, it is a min-queue

risk0 = list(np.loadtxt("input", dtype = str))
risk0 = np.array([[char for char in row] for row in risk0]).astype(int)

def tilePlusH(x,h):
    x = x.copy()
    for step in range(h):
        x += 1
        x[x==10] = 1
    return x

#%%

risk = risk0.copy()
for nx in range(4):
    risk = np.hstack((risk,tilePlusH(risk0,nx+1)))
    
risk0 = risk.copy()
for ny in range(4):
    risk = np.vstack((risk,tilePlusH(risk0,ny+1)))

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

print(int(riskTotal[-1,-1]))