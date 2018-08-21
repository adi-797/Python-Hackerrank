if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())

arr = sorted(arr, reverse=True)
temp = arr[0]
count = 0;
for i in range(len(arr)):
    if arr[i] == temp:
        count +=1;
    else:
        break

for i in range(count):
    arr.pop(0);
    
print arr[0]
