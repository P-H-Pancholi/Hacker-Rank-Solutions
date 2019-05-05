n = int(raw_input())
shared = 5
total = 0
for day in range(n):
     liked = int(shared / 2)
     total += liked
     shared = liked * 3
print total
