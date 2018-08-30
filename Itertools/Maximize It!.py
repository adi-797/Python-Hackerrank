print "Hello, World!"
# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools
k,m=map(int,raw_input().split())
l=[]
while k>0:
    k-=1
    x=list(map(int,raw_input().split()))
    l.append(x[1:])

l = list(itertools.product(*l))

maxm=0
for i in range(len(l)):
    summ=0
    for j in range(len(l[i])):
        summ=summ+(l[i][j]**2)
    ans=summ%m
    if ans>maxm:
        maxm=ans
print maxm
