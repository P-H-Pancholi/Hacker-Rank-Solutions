n = int(input())
list = []
for _ in range(n):
	command = input().split()
	if command[0] == 'insert':
		position, number = int(command[1]),int(command[2])
		if len(list) == 0 or position >= len(list):
			list.append(number)
		else:
			list.insert(position,number)
	elif command[0] == 'print':
		print(list)
	elif command[0] == 'remove':
		number = int(command[1])
		list.remove(number)
	elif command[0] == 'append':
		number = int(command[1])
		list.append(number)
	elif command[0] == 'sort':
		list.sort()
	elif command[0] == 'pop':
		list.pop()
	elif command[0] == 'reverse':
		list.reverse()
	else:
		print("INVALID")
