from itertools import permutations

def findPremutation(n,k):
    solution = []
    s = set(range(1,n+1))

    for pos in range(1, n+1):
        if pos-k in s:
            solution.append(pos-k)
            s.remove(pos-k)
        elif pos+k in s:
            solution.append(pos+k)
            s.remove(pos+k)
        else:
            return [-1]

    return solution

t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    result = findPremutation(n,k)
    print(" ".join(map(str,result)))
