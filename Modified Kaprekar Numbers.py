p = int(input())
q = int(input())
found = False
def kaprekar_number(number):
	global found
	#print(number)
	number = str(number)
	d = len(number)
	square = int(number) ** 2
	square = str(square)

	l = len(square)
	#print(square)
	if l == d:
		if number == '1':
			found = True
			print(number,end = " ")
	elif l == 2*d - 1:
		first_half = int(square[:d-1])
		right_half = int(square[-d:])
		#print("first_half---->",first_half,"right_half----->",right_half)
		if first_half + right_half == int(number):
			found = True
			print(number,end = " ")
	elif l == d*2:
		first_half = int(square[:-d])
		right_half = int(square[-d:])
		#print("first_half---->",first_half,"right_half----->",right_half)
		if first_half + right_half == int(number):
			found = True
			print(number,end = " ")

for i in range(p,q+1):
	kaprekar_number(i)
if found == False:
	print("INVALID RANGE")
