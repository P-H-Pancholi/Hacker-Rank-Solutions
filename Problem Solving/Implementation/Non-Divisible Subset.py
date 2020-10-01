n,k = map(int, input().split())
arr = list(map(int,input().split()))
res = 0

remainder = [0 for _ in range(k)]

for num in arr:
    remainder[num % k] += 1


if k % 2 == 0:
    remainder[k//2] = min(remainder[k//2],1)

res = min(remainder[0],1)

for i in range(1,k//2 + 1):
    res += max(remainder[i], remainder[k - i])

print(res)
