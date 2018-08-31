import numpy
a=map(int,raw_input().split())
print str(numpy.eye(a[0],a[1],k=0)).replace('1',' 1').replace('0',' 0')
