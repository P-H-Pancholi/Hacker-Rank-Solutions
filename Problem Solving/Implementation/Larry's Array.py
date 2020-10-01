t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(input().split())
    swap_required = 0
    for i in range(n):
        for j in range(i+1,n):
            if arr[i] > arr[j]:
                swap_required += 1

    if swap_required % 2 == 0:
        print("YES")
    else:
        print("NO")
