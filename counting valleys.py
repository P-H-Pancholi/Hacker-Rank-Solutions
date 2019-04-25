n = int(input())
<<<<<<< HEAD
path = list(input())
level = 0
valleys = 0
belowSea = False

for step in path:
	if step == 'U':
		level += 1
	else:
		level -= 1

	if not belowSea and level < 0:
		valleys += 1
		belowSea = True

	if level >= 0:
		belowSea = False

=======
path = input()
path  = path.split()
valleys = 0
depth = 0
height = 0
for i in range(len(path)):
    print("FOR PATH",path[i])
    if path[i] == 'U':
        height+=1
        print("HEIGHT->",height)
    if path[i] == 'D':
        depht-=1
        print("DEPTH->",depth)
    if depth < 0 and path[i] == 'U':
        depth+=1
        print("DEPTH->",depth)
    if height > 0 and path[i] == 'D':
        height-=1
        print("HEIGHT->",height)
    if depth == 0:
        valleys+=1
>>>>>>> b6b99a9ada68b527e54dce8a7170e53754a264ac
print(valleys)
