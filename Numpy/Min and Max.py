import numpy as np
n, m = map(int, raw_input().split())
arr = np.array([ map(int, raw_input().split()) for i in range(n) ])
arr = np.min(arr, axis=1)
print np.max(arr)
