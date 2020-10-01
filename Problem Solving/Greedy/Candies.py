n = int(input())
arr = []
for _ in range(n):
    inp = int(input())
    arr.append(inp)


#print(arr)

countl = [1 for _ in range(len(arr))]
countr = [1 for _ in range(len(arr))]

#print(count)

for i in range(1,n):
    if arr[i] > arr[i-1]:
        countl[i] = countl[i-1] + 1

for i in range(n-2,-1,-1):
    if arr[i] > arr[i+1]:
        countr[i] = countr[i+1] + 1

n_candies = 0

for i in range(n):
    n_candies += max(countl[i],countr[i])

print(n_candies)
