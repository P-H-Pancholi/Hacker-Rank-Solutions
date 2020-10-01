n = int(input())
price = list(map(int, input().split()))

min_loss = float("inf")

for i in range(n-1):
    for j in range(i+1,n):
        loss = price[j] - price[i]
        if loss < 0:
            min_loss = min(min_loss, abs(price[j] - price[i]))

print(min_loss)
