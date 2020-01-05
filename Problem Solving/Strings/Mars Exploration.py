inp = input()
count = 0
for i in range(len(inp)):
    if i % 3 == 0:
        if inp[i] != 'S':
            count += 1
    if i % 3 == 1:
        if inp[i] != 'O':
            count += 1
    if i % 3 == 2:
        if inp[i] != 'S':
            count += 1

print(count)
