n,d  = map(int,input().split())
arr = list(map(int,input().split()))

count = 0

for i in range(0,n):
	arr_i = arr[i]
	arr_k = 2*d + arr_i
	arr_j = (arr_i + arr_k)//2

	if arr_j in arr and arr_k in arr and arr_j > arr_i and arr_k > arr_j and arr_k > arr_i:
		count += 1

print(count)
