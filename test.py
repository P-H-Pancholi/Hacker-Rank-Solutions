def kaprekar_number(number):
	print(number)
	number = str(number)
	d = len(number)
	square = int(number) ** 2
	square = str(square)

	l = len(square)
	print(square)
	if l == d and number == '1':
		print(number)
	elif l == 2*d - 1:
		first_half = int(square[:d-1])
		right_half = int(square[-d:])
		print("first_half---->",first_half,"right_half----->",right_half)
		if first_half + right_half == int(number):
			print(number)
	else:
		first_half = int(square[:-d])
		right_half = int(square[-d:])
		print("first_half---->",first_half,"right_half----->",right_half)
		if first_half + right_half == int(number):
			print(number)

kaprekar_number(1)
