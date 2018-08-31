import numpy

N, M, P = map(int, raw_input().split())
array_1 = numpy.array([ map(int, raw_input().split()) for i in range(N) ])
array_2 = numpy.array([ map(int, raw_input().split()) for i in range(M) ])

print numpy.concatenate((array_1, array_2), axis = 0)
