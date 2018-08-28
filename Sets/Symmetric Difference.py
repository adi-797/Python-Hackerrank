import sys, math

N = (sys.stdin.readlines());
A = list(map(int, N[1].split()))
B = list(map(int, N[3].split()))
A = set(A)
B = set(B)

list1 = list(A.difference(B))
list2 = list(B.difference(A))
for element in list1:
    list2.append(element)
    
list2 = sorted(list2)
for element in list2:
    print element
