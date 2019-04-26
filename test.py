q = int(input())
result = []

for i in range(0,q):
	a,b,n = input().split()
	n = int(n)
	str = (a + b)
	while( len(str) < n ):
		str = a + b
		a = b
		b = str
	str = list(str)
	result.append(str[n-1])

for  i in range(0,q):
	print(result[i])
