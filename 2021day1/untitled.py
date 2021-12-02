#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 09:56:08 2021

@author: qcao
"""

import numpy as np

def main():
    
    x = np.loadtxt("input")
    
    print(len(np.nonzero((np.diff(x)>0))[0]))
    
    y = np.convolve(x,[1,1,1],'valid')
    
    print(len(np.nonzero((np.diff(y)>0))[0]))

if __name__ == "__main__":
    
    main()