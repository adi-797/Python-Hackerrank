# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

setname = set()
N = raw_input()
names = sys.stdin.readlines();
for i in range(len(names)):
    name = list(map(str, names[i].split("\n")))
    setname.add(str(name[0]))
print len(setname)
