n = int(raw_input().strip())
a = map(int,raw_input().strip().split(' '))

maximum = 0
diff = 1

for k in a:
    n1 = a.count(k)
    n2 = a.count(k-diff)
    maximum = max(maximum, n1+n2)

print maximum
