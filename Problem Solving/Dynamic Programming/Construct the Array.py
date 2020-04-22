
t = int(input())
for _ in range(t):
    n,k,x = map(int,input().split())
    cnt = 0
    MOD = 10**9 + 7

    a0 = 0
    a1 = 1

    k1 = k - 1
    k2 = k - 2

    for i in range(n-2):
        at = (a0 * k2 + a1) % MOD
        a1 = (a0 * k1) % MOD
        a0 = at

    if x == 1:
        print((a0 * k1) % MOD)
    else:
        print((a0 * k2 + a1) % MOD)
