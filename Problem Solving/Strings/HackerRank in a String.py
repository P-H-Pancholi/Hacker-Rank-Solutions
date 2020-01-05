valid = list("hackerrank")
q = int(input())
for _ in range(q):
    inp = input()
    i = 0
    for c in inp:
        if c == valid[i]:
            valid.remove(valid[i])
            i += 1
            if not valid:
                break
    if not (valid):
        print("YES")
    else:
        print("NO")
