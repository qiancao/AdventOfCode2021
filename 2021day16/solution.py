#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: qcao
"""

import numpy as np

def readBits(N,data,asString=False): # read N bits from data and advance ptr
    bits = data.bits[data.ptr:data.ptr+N]
    if not asString:
        bits = int(bits,2)
    data.ptr += N
    return bits

def readLiteral(data):
    literal = []
    continueReading = True
    while bool(continueReading):
        continueReading = readBits(1,data)
        literalValue = readBits(4,data,True)
        literal.append(literalValue)
    return int("".join(literal),2)
    
def readSubpacketLength(data):
    subpacketLength = readBits(15, data)
    ptr0 = data.ptr
    packets = []
    while data.ptr < (ptr0 + subpacketLength):
        packets.append(readPacket(data))
    return packets
    
def readSubpacketNumber(data):
    numberOfSubpackets = readBits(11, data)
    packets = []
    for ind in range(numberOfSubpackets):
        packets.append(readPacket(data))
    return packets

def readPacket(data):
    version, typeID = readBits(3,data), readBits(3,data)
    data.versionSum += version
    if typeID == 4:
        packet = readLiteral(data)
    else:
        lengthTypeID = readBits(1, data)
        if lengthTypeID == 0:
            packet = readSubpacketLength(data)
        else:
            packet = readSubpacketNumber(data)
    return (version, typeID, packet)

def evalPacket(packet):
    if packet[1] == 4: # already a literal packet
        return packet
    else:
        literals = []
        for ind, subpacket in enumerate(packet[2]):
            if subpacket[1] != 4:
                subpacket = evalPacket(subpacket)
            literals.append(subpacket[2])
        literals = np.array(literals)
        if packet[1] == 0:
            return (packet[0], 4, np.sum(literals))
        elif packet[1] == 1:
            return (packet[0], 4, np.prod(literals))
        elif packet[1] == 2:
            return (packet[0], 4, np.min(literals))
        elif packet[1] == 3:
            return (packet[0], 4, np.max(literals))
        elif packet[1] == 5:
            return (packet[0], 4, int(literals[0]>literals[1]))
        elif packet[1] == 6:
            return (packet[0], 4, int(literals[0]<literals[1]))
        elif packet[1] == 7:
            return (packet[0], 4, int(literals[0]==literals[1]))
        
if __name__ == "__main__":
    
    transmission = str(np.loadtxt("input", dtype = str))
    transmissionArray = np.array([char for char in transmission])
    
    hex2bin = dict()
    with open("Hexidecimal2Binary.txt") as file:
        for l, ll in enumerate(file):
            ll = ll.rstrip()
            ll = ll.split(" = ")
            hex2bin[ll[0]] = ll[1]
        
    transmissionBinaryArray = np.vectorize(hex2bin.get)(transmissionArray)
    transmissionBinary = "".join(transmissionBinaryArray)
    
    data = type("BitString", (object,), {"bits": transmissionBinary, "ptr": 0, \
                                         "versionSum": 0})
    packet = readPacket(data)
    literal = evalPacket(packet)
    
    print(data.versionSum)
    print(literal[2])