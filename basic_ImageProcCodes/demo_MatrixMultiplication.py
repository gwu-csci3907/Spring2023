import numpy as np

A = np.matrix([[-1, 2],[3 , 4]])
# A = np.matrix('-1 2; 3 4')
B = np.matrix([[4], [-2]])
# B = np.matrix('4; -2')

C = np.dot(A, B)
C = np.matmul(A, B)
C = np.multiply(A, B)
print(C)

# np.dot(array a, array b): returns the scalar or dot product of two arrays
# np.matmul(array a, array b): returns the matrix product of two arrays
# np.multiply(array a, array b): returns the element-wise matrix multiplication of two arrays