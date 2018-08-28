n = input()
s = set(map(int, raw_input().split()))
c = raw_input()
for i in range(int(c)):
    command = raw_input().split(" ")
    if command[0] == "pop":
        s.pop()
    elif command[0] == "remove":
        s.remove(int(command[1]))
    else:
        s.discard(int(command[1]))

print sum(s)
