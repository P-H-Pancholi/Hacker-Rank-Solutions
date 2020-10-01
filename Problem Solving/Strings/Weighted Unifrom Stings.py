l = [c for c in "abcdefghijklmnopqrstuvwxyz"]




s = input()

weights = set()
prev = -1
length = 0
for c in s:
    weight = ord(c) - ord('a') + 1
    weights.add(weight)
    if prev == c:
        length += 1
        weights.add(length*weight)
    else:
        prev = c
        length = 1

#print(weight)


n = int(input())

for _ in range(n):
    query = int(input())
    if query in weights:
        print("Yes")
    else:
        print("No")
