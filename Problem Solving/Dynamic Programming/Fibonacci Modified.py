t1,t2,n = map(int, input().split())

for i in range(3,n + 1):
    ti = t1 + (t2)**2
    t1 = t2
    t2 = ti
print(ti)
