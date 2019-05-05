n_k = list(map(int,input().split()))
n,k = n_k[0],n_k[1]

clouds = list(map(int,input().split()))

cumulus = 0
thunderhead = 1

i = 0
e = 100

while True:
	i = (i + k) % n
	e -= 1
	if clouds[i] == thunderhead:
		e -= 2
	if i == 0:
		break

print(e)
