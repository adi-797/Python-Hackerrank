import numpy as np

arr = list(map(float, raw_input().split()))
k = float(raw_input())

print np.polyval(arr, k)
