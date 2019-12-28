n = int(input())
unsorted = []
for _ in range(n):
    unsorted.append(input())

sorted = sorted(unsorted, key = lambda x:(len(x),x))
for i in range(n):
    print(sorted[i])
