bnm = input()
bnm = bnm.split()
b = int(bnm[0])
n = int(bnm[1])
m = int(bnm[2])

keyboard = input()
keyboard = keyboard.split()

drives = input()
drives = drives.split()

amount = []

for kprice in keyboard:
    for dprice in drives:
        add = int(kprice) + int(dprice)
        amount.append(add)
amount.sort(reverse = True)

for price in amount:
    if price <= b:
        x = True
        break
    else:
        x = False

if x == True:
    print(price)
else:
    print(-1)
