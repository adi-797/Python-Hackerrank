# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools

A = map(int,raw_input().strip().split())
B = map(int,raw_input().strip().split())

X = itertools.product(A,B)
for element in X:
    print (element),
