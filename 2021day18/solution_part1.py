import numpy as np

def makeSnail(number):
    return type("Snail",(object,),{"number" : number,"_ptr" : [], # ptr is a list of [0,1,0,...]
                                   "_stack" : [[1],[0]], "_exploded" : False,"_split" : False})

def addSnail(snail0, snail1):
    return reduceSnail(makeSnail([snail0.number, snail1.number]))

def reduceSnail(snail):
    while True:
        if explodeSnail(snail): # "...repeatedly do the first action in this list that applies to the snailfish number"
            continue
        if splitSnail(snail):
            continue
        return snail
    
def _reset(snail):
    snail._ptr, snail._stack, snail._exploded, snail._split = [], [[1],[0]], False, False
    
def _get(snail): # get node referenced by ptr (a full traversal is needed at each call, but it's okay, capped at 4 lookups)
    node = snail.number
    for p in snail._ptr:
        node = node[p]
    return node
    
def _next(snail): # move ptr to next node in a left-first, depth-first search, _stack contains future nodes to visit
    if len(snail._stack) == 0: # no more elements to traverse
        snail._ptr = None
    else:
        snail._ptr = (snail._stack.pop()) # update ptr to next node
        node = _get(snail)
        if isinstance(node, list): # otherwise if int, no child nodes to append
            snail._stack.extend([snail._ptr+[1], snail._ptr+[0]])
    return snail._ptr

def _leaf(snail, direction): # 0 for left-leaf, 1 for right-leaf
    node, ptr = _get(snail), snail._ptr.copy()
    while isinstance(node, list):
        ptr.append(direction)
        node = node[direction]
    return ptr

def _leafNeighbor(snail, direction):
    ptr0 = snail._ptr.copy() # guaranteed: len(ptr) >= 4
    ptr = None # returns None of no neighboring leaves are found
    while len(snail._ptr) > 0:
        parent = snail._ptr.pop()
        if parent != direction:
            snail._ptr.append(direction) # step in search direction
            ptr = _leaf(snail, 1-direction) # reverse direction and traverse to leaf
            break
    snail._ptr = ptr0
    return ptr

def _replace(snail, replacement): # replace node referenced by ptr
    if snail._ptr is None: # if ptr is none, replace nothing
        return
    lastIndex = snail._ptr.pop()
    _get(snail)[lastIndex] = replacement
    snail._ptr.append(lastIndex)

def explodeSnail(snail):
    _reset(snail)
    while (not snail._exploded) and (_next(snail) != None):
        node = _get(snail)
        if isinstance(node, list) and len(snail._ptr) >= 4:
            for direction in range(2):
                ptr0 = snail._ptr.copy()
                snail._ptr = _leafNeighbor(snail,direction)
                if snail._ptr is not None:
                    leaf = _get(snail)
                    _replace(snail, leaf+node[direction])
                snail._ptr = ptr0
            _replace(snail, 0)
            snail._exploded = True
    return snail._exploded # True if the number has exploded

def splitSnail(snail):
    _reset(snail)
    while (not snail._split) and (_next(snail) != None):
        node = _get(snail)
        if isinstance(node, int) and node >= 10:
            _replace(snail, [int(np.floor(node/2)), int(np.ceil(node/2))])
            snail._split = True
    return snail._split # True if the number has split

def magnitude(number):
    if isinstance(number[0],int):
        left = number[0]
    else:
        left = magnitude(number[0])
    if isinstance(number[1],int):
        right = number[1]
    else:
        right = magnitude(number[1])
    return 3*left + 2*right

if __name__ == "__main__":
    
    numbers = []
    with open("input") as file:
        for l, ll in enumerate(file):
            numbers.append(eval(ll.rstrip())) # just use python parser
    
    snail = makeSnail(numbers[0])
    for ind in range(1,len(numbers)):
        snail = addSnail(snail,makeSnail(numbers[ind]))
    
    print(magnitude(snail.number))
    
    