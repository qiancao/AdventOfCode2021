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
with open("input") as file:
    for l, ll in enumerate(file):
        ll = ll.rstrip()
        ll = ll.split("-")
        
        # Don't go back to start nor bounce back from end
        if ll[1] != "start" and ll[0] != "end":
           edgeList.append(ll)
        
        # Don't go back to start nor bounce back from end
        if ll[0] != "start" and ll[1] != "end":
            edgeList.append(list(reversed(ll)))
        
        if ll[0] not in vertexList:
            vertexList.append(ll[0])
        if ll[1] not in vertexList:
            vertexList.append(ll[1])
    

adjacency = dict()
vertexVisitOnce = set() # set of vertices that can only be visited at most once on each path
for vertex in vertexList:
    adjacency[vertex] = [edge[1] for edge in edgeList if edge[0]==vertex]
    if vertex == vertex.lower() and vertex != "start" and vertex != "end":
        vertexVisitOnce.add(vertex)
            
#%% Part I Modified Depth-first Search (DFS)

Npaths = 0
stack = ["start"]
stackBacktrackPtr = [0] # position in the path to backtrack to, after top stack is popped
path = []

while (True):
# for step in range(100):

    # BacktrackPtr pops with stack
    currentVertex = stack.pop()
    stackBacktrackPtr.pop()

    # Add current vertex to path
    path.append(currentVertex)
    
    # Compute blocked vertices based on current path
    blockedVertices = vertexVisitOnce.intersection(set(path))
    
    # Traverse unblocked neighbors
    traversibleVertices = [vert for vert in adjacency[currentVertex] if vert not in blockedVertices]
    
    # BacktrackPtr (to path list) grows with stack
    stack.extend(traversibleVertices) # nothing happens if empty
    stackBacktrackPtr.extend(np.repeat(len(path)-1, len(traversibleVertices)))
    

    
    # State of stack and path
    # print("Step: "+str(step))
    print("stack: "+" | ".join(stack))
    print("backt: "+" | ".join([str(x) for x in stackBacktrackPtr]))
    print(" -> ".join(path) if len(path)>0 else "path is empty")
    
    if len(traversibleVertices) == 0:
        if currentVertex == "end":
            Npaths += 1
            print("Complete path found: "+" -> ".join(path))
        if len(stack) == 0: # what a weird place to break the loop!! the problem is stackBacktrackPtr[-1] which can't be empty
            break
        pathBacktrackInd = stackBacktrackPtr[-1]+1 # End of path requires backtracking of path
        path = path[:pathBacktrackInd]
        
    print()
    # if len(stack) == 0: # DFS completed
    #     break

print("Total Unique Valid Paths: "+str(Npaths))

#%% Part II
    
print()
