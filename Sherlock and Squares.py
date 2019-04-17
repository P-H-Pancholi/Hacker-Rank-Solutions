import math
t = int(input())
list_of_range = []
for i in range(t):
	range = list(map(int,input().split()))
	list_of_range.append(range)

for range in list_of_range:
	min = range[0]
	max = range[1]
	least_squre = math.ceil(math.sqrt(min))
	max_square = math.floor(math.sqrt(max))
	print(max_square - least_squre + 1)
