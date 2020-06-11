n = int(input())
sticks_l = map(int,input().split())
sorted_sticks_l = sorted(sticks_l, reverse = True)

max_perimeter = 0

for i in range(n-2):
    l1,l2,l3 = sorted_sticks_l[i:i+3]
    if l2 + l3 > l1:
        max_perimeter = l1 + l2 + l3

print(max_perimeter)
