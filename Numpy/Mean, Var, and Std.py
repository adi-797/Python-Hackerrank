import numpy as np
np.set_printoptions(sign=' ')
n, m = map(int, raw_input().split())
arr = np.array([ map(int, raw_input().split()) for i in range(m) ])
print np.mean(arr, axis=1)
print np.var(arr, axis=0)
print np.std(arr)



