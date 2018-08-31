import numpy as np
A = np.array(map(int, raw_input().split()))
B = np.array(map(int, raw_input().split()))
print np.inner(A,B)
print np.outer(A,B)
