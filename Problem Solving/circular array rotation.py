n, k, q = map(int, input().split())
arr = list(map(int,input().split()))
for _ in range(q):
    print(arr[(int(input()) + n - k) % n])
