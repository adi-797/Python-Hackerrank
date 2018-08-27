# Complete the solve function below.
def solve(s):
    ret = s[0].upper()
    i =1
    while i<len(s):
        ret+=s[i]
        if s[i] == " ":
            if s[i+1] != " ":
                ret+=s[i+1].upper()
                i+=1
        i+=1
    return ret
