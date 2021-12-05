#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 23:56:02 2021

@author: qcao
"""

import numpy as np
from skimage.draw import line

xy1 = []
xy2 = []

def isHorizontalOrVertical(x1,y1,x2,y2):
    if x1-x2 == 0:
        return True
    if y1-y2 == 0:
        return True
    return False

with open("input") as file:
    for l, ll in enumerate(file):
        ll = ll.rstrip()
        ll = ll.split("->")
        
        x1y1 = np.array(ll[0].split(",")).astype(int)
        x2y2 = np.array(ll[1].split(",")).astype(int)
        
        xy1.append(x1y1)
        xy2.append(x2y2)
        
xy1 = np.array(xy1)
xy2 = np.array(xy2)

xymax = np.max(np.array([xy1,xy2]))+1

img = np.zeros((xymax, xymax), dtype=np.uint8)

for ind in range(xy1.shape[0]):
    if isHorizontalOrVertical(xy1[ind][0], xy1[ind][1], xy2[ind][0], xy2[ind][1]):
        rr, cc = line(xy1[ind][0], xy1[ind][1], xy2[ind][0], xy2[ind][1])
        img[rr,cc] = img[rr,cc] + 1

print(np.sum(img>=2))

#%% Part II

img = np.zeros((xymax, xymax), dtype=np.uint8)

for ind in range(xy1.shape[0]):
    # if isHorizontalOrVertical(xy1[ind][0], xy1[ind][1], xy2[ind][0], xy2[ind][1]):
    rr, cc = line(xy1[ind][0], xy1[ind][1], xy2[ind][0], xy2[ind][1])
    img[rr,cc] = img[rr,cc] + 1

print(np.sum(img>=2))