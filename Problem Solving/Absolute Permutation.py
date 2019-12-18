from itertools import permutations

def findPremutation(n,k):
    check = False
    l = [i for i in range(1,n+1)]
    list_of_permutations = list(permutations(l))
    for permutation in list_of_permutations:
        l = list(permutation)
        #print("Checking for permutation",l,sep= "---")
        for i in range(1,n+1):
            #print("Checking for i,l[i-1] and l[i-1] - i", i, l[i-1] , l[i-1] - i, sep= "---")
            if abs(l[i-1] - i) == k:
                check =True
                if i == n:
                    return list(permutation)
            else:
                check = False
                break

    return [-1]

t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    result = findPremutation(n,k)
    print(" ".join(map(str,result)))
