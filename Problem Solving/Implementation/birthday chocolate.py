n = int(input())
s = input()
s = s.split()
d_m = input()
d_m = d_m.split()
d = int(d_m[0])
m =  int(d_m[1])
i = 0
count  = 0
for i in range(0,n - m + 1):
    total = 0
    for j in range(i,m+i):
        total = total + int(s[j])
    if total == d:
        count = count + 1
print(count)
