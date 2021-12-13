#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: qcao

Day 12

Compute number of paths between two vertices in an undirected graph with custom vertices.

Adjacency matrix approach

"""

import numpy as np

vertexList = []
edgeList = []
with open("test") as file:
    for l, ll in enumerate(file):
        ll = ll.rstrip()
        ll = ll.split("-")
        
        edgeList.append(ll)
        
        # Don't go back to start nor bounce back from end
        if ll[0] != "start" and ll[1] != "end":
            edgeList.append(list(reversed(ll)))
        
        if ll[0] not in vertexList:
            vertexList.append(ll[0])
        if ll[1] not in vertexList:
            vertexList.append(ll[1])

vertexNames = np.array(vertexList)
vertexTypes = np.zeros(len(vertexNames),dtype=int) # 1 for "visit once" elements
VISIT_ONCE_TYPE = 1
for ind, vertex in enumerate(vertexList):
    if vertex == vertex.lower() and vertex != "start" and vertex != "end":
        vertexTypes[ind] = VISIT_ONCE_TYPE
        
Ainit = np.zeros((len(vertexList),len(vertexList)),dtype=int) # (from,to)
for ind, edge in enumerate(edgeList):
    Ainit[vertexNames == edge[0], vertexNames == edge[1]] = 1
    
#%% Part I

A = Ainit.copy()

print()

#%% Part II
    
print()
