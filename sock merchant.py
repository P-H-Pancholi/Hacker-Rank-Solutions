n = int(input())
socks = input()
socks = socks.split()

pairs = 0
socks_set = set(socks)
i = 0
for sock in socks_set:
    count = 0
    for i in range(len(socks)):
        if sock == socks[i]:
            count +=1
    pairs = pairs + count//2
print(pairs)
