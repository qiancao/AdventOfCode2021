#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: qcao
"""

import numpy as np
from scipy.ndimage.measurements import label

h = list(np.loadtxt("input", dtype = str))
h = np.array([[char for char in hrow] for hrow in h]).astype(int)
        
#%% Part I

isLowest = lambda f,x,y: (f[x-1,y] > f[x,y]) and (f[x+1,y] > f[x,y]) \
    and (f[x,y+1] > f[x,y]) and (f[x,y-1] > f[x,y])

hp = np.pad(h,(1,1),'constant',constant_values = (9,9))
hl = np.zeros(h.shape,dtype=bool)
for i in range(1,hp.shape[0]-1):
    for j in range(1,hp.shape[1]-1):
        hl[i-1,j-1] = isLowest(hp,i,j)
        
print(np.sum(h[hl]+1))

#%% Part II

while (True):
    
    total_size = np.sum(hl)

    xs,ys = np.nonzero(hl)
    
    for x, y in zip(xs, ys):
        if  (x+1) < hl.shape[0] and h[x+1,y] > h[x,y] and h[x+1,y] < 9:
            hl[x+1,y] = True
        if (x-1) >= 0 and h[x-1,y] > h[x,y] and h[x-1,y] < 9:
            hl[x-1,y] = True
        if (y+1) < hl.shape[1] and h[x,y+1] > h[x,y] and h[x,y+1] < 9 :
            hl[x,y+1] = True
        if (y-1) >= 0 and h[x,y-1] > h[x,y] and h[x,y-1] < 9:
            hl[x,y-1] = True
        
    total_size_new = np.sum(hl)
    
    if total_size == total_size_new:
        break

# TODO: write connected-components, oh well
cc, ncomponents = label(hl)

lencc = []
for ii in range(np.max(cc)):
    lencc.append(np.sum(cc == ii+1))
lencc.sort()
lencc = lencc[::-1]

print(lencc[0]*lencc[1]*lencc[2])