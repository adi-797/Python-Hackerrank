# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(raw_input())
arr = list(raw_input().split())
arr = sorted(arr)
i = 0
num = 10
while i<len(arr):
    if i+N>len(arr):
        num = arr[len(arr)-1]
    else:
        if arr[i] != arr[i+N-1]:
            num = arr[i]
            break
    i+=N
print num
