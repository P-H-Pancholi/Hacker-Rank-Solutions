#input
n = int(input())
arr = list(map(int,input().split()))

#sort the array in ascendng order
arr.sort()

#initialize variables

sticks_left_at_each_iteration = []

#begin cutting
while len(arr) > 0:

	min_length = arr[0]

	sticks_left_at_each_iteration.append(len(arr))

	while min_length in arr:
		arr.remove(min_length)

	for i in range(0,len(arr)):
		arr[i] -= min_length
for i in range(0,len(sticks_left_at_each_iteration)):
	print(sticks_left_at_each_iteration[i])
