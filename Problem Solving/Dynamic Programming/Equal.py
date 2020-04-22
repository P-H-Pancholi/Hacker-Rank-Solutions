t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))

    cnt = 0

    lowest = min(arr)

    result = []

    possible_min = [i for i in range(lowest-5,lowest+1)]

    for mini in possible_min:
        cnt = 0
        for val in arr:
            diff = val - mini
            cnt += diff // 5 + (diff % 5) // 2 + (diff % 5) % 2
        #print(mini, cnt )
        result.append(cnt)

    ans = min(result)
    print(ans)
