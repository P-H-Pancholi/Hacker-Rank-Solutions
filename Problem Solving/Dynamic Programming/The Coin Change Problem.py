n,m = map(int,input().split())
d = list(map(int,(input().split())))


table = [[0 for _ in range(n+1)] for _ in range(m)]

for i in range(m):
    table[i][0] = 1

for i in range(m):
    for j in range(1,n+1):
        if d[i] > j:
            table[i][j] += 0
        else:
            rem = j - d[i]
            table[i][j] += table[i][rem]

        if j >= 1:
            table[i][j] += table[i-1][j]
        else:
            table[i][j] += 0

print(table[m-1][n])
