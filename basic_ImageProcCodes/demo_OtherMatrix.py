import numpy as np
A = np.matrix([[-1, 2],[3, 4]])

np.matrix('1 2; 3 4') # use Matlab-style syntax 

np.arange(25).reshape((5, 5)) # create a 1-d range and reshape 

np.array(range(25)).reshape((5, 5)) # pass a Python range and reshape 

np.array([5] * 25).reshape((5, 5)) # pass a Python list and reshape 

np.empty((5, 5)) # allocate, but don't initialize 

np.ones((5, 5)) # initialize with ones 

np.zeros([5, 5])

np.ndarray((5, 5)) # use the low-level constructor
