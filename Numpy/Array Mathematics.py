import numpy

N, M= map(int, raw_input().split())

A = numpy.array([map(int, raw_input().split()) for i in range(N)])
B = numpy.array([map(int, raw_input().split()) for i in range(N)])

print A+B
print A-B
print A*B
print A / B
print A % B
print A**B
