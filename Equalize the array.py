n = int(input())
arr = list(map(int,input().split()))
set_arr = set(arr)

repetitions = []

for num in set_arr:
	count = arr.count(num)
	repetitions.append(count)

print(n - max(repetitions))
