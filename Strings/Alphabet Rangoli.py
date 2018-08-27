def print_rangoli(size):
    # your code goes here
    out = []
    for i in range(n*2-1):
        n1 = abs(i-n+1)
        out.append("{}{}{}{}{}".format("--"*n1, "-".join( [(chr(96+n-x)) for x in range(abs(n1-n))] ), "-", "-".join([(chr(96+n-x)) for x in range(abs(n1-n))][::-1][1:]), "--"*n1 ))
    for i in out:
        print i[:n*4-3]
