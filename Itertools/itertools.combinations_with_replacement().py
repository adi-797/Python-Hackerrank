# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools

input = list(raw_input().split())
s = input[0]
n = int(input[1])

ret = sorted(list(itertools.combinations_with_replacement(sorted(s),n)))
string = ""
for i in range(len(ret)):
    for j in range(n):
        string+=ret[i][j]
    print string
    string = ""
