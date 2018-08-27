def merge_the_tools(string, k):
    # your code goes here
    from collections import OrderedDict
    i = 0
    while i<len(string):
        s = string[i:i+k]
        print "".join(OrderedDict.fromkeys(s))
        i+=k
        s = ""
