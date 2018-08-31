import numpy as np
arr = list(map(int, raw_input().split()))
arr = np.array(arr)
print np.reshape(arr, (3,3))
