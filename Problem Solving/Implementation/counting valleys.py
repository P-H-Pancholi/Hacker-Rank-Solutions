n = int(input())
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
print(valleys)
