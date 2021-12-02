#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 00:21:00 2021

@author: qcao
"""

import numpy as np

def main():
    
    #%% Part I
    
    x, y = 0, 0
    
    with open("input") as file:
        for line in file:
            line = line.rstrip()
            line = line.split(" ")
            
            if line[0] == "forward":
                x = x + int(line[1])
            elif line[0] == "down":
                y = y + int(line[1])
            elif line[0] == "up":
                y = y - int(line[1])
                
    print(x)
    print(y)
    print(x*y)
    
    #%% Part II
    
    x, y, a = 0, 0, 0
    
    with open("input") as file:
        for line in file:
            line = line.rstrip()
            line = line.split(" ")
            
            if line[0] == "forward":
                x = x + int(line[1])
                y = y + a * int(line[1])
            elif line[0] == "down":
                a = a + int(line[1])
            elif line[0] == "up":
                a = a - int(line[1])
                
    print(x)
    print(y)
    print(x*y)

if __name__ == "__main__":
    
    main()
