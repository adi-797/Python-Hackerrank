#!/bin/python

# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(raw_input())
if N%2 !=0:
    print "Weird"
else:
    if N>=2 and N<=5:
        print "Not Weird"
    elif N>=6 and N<=20:
        print "Weird"
    else:
        print "Not Weird"
