"""
Mutate vs Rebind
"""

from dis import dis

def rebind():
    a = 2312
    b = a
    b += 1
    print(a)
    print(b)

def mutate():
    a = [2312]
    b = a
    b[0] += 1
    print(a)
    print(b)
    
"""
For numpy arrays, -= is a difference in rebind vs mutate
"""
# array is not updated in enclosing scope
def npArrayRebind(arr):
   arr = arr - 3

# array is updated in enclosing scope
def npArrayMutate(arr):
   arr -= 3

