n = int(input())
p = int(input())

if n%2 != 0:
    if p == 1 or p == n or p == n-1:
        print(0)
    elif p < (n+1)/2:
        turn = int(p/2)
        print(turn)
    else:
        turn = int((n-p)/2)
        print(turn)
else:
    if p == 1 or p == n:
        print(0)
    elif p <= n/2:
        turn = int(p/2)
        print(turn)
    else:
        turn = int((n-p)/2)+1
        print(turn)

    
