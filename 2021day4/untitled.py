#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 23:48:45 2021

@author: qcao
"""

import numpy as np

draw = str(np.loadtxt("input", max_rows=1, dtype=str)).split(",")
draw = np.array(draw).astype(int)

boardList = []
with open("input") as file:
    for l, line in enumerate(file):
        line = line.rstrip()
        line = line.split()
        
        print(line)

        if l > 0: # beyond the first row

            if len(line) == 0: # new board
                lcount = 0
                board = np.zeros((5,5),dtype=int)
            else:
                board[lcount,:] = np.array(line).astype(int)
                lcount = lcount + 1
                
                if lcount == 4:
                    boardList.append(board)
                    
board = np.array(boardList)
hits = np.zeros(board.shape,dtype=bool)

for d, drawnum in enumerate(draw):
    
    hits = hits | (board==drawnum)
    
    hits1 = np.sum(np.sum(hits,axis=1) == 5, axis=1)>0
    hits2 = np.sum(np.sum(hits,axis=2) == 5, axis=1)>0
    
    if np.any(hits1):
        ind = np.nonzero(hits1)
        print(ind)
        print(hits[ind,:,:])
        callednum = drawnum
        break
    if np.any(hits2):
        ind = np.nonzero(hits2)
        print(ind)
        print(hits[ind,:,:])
        callednum = drawnum
        break
        
print(np.sum(board[ind,:,:]*(1-hits[ind,:,:])) * callednum)

#%% Part II

board = np.array(boardList)
hits = np.zeros(board.shape,dtype=bool)
winningboards = np.zeros(board.shape[0],dtype=bool)

for d, drawnum in enumerate(draw):
    
    # lasthit = hits
    # print(lasthit[lastboardind,:,:])
    
    hits = hits | (board==drawnum)
    
    hits1 = np.sum(np.sum(hits,axis=1) == 5, axis=1)>0
    hits2 = np.sum(np.sum(hits,axis=2) == 5, axis=1)>0
    
    if np.any(hits1):
        ind = np.nonzero(hits1)
        winningboards[ind] = True
        callednum = drawnum
    if np.any(hits2):
        ind = np.nonzero(hits2)
        winningboards[ind] = True
        callednum = drawnum

    if np.sum(winningboards) == (len(winningboards) -1):
        lastboardind = np.nonzero(1-winningboards)[0][0]
        
    if np.sum(winningboards) == (len(winningboards)):
        callednum = drawnum
        break
    
print(np.sum(board[lastboardind,:,:]*(1-hits[lastboardind,:,:])) * callednum)