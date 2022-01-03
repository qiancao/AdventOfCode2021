
import itertools
from collections import defaultdict
import numpy as np
from scipy.spatial import distance_matrix
import networkx as nx

PLOT_BEACONS = True
if PLOT_BEACONS:
    import matplotlib.pyplot as plt
    plt.close('all')
    fig = plt.figure()
    ax = plt.axes(projection='3d')

NTHRESH = 12 # Number of matching pair-wise distances needed to identify as corresponding point

array2set = lambda array: set(map(tuple, array))

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

beaconPair = list(itertools.combinations(range(len(beacons)),2))
transforms = dict()
G = nx.DiGraph() # graph of known transformations between scanners
G.add_nodes_from(list(range(len(beacons))))
for ind, pair in enumerate(beaconPair):
    p0, p1, points = sharedPoints(*[beacons[x] for x in pair])
    # print(len(points))
    if p0 is not None:
        R, t, norm = getTransform(p0,p1)
        assert norm == 0, "getTransform failed to produce correct transform"
        transforms[pair] = (R, t, False)
        transforms[pair[::-1]] = (R, t, True)
        G.add_edge(*pair)
        G.add_edge(*pair[::-1])

allpoints = set(array2set(beacons[0]))
if PLOT_BEACONS: ax.scatter(beacons[0][:,0],beacons[0][:,1],beacons[0][:,2], s=10**2, marker="o")
for ind, beacon in enumerate(beacons[1:], start=1): # 0 is the reference frame
    path = nx.algorithms.shortest_path(G, source=ind, target=0) # transform from n-th beacon to 0th beacon
    for step in range(len(path)-1):
        transform = transforms[(path[step],path[step+1])]
        beacon = applyTransform(beacon, *transform) # okay to mix normal args and unpacked args, interesting
    if PLOT_BEACONS:
        ax.scatter(beacon[:,0],beacon[:,1],beacon[:,2], s=10**2, marker="o")
        # plt.pause(1)
    allpoints = allpoints.union(array2set(beacon))
  
if PLOT_BEACONS: 
    allbeacons = np.array(list(allpoints))
    
    scannerPositions = np.zeros((len(beacons),3))
    for ind, beacon in enumerate(beacons[1:], start=1): 
        path = nx.algorithms.shortest_path(G, source=ind, target=0)
        position = np.array([[0,0,0]]) # origin at zero
        for step in range(len(path)-1):
            transform = transforms[(path[step],path[step+1])]
            position = applyTransform(position, *transform)
        scannerPositions[ind,:] = position
    ax.scatter(scannerPositions[:,0],scannerPositions[:,1],scannerPositions[:,2], c='k', s=30**2,marker="+")
    
    scanners = []
    for ind, beacon in enumerate(beacons):
        indx = (allbeacons[:,0] >= scannerPositions[ind,0] - 1000) & (allbeacons[:,0] <= scannerPositions[ind,0] + 1000)
        indy = (allbeacons[:,1] >= scannerPositions[ind,1] - 1000) & (allbeacons[:,1] <= scannerPositions[ind,1] + 1000)
        indz = (allbeacons[:,2] >= scannerPositions[ind,2] - 1000) & (allbeacons[:,2] <= scannerPositions[ind,2] + 1000)
        scanners.append(allbeacons[indx & indy & indz,:])
        
    fig3 = plt.figure()
    ax3 = plt.axes(projection='3d')
    for ind, beacon in enumerate(scanners):
        ax3.scatter(beacon[:,0],beacon[:,1],beacon[:,2], s=10**2, marker="v")
    
print(len(allpoints))

fig2 = plt.figure()
nx.draw(G, with_labels=True, node_color=['y']*len(beacons))

fig3 = plt.figure()
plt.plot([len(x) for x in scanners])
plt.plot([len(x) for x in beacons])


# pointsList = list(allpoints)
# pointsList.sort()
# print(pointsList)