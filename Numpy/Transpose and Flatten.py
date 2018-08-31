import numpy as np
N, M = raw_input().split()
arr = ""
for i in range(int(N)):
    arr += raw_input() + " "
arr = list(map(int, arr.split()))
arr = np.array(arr)
arr = np.reshape(arr, (int(N),int(M)))
print np.transpose(arr)
print arr.flatten()


