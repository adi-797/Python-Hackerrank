# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(raw_input())
for i in range(N):
    N1 = raw_input()
    A = set(raw_input().split())
    N2 = raw_input()
    B = set(raw_input().split())
    print A<B
