num = input().strip()
sum = 0
MOD = 10**9 + 7
result = num[0]
sum += int(result)
for i in range(1,len(num)):
    numi = int(num[i])

    result = (i+1) * numi + 10*int(result)

    sum += int(result)


print(sum % MOD)
