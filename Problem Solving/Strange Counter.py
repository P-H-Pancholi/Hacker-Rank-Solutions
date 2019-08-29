t = int(input())
n = 3
i = n
for _ in range(t-1):
    if i == 1:
        n *= 2
        i = n+1

    i -= 1
print(i)
