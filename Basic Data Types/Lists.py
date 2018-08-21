if __name__ == '__main__':
    N = int(raw_input())
    
L = []
for N in range(N):
    C = raw_input().split()
    if C[0] == 'insert': L.insert(int(C[1]), int(C[2]))
    elif C[0] == 'append': L.append(int(C[1]))
    elif C[0] == 'remove' and int(C[1]) in L: L.remove(int(C[1]))
    elif C[0] == 'print': print L
    elif C[0] == 'pop': L.pop()
    elif C[0] == 'sort': L.sort()
    elif C[0] == 'reverse': L.reverse()
    else: pass
