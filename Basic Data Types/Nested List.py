list = [];

for _ in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())
    list.append([score, name]);

list = sorted(list);
temp = list[0][0]

count = 0;
for i in range(len(list)):
    if list[i][0] == temp:
        count +=1;
    else:
        break

for i in range(count):
    list.pop(0);

second = list[0][0]

for i in range(len(list)):
    if second == list[i][0]:
        print list[i][1]
