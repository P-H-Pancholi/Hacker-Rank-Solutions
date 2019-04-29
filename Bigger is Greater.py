t = int(input())
for test in range(t):
	string = list(input())
	for i in range(len(string) - 1, 0, -1):
		char1 = string[i]
		char2 = string[i - 1]
		print("Comparing----->",char1,"<-->",char2)
		if char1 >= char2:
			temp = char1
			string[i] = char2
			string[i-1] = temp
			break
	print(string)
