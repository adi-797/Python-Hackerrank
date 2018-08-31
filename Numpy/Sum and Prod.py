import numpy as np
n, m = map(int, raw_input().split())
arr = np.array([ map(int, raw_input().split()) for i in range(m) ])
arr = np.sum(arr, axis=0)
print np.prod(arr)
