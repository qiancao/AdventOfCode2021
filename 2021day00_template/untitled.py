#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: qcao
"""

import numpy as np

e0 = list(np.loadtxt("input", dtype = str))
e0 = np.array([[char for char in erow] for erow in e0]).astype(int)

with open("input") as file:
    for l, ll in enumerate(file):
        ll = ll.rstrip()
        ll = ll.split("|")

        
#%% Part I

print()

#%% Part II

print()
