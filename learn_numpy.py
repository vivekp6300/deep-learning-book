import numpy as np
from pprint import pprint

A = np.array([[1, 2], [3, 4], [3, 4]])
B = np.array([[5, 6,7], [7, 8, 9]])
print(A.shape)
print(B.shape)

C = np.matmul(A, B)
pprint(C)
D = np.matmul(B, A)
pprint(D)

pprint(np.matmul(B, B.T))