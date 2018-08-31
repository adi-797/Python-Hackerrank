import numpy as np
n = int(raw_input())
arr = np.array([ map(float, raw_input().split()) for i in range(n) ])
print np.linalg.det(arr)
