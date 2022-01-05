#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: qcao
"""

import numpy as np

e0 = list(np.loadtxt("test", dtype = str))
e0 = np.array([[char for char in erow] for erow in e0]).astype(int)

with open("test") as file:
    for ind, line in enumerate(file):
        ll = ll.rstrip()
        ll = ll.split(",")

        
#%% Part I

print()

