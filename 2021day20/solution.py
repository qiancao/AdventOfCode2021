# https://www.youtube.com/watch?v=oeEvZ8WHSvY

import numpy as np

UNKNOWN = -1

sym2bitstr = lambda sym: sym.replace('.', '0').replace('#','1')
bitarray2num = lambda bit: bit.dot(2**np.arange(bit.size)[::-1])
patch2num = lambda image, xy: bitarray2num(image[xy[0]-1:xy[0]+2,xy[1]-1:xy[1]+2].flatten())
readCodec = lambda codec, num: int(sym2bitstr(codec[num]))

def setBoundary(image,value):
    image[:,0], image[:,-1], image[0,:], image[-1,:] = (value,)*4

image = []
with open("input") as file:
    lines = file.readlines()
    for ind, line in enumerate(lines):
        line = line.rstrip()
        if ind == 0:
            codec = line
        elif ind > 1:
            image.append(list(sym2bitstr(line)))
            
image = np.array(image).astype(int)

# Padding for infinity may change with each iteration
infPad = {0: readCodec(codec,bitarray2num(np.array([0]*9))),
          1: readCodec(codec,bitarray2num(np.array([1]*9)))}
infBit = 0

#%% Part I

Niters = 2

image0 = image.copy()
for ii in range(Niters): # image0 -> image1

    image0 = np.pad(image0,((2,2),)*2, mode='constant',constant_values=infBit)
    infBit = infPad[infBit] # update the current infinity bit
    
    image1 = np.zeros(image0.shape,dtype=int)
    setBoundary(image1,infBit)

    for xind in range(1,image0.shape[0]-1):
        for yind in range(1,image0.shape[1]-1):
            num = patch2num(image0,(xind,yind))
            replacement = readCodec(codec,num)
            image1[xind,yind] = replacement
            # print(f"{xind,yind} -> {num} -> {replacement}")
            
    image0 = image1
    
print(np.sum(image0))

#%% Part II

Niters = 50

image0 = image.copy()
for ii in range(Niters): # image0 -> image1

    image0 = np.pad(image0,((2,2),)*2, mode='constant',constant_values=infBit)
    infBit = infPad[infBit] # update the current infinity bit
    
    image1 = np.zeros(image0.shape,dtype=int)
    setBoundary(image1,infBit)

    for xind in range(1,image0.shape[0]-1):
        for yind in range(1,image0.shape[1]-1):
            num = patch2num(image0,(xind,yind))
            replacement = readCodec(codec,num)
            image1[xind,yind] = replacement
            
    image0 = image1
    
print(np.sum(image0))