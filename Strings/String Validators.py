if __name__ == '__main__':
    S = raw_input()
    
print True if any(k in "0123456789" or k.lower() in "abcdefghijklmnopqrstuvwxyz" for k in S) else False
print True if any(k.lower() in "abcdefghijklmnopqrstuvwxyz" for k in S) else False
print True if any(k in "0123456789" for k in S) else False
print True if any(k in "abcdefghijklmnopqrstuvwxyz" for k in S) else False
print True if any(k in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" for k in S) else False
