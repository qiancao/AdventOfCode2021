# Welp, lesson learned: np.array.astype doesn't do rounding! Invoke array.round first
import itertools
import numpy as np
from scipy.spatial import distance_matrix

NTHRESH = 12 # Number of matching pair-wise distances needed to identify as corresponding point

array2set = lambda array: set(map(tuple, array))
set2array = lambda s: np.array(list(s))

permuteXYZ = list(itertools.permutations([0,1,2])) # Rotation: 2**(n-1) +/-, n! positions
signXY = list(itertools.product(*[(-1,1)]*2)) # Sign of Z determined by signs of X and Y (because detR=1)
rotations = list(itertools.product(*[permuteXYZ,signXY])) # 24 configurations

def sharedPoints(xyz0, xyz1): # search for corresponding points and their indices
    p0, p1, points = None, None, []
    dists = [distance_matrix(x,x) for x in [xyz0,xyz1]]
    for d0, d1 in list(itertools.product(*[range(len(dists[x])) for x in range(2)])):
        if len(np.intersect1d(dists[0][d0], dists[1][d1])) >= NTHRESH: # d0, d1 are corresponding points
            points.append((d0,d1))
            
    if len(points) > 0:
        inds = list(zip(*points)) # returns shared points in addition to list of indices
        p0, p1 = xyz0[inds[0],:], xyz1[inds[1],:] # points
    return p0, p1, points

def getTransform(p0,p1): # transform p0 to p1: p1 = R*p0+t
    for r, rotation in enumerate(rotations):
        R = makeRotationMatrix(*rotation)
        p0r = applyRotationMatrix(R, p0).astype(float)
        t = np.mean(p1,axis=0) - np.mean(p0r,axis=0)
        p0r += t
        norm = np.sum(np.linalg.norm(p1-p0r,axis=1)) # rounds infinitesmal to zero
        if norm == 0:
            break
    return R.round().astype(int), t.round().astype(int), norm # Note: astype doesn't do rounding!

def applyTransform(p, R, t, inverse=False): # R*p + t
    return applyRotationMatrix(R.T, p-t) if inverse else applyRotationMatrix(R, p) + t

def makeRotationMatrix(pxyz, sign): # Compute SO3, pxyz is permuteXYZ, sign is signXY
    R = np.zeros((3,3),dtype=int)
    R[tuple(range(3)),pxyz] = (*sign,1)
    R[2,pxyz[2]] = R[2,pxyz[2]] * int(np.linalg.det(R)) # flip sign of z axis if det(R)=-1
    return R

def applyRotationMatrix(R, xyz):
    return np.matmul(R[None,:],xyz[:,:,None])[:,:,0] # Pad until the last two dimensions match to enable broadcasting

#%% Part I

beacons = []
with open("input") as file:
    lines = file.readlines()
    for ind, line in enumerate(lines):
        line = line.rstrip()
        
        if "--- scanner" in line:
            detections = []
        elif line == "":
            beacons.append(np.array(detections))
        else:
            xyz = line.split(",")
            detections.append([int(n) for n in xyz])
            if ind==len(lines)-1: # last line
                beacons.append(np.array(detections))

NotRegistered, transforms = set(range(1,len(beacons))), [None]*len(beacons)
allpoints = set(array2set(beacons[0]))
while len(NotRegistered) > 0:
    Registered = set()
    for ind in NotRegistered: # register to beacons[0]
        beacon = beacons[ind].copy()
        p0, p1, points = sharedPoints(set2array(allpoints),beacon)
        if p0 is not None:
            R, t, norm = getTransform(p0,p1) # transform from p0 to p1
            assert norm == 0, f"getTransform failed to produce correct transform, norm = {norm}"
            beaconTransformed = applyTransform(beacon, R, t, inverse=True)
            allpoints = allpoints.union(array2set(beaconTransformed))
            Registered.add(ind)
            transforms[ind] = (R,t)
            
    NotRegistered = NotRegistered - Registered
            
print(len(allpoints))

#%% Part II

scannerPositions = np.zeros((len(beacons),3))
for ind in range(1,len(beacons)): 
    scannerPositions[ind,:] = applyTransform(np.array([[0,0,0]]),*transforms[ind],inverse=True)
dists = distance_matrix(scannerPositions,scannerPositions, p=1)
print(np.max(dists))

manhattans = [] # sanity check
for ind0, ind1 in list(itertools.combinations(range(len(beacons)), 2)): 
    manhattans.append(np.sum(np.abs(scannerPositions[ind1,:]-scannerPositions[ind0,:])))
print(np.max(manhattans))