import numpy as np
n = int(raw_input())
A = np.array([ map(int, raw_input().split()) for i in range(n) ])
B = np.array([ map(int, raw_input().split()) for i in range(n) ])
print np.dot(A, B)
