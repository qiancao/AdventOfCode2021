#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: qcao

Day 12

Compute number of paths between two vertices in an undirected graph with custom vertices.

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

graph = dict()
for vertex in vertexList:
    graph[vertex] = [edge[1] for edge in edgeList if edge[0]==vertex]

#%% Part I - Modified DFS

pathList = [] # stores all paths
currentPath = []
blockedVertexList = []

verticesToVisit = ["start"] # DFS Array
verticesToVisitStackWidth = [1] # verticesToVisit contains 1 element from the 0th traverse

while (True):
    
    currentVertex = verticesToVisit.pop()
    verticesToVisitStackWidth[-1] -= 1 # the (Nth traverse) top stack has lost 1 element
    
    currentPath.append(currentVertex)
    print("Current path: "+"->".join(currentPath))
    
    if currentVertex == currentVertex.lower() and currentVertex != "end":
        blockedVertexList.append(currentVertex)
        
    nextVertices = [vert for vert in graph[currentVertex] if vert not in blockedVertexList]
    verticesToVisit.extend(nextVertices) # this could be an empty list
    
    if verticesToVisitStackWidth[-1] == 0:
        verticesToVisitStackWidth.pop()
    if len(nextVertices) > 0: # only create new stack if there is new traversal
        verticesToVisitStackWidth.append(len(nextVertices))
    
    print("Vertices to visit: "+" | ".join(verticesToVisit))
    print("Vertices to visit, stack width: "+" | ".join([str(x) for x in verticesToVisitStackWidth]))
    
    if len(nextVertices) == 0: # Current path is completed, save to path list
        print("--> Path Found: "+"->".join(currentPath))
        pathList.append(currentPath.copy())
        currentPath.pop()
            
        
    print()
    if len(verticesToVisit) == 0: # No more vertices to visit in the graph, DFS over
        break
    
# print(pathList)
# print(len(pathList))

#%% Part II
    
print()
