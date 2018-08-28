# Enter your code here. Read input from STDIN. Print output to STDOUT
A = set(raw_input().split())
n = int(raw_input())
ret = True
for i in range(n):
    test = set(raw_input().split())
    if not A.issuperset(test):
        ret = False
print ret
