# Enter your code here. Read input from STDIN. Print output to STDOUT
s = list(raw_input())
s.append(-1)
ret = []
count = 1

for i in range(len(s)-1):
    if s[i] == s[i+1]:
        count+=1
        continue
    ret.append((count, int(s[i])))
    count = 1
    
for element in ret:
    print element,
