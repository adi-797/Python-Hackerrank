# Enter your code here. Read input from STDIN. Print output to STDOUT
N1 = raw_input()
english = set(raw_input().split())
N2 = raw_input()
french = set(raw_input().split())
english = english.difference(french)
print len(english)
