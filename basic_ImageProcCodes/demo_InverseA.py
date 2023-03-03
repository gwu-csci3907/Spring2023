import numpy as np

A = np.matrix([[-1, 2],[3, 4]])

detA = np.linalg.det(A)
print(detA)

invA = np.linalg.inv(A)
print(invA)