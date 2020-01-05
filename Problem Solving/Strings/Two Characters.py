def validate(cpy):
    for i in range(len(cpy)-1):
        if cpy[i] == cpy[i+1]:
            return False
    return True

for _ in range(int(input().strip())):
    s = input().strip()
    st = list(set(s))
    max_len = 0
    for x in range(len(st)):
        for y in range(x+1, len(st)):
            cpy = [c for c in s if c==st[x] or c==st[y]]
            if validate(cpy):
                max_len = max(max_len, len(cpy))
    print(max_len)
