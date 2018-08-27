def minion_game(s):
    vowels = ["A","E","I","O","U"]
    countS, countK = 0,0;
    length = len(s)
    for i in range(length):
        #STUART
        if s[i] not in vowels:
            countS+=length-i
        #KEVIN
        else:
            countK+=length-i
        
    if countK>countS:
        print "Kevin " + str(countK)
    elif (countK==countS):
        print "Draw"
    else:
        print "Stuart " + str(countS)
