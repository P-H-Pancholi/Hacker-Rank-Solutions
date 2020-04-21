def get_diff(arr):
    diff = 0
    for i in range(len(arr)-1):
        diff += abs(arr[i] - arr[i+1])

    return diff
t = int(input())
for _ in range(t):
    n = int(input())
    b = list(map(int,input().split()))
    solution_matrix = []
    max = 0
    arr1 = b[::]
    arr2 = b[::]
    print(arr1)
    print(arr2)
    for i in range(n):
        arr1[i] = 1
        arr2[i] = b[i]
        max = max(max, get_diff(arr1), get_diff(arr2))

    print(max)
