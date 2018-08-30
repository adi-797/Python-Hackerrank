# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools

N = int(raw_input())
s = list(raw_input().split())
K = int(raw_input())

ret = list(itertools.combinations(s,K))
count = 0
for i in range(len(ret)):
    for j in range(K):
        print ret[i][j]
        if ret[i][j] == "a":
            count+=1
            break
ret = count/len(ret)
print round(ret, 3)
