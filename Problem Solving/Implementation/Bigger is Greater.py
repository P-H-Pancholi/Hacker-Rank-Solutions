def findNext(arr):
	i = len(arr) - 1
	while i > 0 and arr[i-1] >= arr[i]:
		i -= 1
	if i <= 0:
		return False

	j = len(arr) -1
	#while arr[j] <= arr[i-1]:
	#	j -= 1

	arr[j],arr[i-1] = arr[i-1],arr[j]
	arr[i : ] = arr[len(arr) - 1 : i - 1 : -1]
	return True


t = int(input())
for _ in range(t):
	arr = list(input())
	if findNext(arr):
		print("".join(arr))
	else:
		print("no answer")
