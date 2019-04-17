t = int(input())
numbers = []
for i in range(t):
	num = int(input())
	numbers.append(num)


divisors = []

for number in numbers:
	tempnumber = number

	count_divisors = 0
	while(tempnumber != 0):
		digit = tempnumber % 10
		if digit != 0:
			if number%digit == 0:
				count_divisors += 1
		tempnumber = int(tempnumber/10)
	divisors.append(count_divisors)

for i in range(t):
	print(divisors[i])
