def swap_case(s):
    ret = ""
    for i in range(len(s)):
        if s[i].isalpha() is True: 
            if s[i].isupper() is True:
                ret+=s[i].lower()
            elif s[i].islower() is True:
                ret+=s[i].upper()
        else:
            ret+=s[i]
    return ret
