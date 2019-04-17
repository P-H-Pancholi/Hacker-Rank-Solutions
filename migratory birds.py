n = int(input())
birds = input()
birds = birds.split()
ctype1=0
ctype2=0
ctype3=0
ctype4=0
ctype5 = 0
for i in range(0,n):
    if int(birds[i]) == 1:
        ctype1 = ctype1 + 1
    elif int(birds[i]) == 2:
        ctype2 = ctype2 + 1
    elif int(birds[i]) == 3:
        ctype3 = ctype3 + 1
    elif int(birds[i]) == 4:
        ctype4 = ctype4 + 1
    else:
        ctype5 = ctype5 + 1
find = [ctype1,ctype2,ctype3,ctype4,ctype5]
found = max(find)
for index,x in enumerate(find):
    if x == found:
        print(index+1)
        break
        


