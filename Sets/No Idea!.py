# Enter your code here. Read input from STDIN. Print output to STDOUT
NM = raw_input()
arr = raw_input().split()
A = set(raw_input().split())
B = set(raw_input().split())
happiness = 0
for element in arr:
    if element in A:
        happiness+=1
    elif element in B:
        happiness-=1
print happiness
