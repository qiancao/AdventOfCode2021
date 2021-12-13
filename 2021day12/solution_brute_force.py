#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: qcao

Day 12

Compute number of paths between two vertices in an undirected graph with custom vertices.
https://stackoverflow.com/questions/15448658/creating-tree-structured-list-from-nested-list

"""

import numpy as np
from scipy.sparse.csgraph import depth_first_tree

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

graph = dict()
singleVisitVertices = set()
for vertex in vertexList:
    graph[vertex] = [edge[1] for edge in edgeList if edge[0]==vertex]
    if vertex == vertex.lower() and vertex != "start" and vertex != "end":
        singleVisitVertices.add(vertex)

#%% Part I Record all paths

def updateBlockedVertexList(newVertex, currentBlockedVertices):
    blockedVertices = currentBlockedVertices.copy()
    if (newVertex in singleVisitVertices) \
        and (newVertex not in blockedVertices):
            blockedVertices.append(newVertex)
    return blockedVertices

def traverse(currentPath, blockedVertices):
    nextVertexList = [vert for vert in graph[currentPath[-1]] if vert not in blockedVertices]
    nextPathList = []
    blockedVerticesList = []
    if len(nextVertexList) == 0: # end of path
        nextPathList.append(currentPath.copy())
        blockedVerticesList.append(blockedVertices.copy())
    else:
        for nextVertex in nextVertexList:
            nextPath = currentPath.copy()
            nextPath.append(nextVertex)
            nextPathList.append(nextPath)
            blockedVerticesList.append(updateBlockedVertexList(nextVertex, blockedVertices))
    return nextPathList, blockedVerticesList
    
blockedVerticesList = [[]]
currentPathList = [["start"]]

while (True):
    currentPathList0 = currentPathList.copy()
    for currentPath, blockedVertices in zip(currentPathList.copy(), blockedVerticesList.copy()):
        nextPathList, nextBlockVertices = traverse(currentPath, blockedVertices)
        currentPathList.extend(nextPathList)
        currentPathList.pop(0)
        blockedVerticesList.extend(nextBlockVertices)
        blockedVerticesList.pop(0)
        
    endingPaths = [x for x in currentPathList if x[-1]=="end"]
    
    print(currentPathList)
        
    if currentPathList0 == currentPathList:
        break

print(len(endingPaths))

#%% Part II
    
print()
