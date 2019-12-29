s = list(input())
stack = []
for c in s:
    if not stack:
        stack.append(c)
    else:
        if stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)

if not s:
    print("Empty String")
else:
    print(s)
