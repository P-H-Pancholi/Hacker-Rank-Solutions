n, k = map(int,input().split())
l = []
for _ in range(n):
    i,t = map(int,input().split())
    l.append([i,t])


sorted_l = sorted(l, reverse = True)
#print(sorted_l)

max_luck = 0

for i,t in sorted_l:
    if t == 1:
        if k > 0:
            max_luck += i
            k -= 1
        else:
            max_luck -= i
    else:
        max_luck += i

print(max_luck)
