n = int(input())
s = input()
count1 = 0

special_characters = "!@#$%^&*()-+"

parameters = [False,False,False,False,False]
if n < 6:
    count1 = 6 - len(s)
    parameters[0] = True
else:
    parameters[0] = True

for c in s:
    if ord(c) > 64 and ord(c) < 91:
        parameters[1] = True

    if ord(c) > 96 and ord(c) < 123:
        parameters[2]= True

    if ord(c) > 47 and ord(c) < 58:
        parameters[3] = True

    if c in special_characters:
        parameters[4] = True

count2 = 0

for check in parameters:
    if not check:
        count2 += 1

print(max(count1,count2))
