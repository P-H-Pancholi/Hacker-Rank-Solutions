
string1 = list('mukund')
length_string1 = len(string1)
string2 = list('muk')
length_string2 = len(string2)

k = 2
cost = 0

if length_string1 + k > length_string2:
	print("No")

if length_string1 > length_string2:

	for i in range(length_string2,length_string1):
		string2.append(0)

	for i in range(0,length_string1 + 1):
		print(string2)
		print(string1)
		if string1[i] != string2[i]:
			for j in range(i,length_string1):
				string1.pop()
				cost += 1
			string1.append(string2[i])
			cost += 1

print(string1)
print(string2)
