import math
str = input()
str = str.replace(" ","")
length = len(str)

rows = math.floor(math.sqrt(length))
columns = math.ceil(math.sqrt(length))


if rows * columns < length:
	rows += 1

for i in range(0,columns):
	for j in range(i,length,columns):
		print(str[j],end = "")
	print(" ",end = "")
