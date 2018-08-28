# Enter your code here. Read input from STDIN. Print output to STDOUT
N = raw_input()
A = set(raw_input().split())
nsets = raw_input()

for i in range(int(nsets)):
    name = raw_input().split(" ")
    newset = set(raw_input().split())
    if name[0] == "intersection_update":
        A.intersection_update(newset)
    elif name[0] == "update":
        A.update(newset)
    elif name[0] == "symmetric_difference_update" :
        A.symmetric_difference_update(newset)
    else:
        A.difference_update(newset)
sum = 0
for element in A:
    sum += int(element)
print sum
    
