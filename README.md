# AdventOfCode

## Informative posts

On names and scoping:
- https://nedbatchelder.com/text/names1.html (Ned Batchelder - Facts and Myths about Python names and values - PyCon 2015)
- https://stackoverflow.com/questions/11462314/python-alternatives-to-global-variables
- https://stackoverflow.com/questions/11585793/are-numpy-arrays-passed-by-reference
- closures: https://stackoverflow.com/questions/2497801/closures-are-poor-mans-objects-and-vice-versa-what-does-this-mean

On algorithms and data structures:
- https://stackoverflow.com/questions/20429310/why-is-depth-first-search-claimed-to-be-space-efficient/20429574#20429574
- https://stackoverflow.com/questions/5278580/non-recursive-depth-first-search-algorithm
- https://opendsa-server.cs.vt.edu/ODSA/Books/Everything/html/CompleteTree.html

On Rotation Matrices: pre-multiplication (global) bs post-multiplication (local)
- https://www.seas.upenn.edu/~meam620/slides/kinematicsI.pdf
- http://web.cse.ohio-state.edu/~wang.3602/courses/cse5542-2013-spring/6-Transformation_II.pdf
- https://www.cs.jhu.edu/~rht/RHT%20Papers/1990/On%20Homogeneous%20Transforms,%20Quaternions,%20and%20Computational%20Efficiency.pdf
- https://math.stackexchange.com/questions/2603222/simple-rotations-in-n-dimensions-limited-to-right-angle-rotations

## Useful packages (aside from the numpy/scipy stack)

Point cloud registration:
```pip install pytransform3d
pip install pycpd (pure numpy implementation)
pip install probreg
pip install open3d-python (this is a large, feature-rich package)
```

Simple graphs and network analyis:
```
pip install networkx
```

