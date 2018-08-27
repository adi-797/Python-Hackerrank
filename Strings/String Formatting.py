def print_formatted(number):
    b = str(bin(number))[2:]
    sbuf = len(b)
    buf = sbuf + 1
    
    for x in range(1, number+1):
        o = str(oct(x))[1:]
        h = str(hex(x)).upper()[2:]
        b = str(bin(x))[2:]
        #p = str()
        x = str(x)
        while len(x) != sbuf:
            x = " " + x
        while len(o) != buf:
            o = " " + o
        while len(h) != buf:
            h = " "+ h
        while len(b) != buf:
            b = " "+ b
        print x+o+h+b
