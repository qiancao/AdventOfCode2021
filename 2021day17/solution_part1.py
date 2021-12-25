#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: qcao
"""

import numpy as np

# tx, ty = [20,30], [-10,-5] # test
tx, ty = [282,314], [-80,-45] # input

print("Part I, highest Y position: "+str(int(-ty[0]*(-ty[0]-1)/2)))

steps, rangeVX, rangeVY = np.arange(1000)[:,None], np.arange(1000), np.arange(-500,500)
posX = np.cumsum(np.clip(rangeVX-steps,0,None),axis=0)
posY = np.cumsum(rangeVY-steps,axis=0)
onTargetX, onTargetY = (posX >= tx[0]) & (posX <= tx[1]), (posY >= ty[0]) & (posY <= ty[1])

velocities = set()
for xind in range(onTargetX.shape[1]):
    for yind in range(onTargetY.shape[1]):
        if np.sum(onTargetX[:,xind] & onTargetY[:,yind]) > 0:
            velocities.add((rangeVX[xind],rangeVY[yind]))
print("Part II, number of unique velocities: "+str(len(velocities)))